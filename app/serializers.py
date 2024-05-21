from rest_framework import serializers
from .models import User, Project, Task, Tag

class UserSerializer(serializers.ModelSerializer):
    def validate_mail(self, value):
        if User.objects.filter(mail=value).exists():
            raise serializers.ValidationError("Email já está em uso.")
        return value

    class Meta:
        model = User
        fields = ['id', 'username', 'mail', 'name', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'members', 'created_by']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("O nome do projeto é obrigatório.")
        return value

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'status', 'project', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        task = Task.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            task.tags.add(tag)
        return task

    def update(self, instance, validated_data):
        if instance.status == Task.StatusChoices.CONCLUIDA:
            raise serializers.ValidationError("Tarefas concluídas não podem ser editadas.")
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.project = validated_data.get('project', instance.project)
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            instance.tags.add(tag)
        
        return instance


import logging
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User, Project, Task, Tag
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, TagSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CanCreateUser
from django.http import Http404

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CanCreateUser]

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"Novo usuário criado: {serializer.instance.username}")

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        logger.info(f"Novo projeto criado por {self.request.user.username}: {serializer.instance.name}")


    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        project = self.get_object()
        if project.created_by != request.user:
            return Response({'error': 'Esse usuário não pode adicionar membros'}, status=403)
        user_id = request.data.get('user_id')
        try:
            user = get_object_or_404(User, id=user_id)
        except Http404:
            return Response({'error': 'O usuário não existe'}, status=404)
        project.members.add(user)
        return Response({'status': 'Usuário adicionado com sucesso'})

    @action(detail=True, methods=['post'])
    def remove_member(self, request, pk=None):
        project = self.get_object()
        if project.created_by != request.user:
            return Response({'error': 'Permissão negada'}, status=403)
        user_id = request.data.get('user_id')
        try:
            user = get_object_or_404(User, id=user_id)
        except Http404:
            return Response({'error': 'O usuário não existe'}, status=404)
        project.members.remove(user)
        return Response({'status': 'Membro removido com sucesso'})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if self.request.user not in project.members.all():
            raise ValidationError("Somente membros do projeto podem criar tarefas.")
        if not serializer.validated_data['tags']:
            raise ValidationError("A tarefa deve ter pelo menos uma tag.")
        serializer.save()

    def perform_update(self, serializer):
        if serializer.instance.status == Task.StatusChoices.CONCLUIDA:
            raise ValidationError("Tarefas concluídas não podem ser editadas.")
        if not serializer.validated_data['tags']:
            raise ValidationError("A tarefa deve ter pelo menos uma tag.")
        serializer.save()

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
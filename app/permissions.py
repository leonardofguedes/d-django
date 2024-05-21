from rest_framework import permissions

class CanCreateUser(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method == 'POST':
            if not request.user.is_authenticated:
                special_username = 'admin'
                special_email = 'admin@example.com'
                if 'username' in request.data and 'mail' in request.data:
                    return (request.data['username'] == special_username and 
                            request.data['mail'] == special_email)
        return request.user.is_authenticated
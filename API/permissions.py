from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite operaciones de lectura (GET, HEAD, OPTIONS) para cualquier solicitud
        if request.method in permissions.SAFE_METHODS:
            return True
        # Requiere autenticación para operaciones de escritura (POST, PUT, DELETE)
        return request.user and request.user.is_authenticated

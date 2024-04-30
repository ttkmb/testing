from rest_framework.permissions import IsAuthenticated


class IsActive(IsAuthenticated):

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_active
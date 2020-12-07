from rest_framework import permissions

class IsAssigned(permissions.BasePermission):
    """ Determines if the damn thing is from the user or not """ 
    def has_object_permission(self, request, view, obj):
        if obj.assigned_to == request.user: 
            return True 
        else: 
            return False
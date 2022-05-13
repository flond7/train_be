from urllib import request
from rest_framework import permissions

class notDeletingPermission(permissions.DjangoModelPermissions):
  # only if user is not active return False and deny access
  # otherwise allow it

  perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': [],
  }

  def has_permission(self, request, view):
    if not request.user.is_active:
      return False
    return super().has_permission(request, view)

  """ def has_permission(self, request, view):
    user = request.user
    print(user.get_all_permissions())
    if user.is_active:
 
      # if the user has the permission for
      # appName.actionYouWantToDo_modelName 
      # return true and allow it otherwise 
      # return False and deny it
      if user.has_perm("api.add_user"):   
        return True
      return False
    return False """

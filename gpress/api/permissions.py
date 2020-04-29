from rest_framework import permissions
from logging import getLogger
logger = getLogger(__name__)


class BasePermission(permissions.IsAuthenticated):
    PERM_CODE = None

    def has_permission(self, request, view):
        isvalid = (request.method in permissions.SAFE_METHODS) \
            or request.user.has_perm(self.PERM_CODE)
        if not isvalid:
            logger.info(f"{request.user} has not {self.PERM_CODE}")
        return isvalid


class Permission(BasePermission):
    PERM_CODE = 'gpress.change_wpposts'

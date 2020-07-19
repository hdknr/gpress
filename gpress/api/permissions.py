from apibase import permissions
from logging import getLogger
logger = getLogger(__name__)


class Permission(permissions.Permission):
    PERM_CODE = 'gpress.change_wpposts'
    PRIVATE = False

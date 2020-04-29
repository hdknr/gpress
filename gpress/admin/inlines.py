from django.contrib import admin
from .. import models


class WpPostmetaInline(admin.TabularInline):
    model = models.WpPostmeta
    extra = 0

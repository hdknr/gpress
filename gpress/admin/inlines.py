from django.contrib import admin
from .. import models


class PostmetaInline(admin.TabularInline):
    model = models.Postmeta
    extra = 0

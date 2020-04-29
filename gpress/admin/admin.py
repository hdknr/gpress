from django.contrib import admin
from .. import models


def default_list_display(model, exclude=[]):
    return [
        f.name for f in model._meta.fields
        if f.name not in exclude
    ]


@admin.register(models.WpPosts)
class WpPostsAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.WpPosts)


@admin.register(models.WpLinks)
class WpLinksAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.WpLinks)


@admin.register(models.WpOptions)
class WpOptionsAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.WpOptions)


@admin.register(models.WpPostmeta)
class WpPostmetaAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.WpPostmeta)
    # raw_id_fields = ['post', ]

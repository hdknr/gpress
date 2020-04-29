from django.contrib import admin
from .. import models
from . import inlines

def default_list_display(model, exclude=[]):
    return [
        f.name for f in model._meta.fields
        if f.name not in exclude
    ]


@admin.register(models.WpPosts)
class WpPostsAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.WpPosts)
    raw_id_fields = ['post_parent', ]
    inlines = [
        inlines.WpPostmetaInline,
    ]

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

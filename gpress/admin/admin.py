from django.contrib import admin
from django.utils.safestring import mark_safe

from .. import models
from . import inlines

import json


def default_list_display(model, exclude=[]):
    return [
        f.name for f in model._meta.fields
        if f.name not in exclude
    ]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.Post)
    raw_id_fields = ['post_parent', ]
    inlines = [
        inlines.PostmetaInline,
    ]
    search_fields = ['post_title', 'post_content', ]
    list_filter = ['post_type', 'post_status', ]

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.Link)


@admin.register(models.Option)
class OptionsAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.Option)
    search_fields = ['option_name', 'option_value', ]


@admin.register(models.Postmeta)
class PostmetaAdmin(admin.ModelAdmin):
    list_display = default_list_display(models.Postmeta)
    raw_id_fields = ['post', ]
    list_filter = ['meta_key', ]
    search_fields = ['post__post_title', 'post__post_content', ]
    readonly_fields = ['meta_value_obj_json']

    def meta_value_obj_json(self, obj):
        data = json.dumps(obj.meta_value_obj, indent=2, ensure_ascii=False)
        return mark_safe(f"<pre>{data}</pre>")

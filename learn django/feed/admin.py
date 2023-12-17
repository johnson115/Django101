from django.contrib import admin
from .models import Post

class postAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,postAdmin)
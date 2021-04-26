from django.contrib import admin
from .models import post, comment
# Register your models here.


class commentInline(admin.TabularInline): # new
    model =comment
    # extra = 0
class postAdmin(admin.ModelAdmin): # new
    inlines = [
    commentInline,
    ]
admin.site.register(post, postAdmin) # new
admin.site.register(comment)

# admin.site.register(post)
# admin.site.register(comment)
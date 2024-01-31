from django.contrib import admin
from .models import  Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("titulo","autor",)
    #para que no se muestre en el admin 
    exclude = ('created', 'updated')


admin.site.register(Post, PostAdmin)
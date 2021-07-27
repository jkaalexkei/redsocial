from django.contrib import admin

# Register your models here.

from .models import Post,Perfil,RelationsShip


admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(RelationsShip)

from django.contrib import admin
from .models import Usuario, Pregunta, Resultado
from django.contrib.auth.admin import UserAdmin

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rol', {'fields': ('rol',)}),
    )

admin.site.register(Pregunta)
admin.site.register(Resultado)

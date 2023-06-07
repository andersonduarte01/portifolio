from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ..core.models import Usuario
from ..core.forms import UserCreationForm, UserChangeForm


# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'nome', 'is_admin', 'is_vendedor')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nome',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_vendedor')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Usuario, UserAdmin)

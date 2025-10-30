from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomCreationForm,CustomChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_staff', 'is_active', 'age', 'is_agent'
    )
    list_filter = (
        'is_staff', 'is_active', 'is_agent'
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'is_agent', 'agency_name', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
                'age', 'is_agent', 'agency_name', 'phone_number'
            )
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

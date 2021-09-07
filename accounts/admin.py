from django.contrib import admin
from accounts.models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('email', 'username', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'username')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login', )
    fieldsets=()
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'phone', 'password1', 'password2'),

        }),
    )
    ordering=('email',)




admin.site.register(MyUser, MyUserAdmin)
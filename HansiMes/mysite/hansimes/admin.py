from django.contrib import admin
from hansimes.models import ContactMess, User

# Register your models here.
@admin.register(ContactMess)
class ContactMessAdmin(admin.ModelAdmin):
    list_display = (
        'Name',
        'Email',
        'Message',
        'Created_at'
    )
    search_fields = ('Name', 'Email', 'Message')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'password',
        'created_at'
    )
    search_fields = ('username', 'email', 'password')
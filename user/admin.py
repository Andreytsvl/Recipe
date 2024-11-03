
from user.models import User
from django.contrib import admin



#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'registration_date')
    search_fields = ('username',)
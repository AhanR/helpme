from django.contrib import admin

# Register your models here.
from .models import Posts, User

admin.site.register(User)
admin.site.register(Posts)
from django.contrib import admin

from .models import Member

from .models import Notification

admin.site.register(Notification)

admin.site.register(
    Member
)
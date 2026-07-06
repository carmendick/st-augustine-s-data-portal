from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Notification(models.Model):

    TYPES = [

        ("birthday", "Birthday"),

        ("system", "System"),

        ("announcement", "Announcement"),

        ("profile", "Profile"),

    ]

    recipient = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="notifications"

    )

    title = models.CharField(

        max_length=150

    )

    message = models.TextField()

    notification_type = models.CharField(

        max_length=20,

        choices=TYPES,

        default="system"

    )

    is_read = models.BooleanField(

        default=False

    )

    created = models.DateTimeField(

        default=timezone.now

    )

    class Meta:

        ordering = ["-created"]

    def __str__(self):

        return self.title


class Member(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    photo = models.ImageField(
    upload_to="profiles/",
    blank=True,
    null=True
    )

    STATUS = [

        ('Single', 'Single'),

        ('Married', 'Married'),

        (
            'Relationship',
            'In a Relationship'
        )

    ]

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    photo = models.ImageField(
    upload_to='profiles/',
    blank=True,
    null=True
)

    birthday = models.DateField()

    state_origin = models.CharField(
        max_length=100
    )

    state_residence = models.CharField(
        max_length=100
    )

    relationship_status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    show_phone = models.BooleanField(
        default=False
    )

    show_relationship = models.BooleanField(
        default=False
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.full_name
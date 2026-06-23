from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
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
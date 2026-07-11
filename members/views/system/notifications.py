from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from members.models import Notification


@login_required
def notifications(request):

    notifications = Notification.objects.filter(

        recipient=request.user

    ).order_by("-created")

    return render(

        request,

        "notifications.html",

        {

            "notifications": notifications

        }

    )
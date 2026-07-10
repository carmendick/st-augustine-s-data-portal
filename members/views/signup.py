from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from members.forms import SignUpForm
from members.models import Notification


def signup(request):

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            Notification.objects.create(
                recipient=user,
                title="Welcome!",
                message=(
                    "Welcome to the St. Augustine Community Portal. "
                    "We're delighted to have you with us."
                ),
                notification_type="system",
            )

            messages.success(
                request,
                "Your account has been created successfully."
            )

            return redirect("profile")

    else:

        form = SignUpForm()

    return render(
        request,
        "signup.html",
        {
            "form": form
        }
    )
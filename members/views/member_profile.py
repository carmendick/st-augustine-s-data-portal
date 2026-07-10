from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from members.models import Member


@login_required
def member_profile(request, pk):

    member = get_object_or_404(

        Member,

        pk=pk

    )

    return render(

        request,

        "member_profile.html",

        {

            "member": member

        }

    )
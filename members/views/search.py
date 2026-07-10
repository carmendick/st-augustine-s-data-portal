from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from members.models import Member


@login_required
def search(request):

    query = request.GET.get("q", "").strip()

    members = Member.objects.none()

    if query:

        members = Member.objects.filter(

            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(state_origin__icontains=query) |
            Q(state_residence__icontains=query) |
            Q(relationship_status__icontains=query)

        )

    return render(

        request,

        "search_results.html",

        {

            "query": query,

            "members": members,

        }

    )
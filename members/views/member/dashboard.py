from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from members.models import Member

@login_required
def dashboard(request):

    members = Member.objects.all()

    today = date.today()

    total_members = members.count()

    upcoming = []

    states = set()

    for m in members:

        # Count unique states
        if m.state_residence:

            states.add(
                m.state_residence
    )

        next_day = m.birthday.replace(
            year=today.year
        )

        if next_day < today:

            next_day = next_day.replace(
                year=today.year + 1
            )

        m.days_left = (
            next_day -
            today
        ).days

        if m.days_left <= 30:

            upcoming.append(m)

        

    upcoming.sort(
        key=lambda x: x.days_left
    )

    context = {

        "total_members": total_members,

        "upcoming_birthdays": len(upcoming),

        "states_count": len(states),

        "upcoming": upcoming[:6],

    }

    return render(

        request,

        "dashboard.html",

        context

    )

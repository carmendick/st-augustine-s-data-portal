from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from members.models import Member



@login_required
def directory(request):

    members = (
        Member.objects.all()
    )

    today = date.today()

    q = request.GET.get(
        'q'
    )

    state = request.GET.get(
        'state'
    )

    status = request.GET.get(
        'status'
    )

    upcoming = request.GET.get(
        'upcoming'
    )


    # SEARCH EVERYTHING

    if q:

        members = (

            members.filter(

                Q(
                    full_name__icontains=q
                )

                |

                Q(
                    phone__icontains=q
                )

                |

                Q(
                    state_origin__icontains=q
                )

                |

                Q(
                    state_residence__icontains=q
                )

                |

                Q(
                    relationship_status__icontains=q
                )

            )

        )


    members = list(
        members
    )


    for m in members:

        next_birthday = (

            m.birthday.replace(
                year=today.year
            )

        )

        if next_birthday < today:

            next_birthday = (

                next_birthday.replace(
                    year=today.year + 1
                )

            )

        m.days_left = (

            next_birthday
            -
            today

        ).days


    if state:

        members = [

            m

            for m

            in members

            if

            m.state_residence
            ==
            state

        ]


    if status:

        members = [

            m

            for m

            in members

            if

            m.relationship_status
            ==
            status

        ]


    if upcoming:

        members = [

            m

            for m

            in members

            if

            m.days_left
            <=
            30

        ]


    members.sort(
        key=lambda x:
        x.days_left
    )


    return render(

        request,

        'directory.html',

        {

            'members':members,

            'query':q

        }

    )

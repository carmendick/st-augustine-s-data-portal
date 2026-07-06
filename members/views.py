from django.shortcuts import (
render,
redirect
)

from django.contrib.auth import (
login
)

from django.contrib.auth.decorators import (
login_required
)

from .forms import (
SignUpForm,
ProfileForm
)

from .models import (
Member, Notification
)

from datetime import (
date
)

from datetime import date

from django.db.models import Count



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


def home(request):

    return render(
        request,
        'home.html'
    )


def signup(request):

    if request.method == 'POST':

        form = SignUpForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            return redirect(
                'profile'
            )

    else:

        form = SignUpForm()

    Notification.objects.create(

    recipient=user,

    title="Welcome!",

    message="Welcome to the St. Augustine Community Portal. We're delighted to have you with us.",

    notification_type="system"

)

    return render(
        request,
        'signup.html',
        {'form': form}
    )


@login_required
def profile(request):

    try:

        member = Member.objects.get(
            user=request.user
        )

    except Member.DoesNotExist:

        member = None

    if request.method == 'POST':

        form = ProfileForm(
request.POST,
request.FILES,
instance=member
)

        if form.is_valid():

            profile = form.save(
                commit=False
            )

            profile.user = (
                request.user
            )

            profile.save()

            return redirect(
                'directory'
            )

    else:

        form = ProfileForm(
            instance=member
        )

        

    return render(

        request,

        'profile.html',

        {

            'form': form,
            'member': member

        }

    )




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


@login_required
def notifications(request):

    notifications = Notification.objects.filter(

        recipient=request.user

    )

    return render(

        request,

        "notifications.html",

        {

            "notifications": notifications

        }

    )

########################################
# from django.shortcuts import (
# render,
# redirect
# )

# from django.contrib.auth import (
# login
# )

# from .forms import (
# SignUpForm
# )


# def home(request):

#     return render(
#         request,
#         'home.html'
#     )


# def signup(request):

#     if request.method == 'POST':

#         form = SignUpForm(
#             request.POST
#         )

#         if form.is_valid():

#             user = form.save()

#             login(
#                 request,
#                 user
#             )

#             return redirect(
#                 '/'
#             )

#     else:

#         form = SignUpForm()

#     return render(

#         request,

#         'signup.html',

#         {

#         'form': form

#         }

#     )


####################################
# # from django.shortcuts import (
#     render,
#     redirect
# )

# from .forms import MemberForm


# def home(request):

#     if request.method == 'POST':

#         form = MemberForm(
#             request.POST
#         )

#         if form.is_valid():

#             form.save()

#             return redirect(
#                 'success'
#             )

#     else:

#         form = MemberForm()

#     return render(

#         request,

#         'home.html',

#         {

#             'form': form

#         }

#     )


# def success(request):

#     return render(
#         request,
#         'success.html'
#     )
######################################
# from django.shortcuts import render


# def home(request):

#     return render(
#         request,
#         'home.html'
#     )

################################
# from django.http import HttpResponse


# def home(request):

#     return HttpResponse(
#         """
#         <h1>🎂 Birthday Portal</h1>

#         <p>My first full-stack Python website.</p>
#         """
#     )
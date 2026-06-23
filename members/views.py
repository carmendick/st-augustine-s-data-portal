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
Member
)

from datetime import (
date
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

            'form': form

        }

    )


@login_required
def directory(request):

    members = list(
        Member.objects.all()
    )

    today = date.today()

    state = (
        request.GET.get(
            'state'
        )
    )

    status = (
        request.GET.get(
            'status'
        )
    )

    upcoming = (
        request.GET.get(
            'upcoming'
        )
    )

    for m in members:

        next_birthday = (
            m.birthday.replace(
                year=today.year
            )
        )

        if (
            next_birthday
            <
            today
        ):

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

            'members': members

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
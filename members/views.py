from django.shortcuts import (
render,
redirect
)

from django.contrib.auth import (
login
)

from .forms import (
SignUpForm
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
                '/'
            )

    else:

        form = SignUpForm()

    return render(

        request,

        'signup.html',

        {

        'form': form

        }

    )


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
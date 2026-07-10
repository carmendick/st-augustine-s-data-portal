from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from members.forms import ProfileForm
from members.models import Member


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
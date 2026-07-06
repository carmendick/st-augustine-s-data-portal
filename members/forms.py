from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import (
    UserCreationForm
)

from .models import Member


class SignUpForm(
    UserCreationForm
):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [

            'username',

            'email',

            'password1',

            'password2'

        ]


class ProfileForm(
    forms.ModelForm
):

    class Meta:

        model = Member

        fields = [
            "photo",
            "full_name",
            "phone",
            "birthday",
            "state_origin",
            "state_residence",
            "relationship_status",
            "show_phone",
            "show_relationship",
]


###########################################
# from django import forms

# from django.contrib.auth.models import User

# from django.contrib.auth.forms import (
#     UserCreationForm
# )

# from .models import Member


# class SignUpForm(
#     UserCreationForm
# ):

#     email = forms.EmailField()

#     class Meta:

#         model = User

#         fields = [

#             'username',

#             'email',

#             'password1',

#             'password2'

#         ]
#############################
# from django import forms
# from .models import Member


# class MemberForm(forms.ModelForm):

#     class Meta:

#         model = Member

#         fields = [

#             'full_name',

#             'phone',

#             'birthday',

#             'state_origin',

#             'state_residence',

#             'relationship_status',

#             'show_phone',

#             'show_relationship'

#         ]
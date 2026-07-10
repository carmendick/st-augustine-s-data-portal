from django.urls import path

from .views.system import notifications

from .views.member import directory, profile

from .views.search import search

from .views import (
    home,
    signup,
    dashboard,
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'sign-up/',
        signup,
        name='signup'
    ),

    path(
        'profile/',
        profile,
        name='profile'
    ),

    path(
        'directory/',
        directory,
        name='directory'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'notifications/',
        notifications,
        name='notifications'
    ),

    path(
        "search/",
        search,
        name="search"
),

    path(
    "members/",
    member_profile,
    name="member_profile"
),
]


####################################
# from django.urls import path

# from .views import (
# home,
# signup
# )


# urlpatterns=[

# path(
# '',
# home,
# name='home'
# ),

# path(
# 'sign-up/',
# signup,
# name='signup'
# ),

# ]

######################################################

# from django.urls import path

# from .views import (
#     home,
#     success
# )


# urlpatterns = [

# path(
# '',
# home,
# name='home'
# ),

# path(
# 'success/',
# success,
# name='success'
# ),

# ]


#####################################
# # from django.urls import path
# from .views import home


# urlpatterns = [

# path('', home),

# ]
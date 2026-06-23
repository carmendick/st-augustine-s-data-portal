from django.urls import path

from .views import (
home,
signup,
profile,
directory
)

urlpatterns=[

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
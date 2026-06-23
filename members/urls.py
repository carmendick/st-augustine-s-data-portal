from django.urls import path

from .views import (
home,
signup
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

]

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
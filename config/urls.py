from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

path(
'admin/',
admin.site.urls
),

path(
'',
include(
'members.urls'
)
),

path(
'accounts/',

include(
'django.contrib.auth.urls'
)

),

path(
'login/',
views.LoginView.as_view(
template_name='login.html'
),
name='login'
),

]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
# urlpatterns = [

# path(
# 'admin/',
# admin.site.urls
# ),

# path(
# '',
# include('members.urls')
# ),

# ]
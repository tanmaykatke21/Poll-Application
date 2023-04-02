from django.contrib import admin
from django.urls import path
from auth_app.views import ulogin, usignup, uwelcome

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',ulogin,name="ulogin"),
	path('usignup',usignup,name='usignup'),
	path('uwelcome',uwelcome,name='uwelcome'),
]

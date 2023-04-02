from django.contrib import admin
from django.urls import path
from auth_app.views import ulogin, usignup, uwelcome, ulogout, ucp

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',ulogin,name="ulogin"),
	path('usignup',usignup,name='usignup'),
	path('uwelcome',uwelcome,name='uwelcome'),
	path('ulogout',ulogout,name='ulogout'),
	path('ucp',ucp,name='ucp'),
]

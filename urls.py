from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

from django.contrib.auth.forms import AuthenticationForm

from views import UserProfile, Logout, Registration
from forms import JDUAuthenticationForm
urlpatterns = patterns('',)


# As this login uses django.contrib.auth.views.login we need to add the
# login redirect tothe settings file using the LOGIN_REDIRECT_URL
#
# The pattern of urls should work thusly within this app:
# login get = loginformpage
# login post = LOGIN_REDIRECT_URL  if loginsuccessful else loginformpage
#
# LOGIN_REDIRECT_URL get = redirect to LOGIN_REDIRECT_URL/currentuser
#
# currentuser get



urlpatterns += patterns('', url( '^login/$', login, {'template_name':'justdifferentusers/generic.html','authentication_form':JDUAuthenticationForm, }, name='login' )) # 'redirect_field_name':'profile'
urlpatterns += patterns('', url( "^logout/$", Logout.as_view(), {'next_page': '/successfully_logged_out/'},name="logout"))
urlpatterns += patterns('', url( "^user/$", UserProfile.as_view(), {}, name="profile"))
urlpatterns += patterns('', url( "^register/$", Registration.as_view(), {'success_url':'/auth/user'}, name="register"))


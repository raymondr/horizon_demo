from django import shortcuts
from django.views.decorators import vary

import horizon
from horizon.views import auth as auth_views


def user_home(user):
    if user.admin:
        return horizon.get_dashboard('syspanel').get_absolute_url()
    return horizon.get_dashboard('nova').get_absolute_url()


# Copied from OpenStack Dashboard
@vary.vary_on_cookie
def splash(request):
    if request.user.is_authenticated():
        return shortcuts.redirect(user_home(request.user))
    form, handled = auth_views.Login.maybe_handle(request)
    if handled:
        return handled
    request.session.clear()
    return shortcuts.render(request, 'splash.html', {'form': form})

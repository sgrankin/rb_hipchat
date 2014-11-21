from __future__ import unicode_literals

from django.conf.urls import patterns, url

from rb_hipchat.extension import RbHipchat
from rb_hipchat.forms import RbHipchatSettingsForm


urlpatterns = patterns(
    '',
    url(r'^$',
        'reviewboard.extensions.views.configure_extension',
        {
            'ext_class': RbHipchat,
            'form_class': RbHipchatSettingsForm,
        })
)

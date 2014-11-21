from django import forms
from djblets.extensions.forms import SettingsForm


class RbHipchatSettingsForm(SettingsForm):
    enabled = forms.BooleanField(initial=False, required=False)
    token = forms.CharField(help_text="HipChat access token")
    room = forms.IntegerField(help_text="HipChat room ID")
    user = forms.CharField(help_text="User Name")


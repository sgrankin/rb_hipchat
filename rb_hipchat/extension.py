# rb-hipchat Extension for Review Board.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include
from django.utils.six.moves.urllib.parse import urljoin
from reviewboard.admin.server import get_server_url
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import SignalHook
from reviewboard.reviews.signals import review_request_published
import hipchat

class RbHipchat(Extension):
    metadata = {
        'Name': 'HipChat',
        'Summary': 'ReviewBoard HipChat integration',
    }
    is_configurable = True
    default_settings = {
        'enabled': False,
        'token': '',
        'room': 0,
        'user': ''
    }

    def initialize(self):
        SignalHook(self, review_request_published, self.on_published)


    def on_published(self, review_request=None, changedesc=None, **kwargs):
        if not self.settings['enabled'] or not self.settings['token'] or not self.settings['room']:
            return

        local_site = review_request.local_site
        base_url = get_server_url(local_site=local_site)
        url = urljoin(base_url, review_request.get_absolute_url())
        message = '{author}: <a href="{url}">{title}</a>'.format(
            author=review_request.submitter.username,
            title=review_request.summary,
            url=url)

        hipster = hipchat.HipChat(token=self.settings['token'])

        hipster.method('rooms/message', method='POST', parameters={
            'room_id': int(self.settings['room']),
            'from': self.settings['user'],
            'message': message,
            'message_format': 'html',
            'color': 'purple',
        })


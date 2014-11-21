from __future__ import unicode_literals

from reviewboard.extensions.packaging import setup


PACKAGE = "rb-hipchat"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="ReviewBoard HipChat integration",
    author="None",
    packages=["rb_hipchat"],
    entry_points={
        'reviewboard.extensions':
            '%s = rb_hipchat.extension:RbHipchat' % PACKAGE,
    },
    install_requires=[
	'python-simple-hipchat',
    ],
)

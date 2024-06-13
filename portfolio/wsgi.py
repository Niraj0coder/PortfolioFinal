"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
app =application

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "verceldb",
#         'USER': "default",
#         'PASSWORD':"xOmkhwa6Z3jc",
#         'HOST': "ep-super-wood-a4z0dmm7-pooler.us-east-1.aws.neon.tech",
#         'PORT': 5432,
#     }
# }

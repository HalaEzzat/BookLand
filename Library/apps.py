from django.apps import AppConfig
from ddtrace import config
from ddtrace import patch_all
config.env = "dev"      # the environment the application is in
config.service = "BookLand"  # name of your application
config.version = "0.1"  # version of your application
patch_all()
class LibraryConfig(AppConfig):
    name = 'Library'

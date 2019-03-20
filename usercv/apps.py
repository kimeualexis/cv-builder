from django.apps import AppConfig


class UsercvConfig(AppConfig):
    name = 'usercv'

    def ready(self):
        import usercv.signals

from django.apps import AppConfig


class SettingemployerConfig(AppConfig):
    name = 'settingEmployer'

    def ready(self):
        import settingEmployer.signals

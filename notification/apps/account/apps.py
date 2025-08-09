from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.account'

    def ready(self):
        # این بخش بدون تغییر باقی می‌ماند
        import apps.account.signals
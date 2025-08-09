# apps/notif/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
#  تغییر ۱: مدل کاربر سفارشی خودتان را import کنید
from .models import CustomUser  
from django_eventstream import send_event

# تغییر ۲: در دکوراتور، sender را به CustomUser تغییر دهید
@receiver(post_save, sender=CustomUser)
def send_user_creation_notification(sender, instance, created, **kwargs):
    """
    این تابع بعد از هر بار ذخیره شدن یک آبجکت CustomUser اجرا می‌شود.
    """
    if created:
        print(f"Signal received: New user '{instance.name}' created. Sending notification...")
        
        send_event(
            'admin-notifications',
            'message',
            {
                # تغییر ۳: از فیلد name (به جای username) استفاده کنید
                'text': f'کاربر جدیدی با نام «{instance.name}» و موبایل «{instance.mobile}» ساخته شد!'
            }
        )
"""
URL configuration for notification project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

# نکته: می‌توانیم با استفاده از login_required و user_passes_test این مسیر را امن‌تر کنیم تا فقط ادمین به آن دسترسی داشته باشد، اما فعلاً برای سادگی از آن صرف نظر می‌کنیم.
from django.contrib.auth.decorators import login_required
import django_eventstream


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.account.urls',namespace='account')),
    # این مسیر فقط برای ادمین است تا به رویدادها گوش دهد
    path('admin-events/', include(django_eventstream.urls), {
        'channels': ['admin-notifications'] # نام کانال اختصاصی ادمین
    }),
    
]







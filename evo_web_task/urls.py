"""evo_web_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from random_winners.views import call_three_random_names, add_person, index, delete_person

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='send_form'),
    url(r'^add_person/$', add_person, name='add_person'),
    url(r'^delete_person/$', delete_person, name='delete_person'),
    url(r'^random/$', call_three_random_names, name='random')
]

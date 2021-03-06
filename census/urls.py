"""census URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog
from .views import index

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('export/events/', views.export_events),
    path('submit/', views.SubmitEventView.as_view()),
    path('pending/', views.PendingList.as_view(), name = 'pending_list'),
    path('event/<int:pk>/update/', views.UpdateEvent.as_view(), name= 'event_update'),
    path('event/<int:pk>/delete/', views.DeleteEvent.as_view(), name= 'event_delete'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # this is to update list of events on the homepage based on datepicker selection
    url(r'^events/$', views.get_events, name='get_events'),
]
js_info_dict = {
    'packages': ('recurrence', ),
}
urlpatterns += [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['recurrence']),
         name='javascript-catalog')
]

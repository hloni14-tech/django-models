from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('detail', views.AboutView.as_view(),
         name='detail'),
]

from django.urls import path, include

urlpatterns = [
    # ...
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # ...
]

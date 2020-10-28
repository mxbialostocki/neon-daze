from django.urls import path

from . import views

app_name = 'stack'
urlpatterns = [
    # /stack/
    path('', views.index, name='index'),
    # /stack/1/
    path('<int:question_id>/', views.detail, name='detail'),
]
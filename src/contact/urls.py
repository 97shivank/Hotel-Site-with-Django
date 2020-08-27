from django.urls import path
from . import views


app_name='contacts'


urlpatterns=[
    path('',views.send_mail,name='send_mail'),
    path('success/',views.success , name='success'),

]
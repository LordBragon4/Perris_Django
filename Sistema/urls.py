from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^registro/$',views.registro,name="registro"),
    url(r'^lala/$',views.upload_image_view,name="lala")
]

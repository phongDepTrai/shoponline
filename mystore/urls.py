from django.contrib import admin
from django.urls import path
from mystore import views
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^tao-cookie$', views.tao_cookie, name='tao_cookie'),
    url(r'^doc-cookie$', views.doc_cookie, name='doc_cookie'),
    url(r'^xoa-cookie$', views.xoa_cookie, name='xoa_cookie'),
]
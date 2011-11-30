#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from shop_bulkorder.views import CartBulkView

urlpatterns = patterns('',
     url(r'^order-form/$', CartBulkView.as_view(), name='shop_order_form'),
     )

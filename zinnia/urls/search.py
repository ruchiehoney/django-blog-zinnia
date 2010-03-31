"""Urls for the zinnia search"""
from django.conf.urls.defaults import *

urlpatterns = patterns('zinnia.views',
                       url(r'^$', 'search_list', name='zinnia_entry_search'),
                       )

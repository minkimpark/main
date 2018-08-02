from django.urls import path
from django.conf.urls import url

from .djangoapps.testview import views as TestViews


urlpatterns = [
    url('testview$', TestViews.testview, name='testview'),
]

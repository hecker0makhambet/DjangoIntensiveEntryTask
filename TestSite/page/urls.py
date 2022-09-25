from django.urls import path
from django.views.generic import TemplateView
import os
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html",
                                  extra_context={"image": str(os.getcwd())})),
]
urlpatterns += staticfiles_urlpatterns()

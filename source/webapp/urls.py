from django.urls import path

from webapp.views.views import IndexView

urlpatterns = [
    path ('', IndexView.as_view(), name="poll")
]

from django.urls import path

from webapp.views.views import IndexView, DetailsView

urlpatterns = [
    path ('', IndexView.as_view(), name="poll"),
    path ('poll/<int:pk>/', DetailsView.as_view(), name="detail")
]

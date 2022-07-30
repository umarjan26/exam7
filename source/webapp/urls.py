from django.urls import path

from webapp.views.views import IndexView, DetailsView, UpdatesView

urlpatterns = [
    path ('', IndexView.as_view(), name="poll"),
    path ('poll/<int:pk>/', DetailsView.as_view(), name="detail"),
    path('poll/update/<int:pk>/', UpdatesView.as_view(), name='update')
]

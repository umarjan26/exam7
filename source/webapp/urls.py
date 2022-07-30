from django.urls import path

from webapp.views.views import IndexView, DetailsView, UpdatesView, DeletesView,CreatesView
from webapp.views.choice import ChoiceCreateView, ChoiceUpdateView
urlpatterns = [
    path ('', IndexView.as_view(), name="poll"),
    path ('poll/<int:pk>/', DetailsView.as_view(), name="detail"),
    path('poll/update/<int:pk>/', UpdatesView.as_view(), name='update'),
    path('poll/delete/<int:pk>/', DeletesView.as_view(), name='delete'),
    path('poll/create/', CreatesView.as_view(), name='creates'),
    path('choice/add/<int:pk>/', ChoiceCreateView.as_view(), name='choice_add'),
    path('choice/edit/<int:pk>/', ChoiceUpdateView.as_view(), name='choice_update')
]

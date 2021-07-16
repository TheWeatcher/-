from django.urls import path
from .views import TicketCreateView, TicketDetailView, TicketListView
from . import views
urlpatterns = [
    path('ticket/', TicketListView.as_view()),
    path('addticket/', TicketCreateView.as_view()),
    path('ticket/detail/<str:pk>/', TicketDetailView.as_view()),

]

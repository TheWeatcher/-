from rest_framework import generics
from .serializers import TicketSerializer
from .models import Ticket


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# permission_classes = [HasAPIKey]


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = [HasAPIKey]


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = [HasAPIKey]

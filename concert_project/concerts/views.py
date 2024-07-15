from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Concert, SeatingLayout, Reservation
from .serializers import ConcertSerializer, SeatingLayoutSerializer, ReservationSerializer

class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

class SeatingLayoutViewSet(viewsets.ModelViewSet):
    queryset = SeatingLayout.objects.all()
    serializer_class = SeatingLayoutSerializer

    def list(self, request, *args, **kwargs):
        # Optionally filter seating layouts to show only available seats
        queryset = self.get_queryset().filter(is_reserved=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            seating_layout = serializer.save()
            seating_layout.is_reserved = False  # Initialize as not reserved
            seating_layout.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        seating_layout_id = request.data.get('seating_layout')
        try:
            seating_layout = SeatingLayout.objects.get(id=seating_layout_id)
        except SeatingLayout.DoesNotExist:
            return Response({'error': 'Seating layout not found.'}, status=status.HTTP_404_NOT_FOUND)

        if seating_layout.is_reserved:
            return Response({'error': 'This seat is already reserved.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            seating_layout.is_reserved = True
            seating_layout.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

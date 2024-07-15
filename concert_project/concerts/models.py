from django.db import models

class Concert(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SeatingLayout(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='seating_layouts')
    section = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)
    is_reserved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('concert', 'section', 'seat_number')

    def __str__(self):
        return f"{self.section} - {self.seat_number}"

class Reservation(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='reservations')
    seating_layout = models.ForeignKey(SeatingLayout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        unique_together = ('concert', 'seating_layout')

    def __str__(self):
        return f"Reservation for {self.name} ({self.email})"

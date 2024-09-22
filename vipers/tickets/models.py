from django.db import models
from matches.models import Match
from tournaments.models import Tournament


TICKETCATEGORY_CHOICES = (
    ('VIP', 'VIP'),
    ('ORDINARY', 'ORDINARY'),
    ('STUDENT', 'STUDENT'),
    ('VVIP', 'VVIP'),
)

TICKET_HOLDER_ALLOCATION_CHOICES = (
    ('SEASONAL', 'SEASONAL'),
    ('SPONSORS', 'SPONSORS'),
    ('SPECIAL', 'SPECIAL'),
    ('PROMOTIONAL', 'PROMOTIONAL'),
    ('GENERAL', 'GENERAL'),
)
class Ticket(models.Model):
    """Model definition for Ticket."""
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=200, choices=TICKETCATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_holder_allocation = models.CharField(max_length=200, choices=TICKET_HOLDER_ALLOCATION_CHOICES)
    seat_number = models.IntegerField(blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True)
    availability_status = models.BooleanField(default=True)
    barcode = models.CharField(max_length=200, null=True, blank=True)
    date_issued = models.DateField(null=True, blank=True)
    date_sold = models.DateField(null=True, blank=True)
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)


    def __str__(self):
        """Unicode representation of Ticket."""
        return str(f"{self.match} - {self.ticket_type} - {self.price} - {self.ticket_holder_allocation}")




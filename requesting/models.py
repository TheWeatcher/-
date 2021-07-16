from django.db import models


class Ticket(models.Model):
    request_text = models.TextField()
    reg_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.request_text

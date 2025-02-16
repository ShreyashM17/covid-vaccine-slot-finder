from django.db import models


# Create your models here.
class Registrations(models.Model):
    AADHAR_CARD = 'AC'
    PAN_CARD = 'PC'
    doc_options = [
        (AADHAR_CARD, 'Aadhar card'),
        (PAN_CARD, 'Pan card')
    ]
    Uid = models.CharField(max_length=20)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Email_id = models.EmailField()
    Phone_number = models.IntegerField(blank=False)
    Date_of_birth = models.DateField(blank=False)
    Document = models.CharField(max_length=11, choices=doc_options, default=AADHAR_CARD)
    document_no = models.CharField(max_length=15, blank=True, null=True)
    Verified = models.BooleanField(default=False)
    Password = models.CharField(max_length=30, default=None, null=True)
    device1 = models.CharField(max_length=100, null=True, blank=True)
    device2 = models.CharField(max_length=100, null=True, blank=True)
    device3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Uid

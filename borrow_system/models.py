from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=True)
    condition = models.CharField(max_length=100, default='New')  # New field to track the condition
    location = models.CharField(max_length=255)  # Field for storing the location of the equipment
    type = models.CharField(max_length=100)  # Field for equipment type (e.g., Projector, Mouse)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    borrowed_by = models.CharField(max_length=255)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)  # New field for due date
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Fine if overdue
    staff_responsible = models.CharField(max_length=255)  # Staff member responsible for the transaction

    def __str__(self):
        return f"{self.equipment.name} borrowed by {self.borrowed_by}"


class OverdueRecord(models.Model):
    borrow_record = models.ForeignKey(BorrowRecord, on_delete=models.CASCADE)
    overdue_days = models.IntegerField()  # Number of days overdue
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2)  # Fine amount for the overdue item

    def __str__(self):
        return f"Overdue: {self.borrow_record.equipment.name} - {self.overdue_days} days late"


class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    object_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)


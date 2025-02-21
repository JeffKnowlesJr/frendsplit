from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='frendsplit_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')

    def __str__(self):
        return self.name

class Expense(models.Model):
    SPLIT_CHOICES = [
        ('EQUAL', 'Split Equally'),
        ('EXACT', 'Exact Amounts'),
        ('PERCENT', 'By Percentage'),
    ]

    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='expenses')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_paid')
    split_type = models.CharField(max_length=10, choices=SPLIT_CHOICES, default='EQUAL')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class ExpenseSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='splits')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_splits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} owes {self.amount} for {self.expense.description}"

class Settlement(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='settlements')
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='settlements_paid')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='settlements_received')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.payer.username} pays {self.receiver.username} {self.amount}"

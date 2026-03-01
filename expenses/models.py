from django.db import models


class Expense(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expense_date = models.DateField()

    category = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50)

    reference_no = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    store = models.ForeignKey(
        "stores.Store",   # change app name if different
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    def __str__(self):
        return self.title


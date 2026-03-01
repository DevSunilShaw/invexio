from django.db import models


class Inventory(models.Model):

    MOVEMENT_TYPE = (
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
        ("ADJUST", "Adjustment"),
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="inventory_logs"
    )

    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPE
    )

    quantity = models.IntegerField()

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="inventories"
    )

    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"
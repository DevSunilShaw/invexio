from django.db import models

class Order(models.Model):
	PLATFORM_CHOICES = (
		('amazon', 'Amazon'),
		('flipkart', 'Flipkart'),
		('meesho', 'Meesho'),
		('website', 'Website'),
	)
	STATUS_CHOICES = (
		('Pending', 'Pending'),
		('packed', 'Packed'),
		('shipped', 'Shipped'),
		('delivered', 'Delivered'),
		('cancelled', 'Cancelled'),
	)

	order_id = models.CharField(max_length=100)
	platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	product = models.ForeignKey(
		"products.Product", on_delete=models.CASCADE
	)
	quantity = models.IntegerField()
	selling_price = models.DecimalField(max_digits=10, decimal_places=2)

	customer_name = models.CharField(max_length=150)
	customer_phone = models.CharField(max_length=15)
	shipping_address = models.TextField()
	pincode = models.CharField(max_length=10)

	tracking_id = models.CharField(max_length=100, null=True, blank=True)
	courier_partner = models.CharField(max_length=100, null=True, blank=True)
	barcode = models.CharField(max_length=100, null=True, blank=True)

	packed_at = models.DateTimeField(null=True, blank=True)
	shipped_at = models.DateTimeField(null=True, blank=True)
	delivered_at = models.DateTimeField(null=True, blank=True)

	platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	packaging_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	total_amount = models.DecimalField(max_digits=10, decimal_places=2)
	profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	store = models.ForeignKey(
		"stores.Store", on_delete=models.CASCADE
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.order_id} - {self.platform}"

	def save(self, *args, **kwargs):
		total_cost = (
			self.platform_fee + self.shipping_charge + self.packaging_cost
		)

		self.profit = self.total_amount - total_cost

		super().save(*arg, **kwargs)


	@property
	def total_price(self):
		return self.quantity * self.selling_price

	# def reduce_stock(self):
	# 	from inventory .models import Inventory

		
	
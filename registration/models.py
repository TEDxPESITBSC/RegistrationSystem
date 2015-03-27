from django.db import models


class Attendee(models.Model):
	date_registered			= models.CharField(max_length=20)
	attendee_name 			= models.CharField(max_length=200)
	attendee_email			= models.EmailField()
	ticket_name				= models.CharField(max_length=100,blank=True)
	ticket_category			= models.CharField(max_length=100,blank=True)
	order_number			= models.CharField(max_length=100)
	ticket_number			= models.CharField(max_length=100)
	buyer_name				= models.CharField(max_length=200)
	buyer_email				= models.EmailField()
	mobile_number			= models.CharField(max_length=15)
	seat_number				= models.CharField(max_length=100)
	contact_number			= models.CharField(max_length=15)
	lunch_type				= models.CharField(max_length=100)
	comment					= models.CharField(max_length=200,blank=True)
	explara_barcode 		= models.CharField(max_length=100)
	pesit_barcode 			= models.CharField(max_length=100,blank=True)
	had_lunch 				= models.BooleanField(default=False)
	got_goodie_bag 			= models.BooleanField(default=False)

	def __str__(self):
		return self.attendee_name


from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=200)


class products(models.Model):
    name = models.CharField(max_length=200)
    company_brand_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    product_image = models.CharField(max_length=500)
    price = models.IntegerField()
    number_of_availability = models.IntegerField()
    seller_id = models.IntegerField()


class Slide(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class testimonial(models.Model):
    user_email = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    testimonial_description = models.CharField(max_length=500)
    user_profile_pic = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

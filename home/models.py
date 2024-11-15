from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_images = models.ImageField(blank=True, upload_to='home/%Y/%m/%d/')


    def __str__(self):
        return self.title



class Reviews(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_images = models.ImageField(blank=True, upload_to='home/%Y/%m/%d/')

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_images = models.ImageField(blank=True, upload_to='home/%Y/%m/%d/')


    def __str__(self):
        return self.name




class Usluga(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class UslugaPrice(models.Model):
    name_service = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    name = models.ForeignKey(Usluga, on_delete=models.CASCADE)



class Status(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=200)
    order_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.order_name


class Social(models.Model):
    social_facebook = models.CharField(max_length=200)
    social_instagram = models.CharField(max_length=200)
    social_twitter = models.CharField(max_length=200)







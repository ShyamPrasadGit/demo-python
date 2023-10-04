from django.db import models

class form_app(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    AGE = models.CharField(max_length=200)  # Assuming AGE is a character field, update to IntegerField if it's meant to be an integer
    GENDER = models.CharField(max_length=10)  # Assuming GENDER is a character field, adjust size accordingly
    PHONE_NUMBER = models.CharField(max_length=15)  # Assuming PHONE NUMBER is a character field
    MAIL_ID = models.EmailField()  # Assuming MAIL ID is an email field
    ADDRESS = models.TextField()  # Assuming ADDRESS is a longer text field
    # Add more fields as needed

    def __str__(self):
        return self.Name  # This is just for representation in the Django admin

    class Meta:
        verbose_name_plural = "form_app"  # This is the plural name used in Django admin



# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class DOB(models.Model):
    number=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AGE(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class GENDER(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PHONE_NUMBER(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class MAIL_ID(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class ADDRESS(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

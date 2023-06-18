from django.db import models

class Book(models.Model):
    Auth_first_name = models.CharField(max_length=30)
    Auth_email = models.EmailField()
    Title = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Publication_year = models.IntegerField(default=0)
    Issue_status = models.BooleanField(default=False)
    Issued_roll_no = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

from django.db import models
from ckeditor.fields import RichTextField


class LicenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class License(models.Model):
    name = RichTextField(blank=True)  # Change the CharField to RichTextField
    address = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=50, blank=True)
    weblink = models.URLField(blank=True)
    category = models.ForeignKey('LicenseCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
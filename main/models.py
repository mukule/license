from django.db import models

class LicenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class License(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=50, blank=True)
    weblink = models.URLField(blank=True)
    category = models.ForeignKey('LicenseCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

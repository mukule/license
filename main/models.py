from django.db import models

class LicenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class License(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50)
    weblink = models.URLField()
    category = models.ForeignKey('LicenseCategory', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

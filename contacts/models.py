from django.utils import timezone
from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     status = models.CharField(max_length=20, choices=[
#         ('todo', 'To Do'),
#         ('inprogress', 'In Progress'),
#         ('done', 'Done'),
#     ])
    
class Contact(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    end_date = models.DateField(default=timezone.now() + timezone.timedelta(days=10))
    # file = models.FileField(upload_to='deals/files', blank=True, null=True)
    # organization = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    # agent = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE, default=None, blank=True, null=True)
    # related_product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    
    def __str__(self):
        return self.Name
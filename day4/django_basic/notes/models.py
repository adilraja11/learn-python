from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

class Task(models.Model):
    task = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
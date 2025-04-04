from django.db import models

from core.models import BaseModel


# Create your models here.
class Department(BaseModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class DepartmentMember(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

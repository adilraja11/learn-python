from django.db import models

from .utils import generate_id


class BaseModel(models.Model):
    id = models.CharField(
        primary_key=True, max_length=100, default=generate_id, editable=False
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

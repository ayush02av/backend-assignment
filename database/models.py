from django.db import models
from django.utils import timezone
from uuid import uuid4
from . import utility

class record(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    _created = models.DateTimeField(default=timezone.now, editable=False)

    record_name = models.CharField(max_length=255, default="Sample Record")
    record_species = models.CharField(max_length=255)

    record_weight = models.FloatField(default=0.0)
    record_length = models.FloatField(default=0.0)
    record_latitude = models.FloatField(default=0.0)
    record_longitude = models.FloatField(default=0.0)
    
    record_photo = models.ImageField(upload_to=utility.record_image_path)

    def save(self, *args, **kwargs):
        super(record, self).save(*args, **kwargs)
        utility.resize_image(self.record_photo.path)
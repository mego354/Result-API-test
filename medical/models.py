from django.db import models
from datetime import datetime
from pytz import timezone
# megahd
# firstuser

class result(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)

    temp = models.CharField(max_length=64)
    press = models.CharField(max_length=64)
    h_rate = models.CharField(max_length=64)
    b_oxy = models.CharField(max_length=64)
    Sugar = models.CharField(max_length=64)
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now(timezone('Egypt'))
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Result number {self.id}"


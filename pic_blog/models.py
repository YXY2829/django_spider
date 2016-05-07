from django.db import models

# Create your models here.
class Picture(models.Model):
    name=models.CharField(max_length=50)
    index=models.URLField()
    class Meta:
        db_table='picture'
    def __unicode__(self):
        return self.name
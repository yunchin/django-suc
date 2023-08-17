from django.db import models

from django_suc import SmartUniqueConstraint


class MyModel(models.Model):
    field1 = models.IntegerField()
    field2 = models.IntegerField()

    class Meta:
        constraints = [
            SmartUniqueConstraint(fields=['field1', 'field2']),
            SmartUniqueConstraint(fields=['field1'], name='MY_UNIQ_NAME')
        ]

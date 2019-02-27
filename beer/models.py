# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import *
from django.db import models as models
from django_measurement.models import MeasurementField
from measurement.measures import Volume, Weight, Temperature

# Create your models here.
class Fermentable(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=250)
    color = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    extract = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    moisture = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    mash_required = models.BooleanField()
    quantity = MeasurementField(measurement=Weight, unit_choices=(("oz", "oz"), ("lb", "lb"), ("g", "g"), ("kg", "kg")), default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('inventory_fermentable_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('inventory_fermentable_update', args=(self.slug,))

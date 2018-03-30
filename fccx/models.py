# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
		houseid = models.BigIntegerField(primary_key=True)
		cellid = models.BigIntegerField()
		district_id = models.IntegerField()
		cell_name = models.CharField(max_length=200)
		title = models.CharField(max_length=200)
		unit_price = models.IntegerField()
		total_price = models.FloatField()
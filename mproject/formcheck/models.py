import imp
from random import choices
from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from django.db import models
from multiselectfield import MultiSelectField 

# Create your models here.


class Geek(models.Model):
    MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))
    geeks_field = MultiSelectField(max_length=200,choices=MY_CHOICES)
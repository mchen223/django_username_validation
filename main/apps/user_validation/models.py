# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Username(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -*- coding: utf-8 -*-
#Django提供的后台管理模板
from __future__ import unicode_literals

from django.contrib import admin
from murong import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.DeploySteps)
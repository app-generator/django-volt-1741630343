# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    pword = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Workout(models.Model):

    #__Workout_FIELDS__
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    exercisetype = models.TextField(max_length=255, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    tracking = models.BooleanField()

    #__Workout_FIELDS__END

    class Meta:
        verbose_name        = _("Workout")
        verbose_name_plural = _("Workout")


class Health(models.Model):

    #__Health_FIELDS__
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    stat_name = models.CharField(max_length=255, null=True, blank=True)
    stat_value = models.IntegerField(null=True, blank=True)
    tracking = models.BooleanField()

    #__Health_FIELDS__END

    class Meta:
        verbose_name        = _("Health")
        verbose_name_plural = _("Health")



#__MODELS__END

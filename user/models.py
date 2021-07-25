from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator



class Education(models.Model):
    course_name = models.CharField(max_length=20, blank=False, null=False)
    university = models.CharField(max_length=100, blank=False, null=False)
    passing_year = models.PositiveIntegerField(default=datetime.date.today().year, validators=[MinValueValidator(2015), MaxValueValidator(2027)])
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)

    def __str__(self):
        return self.university+'_'+str(self.passing_year)+'_'+self.course_name

class BasicDetails(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length = 30, blank=False, null=False)
    last_name = models.CharField(max_length = 30, blank=False, null=False)
    father_name = models.CharField(max_length = 50, blank=False, null=False)
    mother_name = models.CharField(max_length = 50, blank=False, null=False)
    date_of_birth = models.DateField(auto_now = False, auto_now_add = False, blank=False, null=False)
    gender = models.CharField(max_length = 1, choices=GENDER_CHOICES, blank=True)
    about = models.TextField(max_length = 500, blank=True)
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)
    education = models.ForeignKey(to='Education', related_name='students', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.first_name+"_"+self.last_name+'_'+str(self.created)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"

class teachers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads')
    about = models.CharField(max_length=100)
    class Meta:
        db_table = "teachers"

class team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads')
    facebook = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=1000)
    youtube = models.CharField(max_length=1000)
    class Meta:
        db_table = "team"


class course(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    url = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='uploads',null=True,blank=True)
    video_link = models.CharField(max_length=500,null=True,blank=True)
    teacher = models.ForeignKey('teachers',null=True,blank=True)
    categorie = models.ForeignKey('categories',null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    certification = models.TextField(null=True,blank=True)
    curricalum = models.TextField(null=True,blank=True)
    course_assign_time = models.CharField(max_length=100,null=True,blank=True)
    course_assign_description = models.TextField(null=True,blank=True)
    project_time = models.CharField(max_length=100,null=True,blank=True)
    project_description = models.TextField(null=True,blank=True)
    life_time_access = models.TextField(null=True,blank=True)
    support = models.TextField(null=True,blank=True)
    get_certified = models.TextField(null=True,blank=True)
    trending = models.CharField(max_length=10,null=True,blank=True)
    popular = models.CharField(max_length=10,null=True,blank=True)

    class Meta:
        db_table = "course"

class onlinecourse(models.Model):
    course_id = models.ForeignKey(course)
    date1 = models.CharField(max_length=100)
    month1 = models.CharField(max_length=100)
    day1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    date2 = models.CharField(max_length=100)
    month2 = models.CharField(max_length=100)
    day2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    date3 = models.CharField(max_length=100)
    month3 = models.CharField(max_length=100)
    day3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        db_table = "onlinecourse"

class promecode(models.Model):
    course_id = models.ForeignKey(course)
    promo = models.CharField(max_length=100)
    discount = models.IntegerField()
    class Meta:
        db_table = "promecode"

class reviews(models.Model):
    course_id = models.ForeignKey(course)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    discription = models.TextField(null=True,blank=True)
    class Meta:
        db_table = "reviews"

class faq(models.Model):
    qustion = models.CharField(max_length=1000)
    answer = models.TextField(null=True,blank=True)
    class Meta:
        db_table = "faq"

class pdf(models.Model):
    course_id = models.ForeignKey(course)
    course_pdf = models.FileField(upload_to='uploads',null=True,blank=True)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)
    video_link = models.CharField(max_length=1000)
    class Meta:
        db_table = "pdf"



class Blog(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    categories_id = models.ForeignKey(categories)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)
    discription = models.TextField(null=True,blank=True)
    keywords = models.CharField(max_length=500,null=True, blank=True)
    date = models.CharField(max_length=500,null=True, blank=True)
    class Meta:
        db_table = "Blog"




class carporate_traning(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    company = models.CharField(max_length=500,null=True,blank=True)
    primary_role = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    categorie = models.ForeignKey('categories',null=True,blank=True)
    course_id = models.ForeignKey('course',null=True,blank=True)
    mode = models.CharField(max_length=100,null=True, blank=True)
    message = models.TextField(null=True,blank=True)

    class Meta:
        db_table = "carporate_traning"

class free_esources(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "free_esources"

class contactus(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "contactus"

class REQUIREMENTS(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    hours = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "REQUIREMENTS"


class BECOME_Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "BECOME_Contact"


class subscribe(models.Model):
    email = models.CharField(max_length=100)
    suscribes = models.CharField(max_length=2)

    class Meta:
        db_table = "subscribe"



class payment(models.Model):
    user_id = models.ForeignKey(User,null=True,blank=True)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_id = models.ForeignKey(course,null=True,blank=True)
    class Meta:
        db_table = "payment"


class instamojo_payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    payment_request_id = models.CharField(max_length=100)
    class Meta:
        db_table = "instamojo_payment"



class instamojo_payment_done(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    payment_request_id = models.CharField(max_length=255,unique=True)
    status =  models.CharField(max_length=500)
    payment_id = models.CharField(max_length=255,unique=True)
    user_id = models.ForeignKey(User,null=True,blank=True)
    class Meta:
        db_table = "instamojo_payment_done"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class userDB_Manager(models.Manager):
    def check_create(self,data):
        errors = []
        if len(data['name']) < 3:
            errors.append(['name', "Name must be at least 3 characters long"])
        if len(data['username']) < 3:
            errors.append(['username', "Username must be at least 3 characters long"])
        if len(data['password']) < 8:
            errors.append(['password', "Password must be at least 8 characters long"])
        if not data['password'] == data['confirmpass']:
            errors.append(['confirmpass', "Passwords do not match"])
        if errors:
            return [False, errors]
        else:
            current_user = userDB.objects.filter(name=data['name'])
            if current_user:
                errors.append(['current_user', "Unable to register, please use alternate information"])
                return [False, errors]
            newUser = userDB(name=data['name'],username=data['username'])
            hashed_pass = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            print hashed_pass, "hashed password"
            newUser.hashpw = hashed_pass
            newUser.save()
            return [True, newUser]

    def check_log(self, data):
        errors = []
        current_user = userDB.objects.filter(name=data['name'])
        if not current_user:
            errors.append(['account', "Username or Password is incorrect"])
        elif not bcrypt.checkpw(data['password'].encode(), current_user[0].hashpw.encode()):
            errors.append(['account', "Username or Password is incorrect"])
        if errors:
            return [False, errors]
        else:
            return [True, current_user[0]]

class userDB(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    hashpass = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = userDB_Manager()
    def __str__(self):
        return 'ID: %s | Name: %s | Username: %s' %(self.id, self.name, self.username)

class plan_Manager(models.Manager):
    pass

class plan(models.Model):
    plan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(userDB, related_name="plan")

    objects = plan_Manager()

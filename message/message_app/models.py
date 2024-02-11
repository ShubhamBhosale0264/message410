from django.db import models

class Msg(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    mobile = models.CharField(max_length=15)
    mesg = models.TextField(default = "no message ") 


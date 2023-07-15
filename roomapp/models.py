from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Room(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=500,default="")
    slug=models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        # set the value of the read_only_field using the regular field
        self.slug = slugify(self.name)
        if self.description=="":
            self.description=f"Groupe de discussion {self.name}"
        super(Room, self).save( *args, **kwargs)
        # call the save() method of the parent


    def __str__(self):
        return f"Groupe de {self.name}"


# Table des messages
class Message(models.Model):
    room=models.ForeignKey(Room,related_name="messages",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="users",on_delete=models.CASCADE)
    content= models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('date_added',)
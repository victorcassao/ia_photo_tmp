from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    
    name = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return f"{self.name} - {self.instituicao}"

class Image(models.Model):
    
    filename = models.CharField(max_length=255)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    collection_id = models.IntegerField()
    isIndexed = models.BooleanField(default=False)
    imgHash = models.CharField(max_length=255)
    imgId = models.CharField(max_length=255)
    
class Face(models.Model):
    
    imgId = models.CharField(max_length=255)
    faceId = models.CharField(max_length=255)
    bboxWidth = models.FloatField()
    bboxHeight = models.FloatField()
    bboxLeft = models.FloatField()
    bboxTop = models.FloatField()
    eyeLeftX = models.FloatField()
    eyeLeftY = models.FloatField()
    eyeRightX = models.FloatField()
    eyeLeftY = models.FloatField()
    mouthLeftX = models.FloatField()
    mouthLeftY = models.FloatField()
    mouthRightX = models.FloatField()
    mouthRightY = models.FloatField()
    noseX = models.FloatField()
    noseY = models.FloatField()
    roll = models.FloatField()
    yaw = models.FloatField()
    pitch = models.FloatField()
    brightness = models.FloatField()
    sharpness = models.FloatField()
    confidence = models.FloatField()
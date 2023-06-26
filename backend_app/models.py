from django.db import models
from django.core.validators import MinValueValidator


class Document(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Annotation(models.Model):

    document = models.ForeignKey(Document , on_delete=models.CASCADE)
    start = models.IntegerField(validators=[MinValueValidator(0)])
    end = models.IntegerField(validators=[MinValueValidator(1)])
    label = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.label
    



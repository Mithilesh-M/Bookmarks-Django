from django.db import models
from taggit.managers import TaggableManager


class Event(models.Model):
    """Model representing a Event."""
    name = models.CharField(max_length=200, help_text='Enter a webpage name')
    url = models.CharField(max_length=200, help_text='Enter a webpage url')
    description = models.CharField(max_length=200, help_text='Enter a webpage description')
    tags = TaggableManager(help_text='Enter webpage tags')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

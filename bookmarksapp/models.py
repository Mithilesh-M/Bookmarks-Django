from django.db import models
from taggit.managers import TaggableManager


class Bookmarks(models.Model):
    """Model representing a Bookmarks."""
    name = models.CharField(max_length=200, help_text='Enter a webpage name')
    url = models.CharField(max_length=200, help_text='Enter a webpage url')
    description = models.CharField(max_length=200, help_text='Enter a webpage description')
    tags = TaggableManager(help_text='Enter webpage tags')
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Folder(models.Model):
    """Model representing a Folder"""
    name = models.CharField(max_length=200, help_text='Enter the folder name')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

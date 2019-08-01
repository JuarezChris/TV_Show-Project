from django.db import models
from time import gmtime, strftime

class Show_tv(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        shows_with_same_title = Shows.objects.filter(title=postData['title'])
        print('========')
        print(shows_with_same_title.all())

        # make a call for Show.objects.get(title = postData[title])
        # add keys and values to errors dictionary for each invalid field
        if len(shows_with_same_title.all()) > 0:
            errors['title'] = "Show already exists"
        if len(postData['title']) < 2:
            errors["title"] = "show name should be at least 5 characters"
        if len(postData['description']) > 0 and len(postData['description']) < 11:
            errors["description"] = "show description should be at least 10 characters"
        if postData['release_date'] < strftime("%y-%m-%d-%H-%M-%p", gmtime()):
            errors['release_date'] = "You must put in a valid date"
        print(errors)
        return errors


class Shows(models.Model):
    title= models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Show_tv() 


from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Cv(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Profile(Cv):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField(null=True)
    website = models.URLField(null=True)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class About(Cv):
    description = models.TextField()


class Career(Cv):
    description = models.TextField()


class Education(Cv):
    school = models.CharField(max_length=70)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField()


class Course(Cv):
    name = models.CharField(max_length=30)
    start = models.DateField()
    end = models.DateField()
    school = models.CharField(max_length=40)
    description = models.TextField()


class Experience(Cv):
    position = models.CharField(max_length=45)
    company = models.CharField(max_length=45)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField()


class Portfolio(Cv):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField()
    cover = models.FileField()


class Skill(Cv):
    name = models.CharField(max_length=30)
    description = models.TextField()
    level = models.PositiveIntegerField()


class Hobby(Cv):
    name = models.CharField(max_length=50)


class Language(Cv):
    name = models.CharField(max_length=30)
    level = models.TextField()


class Cocurricular(Cv):
    activity = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField()


class Reference(Cv):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=40)
    company = models.CharField(max_length=55)
    phone = models.CharField(max_length=20)
    email = models.EmailField()




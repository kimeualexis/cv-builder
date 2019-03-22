from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .models import Profile, About, Education, Career, Course, Experience, Portfolio, Skill, Hobby, Language, Cocurricular, Reference


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

"""
@receiver(post_save, sender=User)
def create_about(sender, instance, created, **kwargs):
    if created:
        About.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_about(sender, instance, **kwargs):
    try:
        instance.about.save()
    except ObjectDoesNotExist:
        About.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_education(sender, instance, created, **kwargs):
    if created:
        Education.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_education(sender, instance, **kwargs):
    try:
        instance.education.save()
    except ObjectDoesNotExist:
        Education.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_career(sender, instance, created, **kwargs):
    if created:
        Career.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_career(sender, instance, **kwargs):
    try:
        instance.career.save()
    except ObjectDoesNotExist:
        Career.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_course(sender, instance, created, **kwargs):
    if created:
        Course.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_course(sender, instance, **kwargs):
    try:
        instance.course.save()
    except ObjectDoesNotExist:
        Course.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_experience(sender, instance, created, **kwargs):
    if created:
        Experience.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_experience(sender, instance, **kwargs):
    try:
        instance.experience.save()
    except ObjectDoesNotExist:
        Experience.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_portfolio(sender, instance, **kwargs):
    try:
        instance.portfolio.save()
    except ObjectDoesNotExist:
        Portfolio.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_skill(sender, instance, created, **kwargs):
    if created:
        Skill.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_skill(sender, instance, **kwargs):
    try:
        instance.skill.save()
    except ObjectDoesNotExist:
        Skill.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_hobby(sender, instance, created, **kwargs):
    if created:
        Hobby.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_hobby(sender, instance, **kwargs):
    try:
        instance.hobby.save()
    except ObjectDoesNotExist:
        Hobby.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_language(sender, instance, created, **kwargs):
    if created:
        Language.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_language(sender, instance, **kwargs):
    try:
        instance.language.save()
    except ObjectDoesNotExist:
        Language.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_cocurricular(sender, instance, created, **kwargs):
    if created:
        Cocurricular.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_cocurricular(sender, instance, **kwargs):
    try:
        instance.cocurricular.save()
    except ObjectDoesNotExist:
        Cocurricular.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_reference(sender, instance, created, **kwargs):
    if created:
        Reference.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_course(sender, instance, **kwargs):
    try:
        instance.reference.save()
    except ObjectDoesNotExist:
        Reference.objects.create(user=instance)
        """

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from imagekit.models import ImageModel
import os

GENDER = (
    (u'Male', u'Male'),
    (u'Female', u'Female'),
)

def upload_to(instance, filename):
    name, dot, ext = filename.rpartition('.')
    name = "{0}.{1}".format(instance.user.username, ext)
    return os.path.join('profiles', name)

class UserProfile(ImageModel):
    user  = models.OneToOneField(User, verbose_name="User")
    bio   = models.TextField("About Me", blank=True, null=True)
    image = models.ImageField("Photo", upload_to=upload_to, storage=settings.UPLOAD_STORAGE, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=6, choices=GENDER)
    
    # better a foreign key to some predefined lists
    city = models.CharField("City", max_length=30, blank=True, null=True)    
    country = models.CharField("Country", max_length=30, blank=True, null=True)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    class IKOptions:
        spec_module = 'core.specs'
        image_field = 'image'    
        cache_dir   = 'cache'
    
    def __unicode__(self):
        return u"{0}'s profile".format(self.user.username)

    @property
    def fullname(self):
        return self.user.get_full_name()
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    @property
    def location(self):
        if self.city and self.country:
            return "{0}, {1}".format(self.city, self.country)
        else:
            return None

CONTACT_TYPE = (
    (u'Email Address',u'Email Address'),
    (u'Landline',u'Landline'),
    (u'Mobile Number',u'Mobile Number'),
    (u'Fax',u'Fax'),
)

class ContactInformation(models.Model):
    user = models.ForeignKey(User, verbose_name="User")
    name = models.CharField("Name", max_length=120)
    type = models.CharField("Type", max_length=50, choices=CONTACT_TYPE)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

from django.db import models
from django.utils import timezone
# Create your models here.
class About_pwares(models.Model):
      author = models.ForeignKey('auth.User')
      name = models.CharField(max_length=200, default="About Pwares")
      abouthistory = models.TextField()
      titlea = models.CharField(max_length=200)
      descriptiona = models.TextField()
      titleb = models.CharField(max_length=200)
      descriptionb = models.TextField()
      titlec = models.CharField(max_length=200)
      descriptionc = models.TextField()
      created_date = models.DateTimeField(
              default=timezone.now)
      published_date = models.DateTimeField(
              blank=True, null=True)

      def publish(self):
              self.published_date = timezone.now()
              self.save()

      def __str__(self):
               return self.name

class Pwares_ratings(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Ratings")
    creativedesign = models.CharField(max_length=200, default="1")
    happyclients = models.CharField(max_length=200, default="1")
    peopleloved = models.CharField(max_length=200, default="1")
    saveincome = models.CharField(max_length=200, default="1")
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Pwares_services(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Services")
    servicehistory = models.TextField()
    serviceone = models.CharField(max_length=200)
    serviceone_info = models.TextField()
    servicetwo = models.CharField(max_length=200)
    servicetwo_info = models.TextField()
    servicethree = models.CharField(max_length=200)
    servicethree_info = models.TextField()
    servicefour = models.CharField(max_length=200)
    servicefour_info = models.TextField()
    servicefive = models.CharField(max_length=200)
    servicefive_info = models.TextField()
    servicesix = models.CharField(max_length=200)
    servicesix_info = models.TextField()
    serviceseven = models.CharField(max_length=200)
    serviceseven_info = models.TextField()
    serviceeight = models.CharField(max_length=200)
    serviceeight_info = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Pwares_portfolio(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Portfolio")
    portfoliohistory = models.TextField()
    photo = models.FileField(upload_to='portfolio/')
    description = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Pwares_testimonials(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Testimonials")
    clientname = models.CharField(max_length=200)
    clienttitle = models.CharField(max_length=200)
    photo = models.FileField(upload_to='testimonials/')
    clienttext = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Pwares_updates(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Updates")
    about_updates = models.TextField()
    photo = models.FileField(upload_to='siteupdates/')
    update_title = models.CharField(max_length=200)
    update_source = models.CharField(max_length=200)
    update_info = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Pwares_contacts(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Pwares Contact Info")
    about_ourcontacts = models.TextField()
    email_address = models.CharField(max_length=200)
    phone_numbera = models.CharField(max_length=200)
    phone_numberb = models.CharField(max_length=200)
    linkedin_link = models.CharField(max_length=200)
    google_link = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    current_year = models.CharField(max_length=10, default="2018")
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

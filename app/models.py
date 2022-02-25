from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.contrib.auth.models import User


class IndividualProfile(models.Model):
    JOB_TYPE = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None) 
    name = models.CharField(max_length=500) 
    City = models.CharField(max_length=50) 
    Country = models.CharField(max_length=50) 
    Resume = models.FileField(upload_to=None, max_length=100) 
    Bio = models.TextField()
    Industry = models.CharField(max_length=50) 
    Work_Eligibility = models.BooleanField()
    Job_type = models.CharField(max_length=10, choices=JOB_TYPE)
    Work_experience = models.CharField(max_length=50)
    Unique_traits = models.TextField()
    Skills = models.CharField(max_length=500)
    Website = models.URLField(max_length=200)

    
    class Meta:
        verbose_name = ("IndividualProfile")
        verbose_name_plural = ("IndividualProfiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("IndividualProfile_detail", kwargs={"pk": self.pk})


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


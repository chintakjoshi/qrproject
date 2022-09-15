from django.db import models
import uuid
# Create your models here.


class LoginForm(models.Model):
    username = models.CharField(
        "Enter Your Full Name", max_length=20, default="")
    dob = models.CharField(max_length = 50)
    gender = models.CharField(max_length=1,
                              choices=(
                                  ('M', "Male"),
                                  ('F', "Female"),
                                  ('O', "Other"),
                              ), default="M",
                              )
    mobile = models.PositiveIntegerField(default='')
    email = models.EmailField(default="")
    password = models.CharField(default="", max_length=12)
    confirm_password = models.CharField(default="", max_length=12)
    hint = models.CharField(max_length = 50,blank = True,default = 'user')
    unique = models.UUIDField(default=uuid.uuid4, editable=True,blank = True)
    status = models.BooleanField(verbose_name="Access:",default = False)

    def __str__(self):
        return self.username


class VerifyDocument(models.Model):
    user_data = models.ForeignKey(LoginForm,on_delete=models.CASCADE, default="")
    doc_no = models.CharField(default="", max_length=12, unique=True)
    doc_name = models.CharField(max_length=20,
                                choices=(
                                    ("Adhaar Card", "Adhaar Card"),
                                    ("Driving License", "Driving License"),
                                    ("PAN Card", "PAN Card"),
                                    ("Vehicle RC", "Vehicle RC"),
                                ), default="Adhaar Card",
                                )
    doc_upload_front = models.ImageField(upload_to="media/", blank=True)
    doc_upload_back = models.ImageField(upload_to="media/", blank=True)
    qrcode = models.ImageField(upload_to = 'media/',blank = True, default="")


    def __str__(self):
        return self.doc_no + " | " + self.doc_name 

class feedback(models.Model):
    name = models.CharField(
        "Enter Your Full Name", max_length=20, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.email + " | " + self.message

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
import  uuid
class myUserManager(BaseUserManager):
    def create_user(self,email,name,mobile,refer_code,password=None):
        if not email:
            raise ValueError("Email is required")
        if not name:
            raise ValueError("Name is required")
        if not mobile:
            raise ValueError("Mobile is required")


        user=self.model(
            email=self.normalize_email(email),
            name=name,
            mobile=mobile,
            refer_code=refer_code
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,email,mobile,refer_code,password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            mobile=mobile,
            refer_code=refer_code,
            password=password

        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100,unique=True)
    mobile = models.CharField(max_length=10,unique=True)
    refer_code= models.CharField(max_length=10,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['name','email','refer_code']


    objects=myUserManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True




class Wallet(models.Model):
    wal_bal = models.IntegerField(default=0)
    win_bal = models.IntegerField(default=0)
    user = models.OneToOneField(User,related_name='wallet',null=True,on_delete=models.CASCADE)

class WithdrawModel(models.Model):
    wth_amount=models.IntegerField()
    wth_date=models.DateTimeField(auto_now_add=True)
    wth_method=models.CharField(max_length=200)
    wth_status=models.BooleanField(default=False)
    user = models.ForeignKey(User,related_name='withdraw',null=True,on_delete=models.CASCADE)
    

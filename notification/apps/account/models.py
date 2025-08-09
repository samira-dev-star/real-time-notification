from django.db import models
from django.utils import timezone

# Create your models here.


from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class Customusermanager(BaseUserManager):
    def create_user(self,mobile,name="",password=None):
        if not mobile:
            raise ValueError('please enter your mobile number!')
        user = self.model(
            mobile = mobile,
            name = name
        )
        
        user.set_password(password)
        
        user.save(using = self._db)
        return user
    
    def create_superuser(self,mobile,name,password):
        user = self.create_user(
            mobile=mobile,
            name=name,
            password=password,
            )
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser,PermissionsMixin):
    mobile = models.CharField(max_length=11,unique=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    registered_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = ['name']
    
    
    
    @property
    def is_staff(self):
        return self.is_admin
    
    
    objects = Customusermanager()
    
        
    def __str__(self):
        return self.name
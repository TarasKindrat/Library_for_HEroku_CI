from django.contrib import admin
#from abstract_base_user_samle import CustomUser
from authentication.models import CustomUser
# Register your models here.

admin.site.register(CustomUser)
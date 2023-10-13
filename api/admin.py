from django.contrib import admin

from api.models import Post
from api.models import User
from api.models import Salon

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Salon)


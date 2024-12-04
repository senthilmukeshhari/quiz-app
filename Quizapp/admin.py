from django.contrib import admin
from .models import *

admin.site.register(NewUser)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(UserResponse)
admin.site.register(UserResult)
admin.site.register(Feedback)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

class FeedbackAdmin(admin.ModelAdmin):
	list_display = [ 'user', 'feedback' ]

class UserResponseAdmin(admin.ModelAdmin):
	list_display = [ 'user', 'question', 'selected_option' ]

class UserResultAdmin(admin.ModelAdmin):
	list_display = [ 'user', 'category', 'score' ]

admin.site.register(NewUser)
admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(Question, ImportExportModelAdmin)
admin.site.register(UserResponse, UserResponseAdmin)
admin.site.register(UserResult, UserResultAdmin)
admin.site.register(Feedback, FeedbackAdmin)

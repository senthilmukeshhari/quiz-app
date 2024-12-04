from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'), 
    path('categories', views.catagory_page, name='categories'),
    path('question_collections/<int:category_id>', views.question_collections, name='question_collections'),
    path('questions/<int:category_id>', views.questions, name='questions'),
    path('result/<int:category_id>',views.result,name='result'),
    path('add-feedback', views.AddFeedback, name='add-feedback'),
    path('feedback_result',views.FeedbackResult,name="fbr")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
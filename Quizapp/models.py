from django.db import models

class NewUser(models.Model):
    user_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="caategory/related_images/",null=True, blank=True)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField(max_length=500,null=True)
    opt1 = models.CharField(max_length=80,null=True)
    opt2 = models.CharField(max_length=80,null=True)
    opt3 = models.CharField(max_length=80,null=True)
    opt4 = models.CharField(max_length=80,null=True)
    correct_opt = models.CharField(max_length=80,null=True)

    def __str__(self):
        return self.question
 
class UserResponse(models.Model):
    user = models.ForeignKey(NewUser, models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
# User Results
class UserResult(models.Model):
    user = models.ForeignKey(NewUser, models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_paper_no = models.IntegerField()
    score = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
# User Feeddback
class Feedback(models.Model):
    user = models.ForeignKey(NewUser, models.CASCADE)
    feedback = models.CharField(max_length=50,null=True)
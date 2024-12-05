from django.shortcuts import render,redirect
from .models import *
import random as r
from json import dumps
from django.http import JsonResponse
from django.core.paginator import Paginator

def home(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user = NewUser(user_name=user_name)
        user.save()
        current_user = NewUser.objects.last().pk
        request.session['uid'] = current_user
        return redirect('categories')
    return render(request,'home.html')

def catagory_page(request):
    context= {}
    categories = Category.objects.all()
    context['categories'] = categories
    return render(request, 'category.html', context=context)


def question_collections(request, category_id=None):
    context = {}
    if category_id:
        questions = Question.objects.filter(category=category_id)
        paginator = Paginator(questions, 10)

        context['category'] = category_id
        context['paginator'] = paginator
        return render(request, 'question_collections.html', context=context)
    else: 
        return redirect('categories')

# Question Page
def questions(request, category_id=None):
    context = {}
    current_userid = request.session.get('uid')

    # Checking for currend user
    if current_userid:
        current_user_name = NewUser.objects.get(pk=current_userid).user_name      
        questions = Question.objects.filter(category=category_id)
        paginator = Paginator(questions, 10)
        page_number = request.GET.get("page")
        if not page_number:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        
        # Save user result
        if request.method == 'POST':
            score = 0
            userid = request.session.get('uid')
            user = NewUser.objects.get(id=userid)
            category = Category.objects.get(id=category_id)

            for key, value in request.POST.items():

                if(key.startswith('question-')) and value:
                    question_id = key.split('-')[1]

                    question = Question.objects.get(id=question_id)
                    correct_opt = question.correct_opt.strip()
                    user_response, created = UserResponse.objects.get_or_create(user=user, question=question)
                    user_response.selected_option = value.strip()
                    user_response.save()
                    if value.strip() == correct_opt.strip():
                        print('1')
                        score += 1
                    print('score : ', score, value.strip() == correct_opt.strip(), value)

            user_result, created = UserResult.objects.get_or_create(user=user, category=category, question_paper_no=page_number)
            user_result.score = score
            user_result.save()

            return redirect('result', category_id=category.id)

        context['user'] = current_user_name
        context['questions'] = page_obj

        return render(request,'questions.html',context=context)

    else:
        return redirect('home')

def result(request, category_id=None):
    context = {}
    current_userid = request.session.get('uid')

    # Checking for currend user
    if current_userid:
        user = NewUser.objects.get(id=current_userid)
        user_result = UserResult.objects.get(user=user)

        if not user_result:
            return redirect('categories')

        questions = Question.objects.filter(category=category_id)
        paginator = Paginator(questions, 10)
        page_number = user_result.question_paper_no
        page_obj = paginator.get_page(page_number)

        user_responses = UserResponse.objects.filter(user=user, question__in=questions).select_related('question')
        user_response_dict = {response.question.id : response for response in user_responses}

        context['user_result'] = user_result
        context['user_responses'] = user_responses
        context['user_response_dict'] = user_response_dict
        context['user'] = current_userid
        context['questions'] = page_obj
        return render(request,'result.html',context=context)
    else:
        return redirect('home')

def AddFeedback(request):
    current_userid = request.session.get('uid')

    if request.method == 'POST':
        if current_userid:
            user = NewUser.objects.get(id=current_userid)
            feedback = request.POST.get('feedback')
            feedback = Feedback(user=user, feedback=feedback)
            feedback.save()
    return redirect('categories')

def FeedbackResult(request):
    data = Feedback.objects.all()
    context = {
        'data' : data
    }
    return render(request,'feedback_result.html',context=context)
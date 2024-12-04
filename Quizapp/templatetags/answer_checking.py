from django import template
from Quizapp.models import *

register = template.Library()

@register.simple_tag
def get_style(user_response_dict, question, option):
	print('Question : ', question)
	print('user', user_response_dict)
	print('option :', option)
	user_responses = user_response_dict.get(question.id)
	print('user_responses ', user_responses)
	if user_responses:
		if option == question.correct_opt:
			return 'is-valid'
		elif user_responses.selected_option == option:
			return 'is-invalid'
	return ''

@register.simple_tag
def option(user_response_dict, question, option):
	user_responses = user_response_dict.get(question.id)
	if user_responses:
		if option == user_responses.selected_option:
			return 'checked'
	return ''
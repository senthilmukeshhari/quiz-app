from django import template
from Quizapp.models import *

register = template.Library()

@register.simple_tag
def get_style(user_response_dict, question, option):
	user_responses = user_response_dict.get(question.id)
	if user_responses:
		if option.strip() == question.correct_opt.strip():
			return 'is-valid'
		elif user_responses.selected_option.strip() == option.strip():
			return 'is-invalid'
	return ''

@register.simple_tag
def option(user_response_dict, question, option):
	user_responses = user_response_dict.get(question.id)
	print(user_responses)
	if user_responses:
		if user_responses.selected_option.strip() == option.strip():
			print('hii')
			return 'checked'
	return ''
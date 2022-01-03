from django import template

register = template.Library()

@register.filter(name='placeholder')
def add_placeholder(field, text):
	return field.as_widget(attrs={'placeholder': text})
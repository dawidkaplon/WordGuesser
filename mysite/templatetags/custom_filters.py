from django import template

register = template.Library()

@register.filter
def get_bg_color(keyboard_bg_colors, key):
    return keyboard_bg_colors.get(key, '')

@register.filter
def get_text_color(keyboard_text_colors, key):
    return keyboard_text_colors.get(key, '')
from functools import reduce
from django import template


register = template.Library()


@register.filter(name='UPPER')
def to_upper(inp_string):
    return inp_string.upper()

@register.simple_tag(name='doing_arithmetic')
def add(*args):
    return reduce(lambda x, y: x + y, args)

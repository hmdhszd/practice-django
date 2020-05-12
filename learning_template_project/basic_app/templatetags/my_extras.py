from django import template

@register.filter(name='cut')

def cut(value,arg):
    return value.raplace(arg,'')



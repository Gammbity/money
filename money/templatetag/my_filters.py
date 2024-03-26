from django import template
register = template.Library()


@register.filter
def number(value):
    ans = ''
    v = value[::-1]
    s = 0
    for i in v:
        s += 1
        if s % 3 == 0:
            ans += f",{i}"
        else:
            ans += i            
    return f"{ans[3:][::-1]} so'm"        

               



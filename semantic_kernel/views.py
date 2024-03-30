
# Django
from django.shortcuts import render
from django.utils.safestring import mark_safe



def foo(request):
    html_string = "<h1>Hello, World!</h1>"
    html_content = mark_safe(html_string)
    return render(request, "template.html", {"html_content": html_content})


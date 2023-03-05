# from django.shortcuts import render
# from django.http import HttpResponse
# test


# def coffee(request):
#     return HttpResponse("Hello world!")

from django.http import HttpResponse
from django.template import loader


def coffee(request):
    template = loader.get_template('sample.html')
    return HttpResponse(template.render())

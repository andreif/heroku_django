from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response, HttpResponse, redirect


@cache_page(60 * 5)
def view_index(request):
    return render_to_response('index.html')

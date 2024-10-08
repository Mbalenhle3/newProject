# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET



def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'index.html')

@require_GET
def favicon_view(request):
    return HttpResponse(status=204)  # No Content


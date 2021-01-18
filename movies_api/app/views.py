from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie 


@csrf_exempt
def movies(request):
    if request.method == 'POST':
        name = request.POST["name"]
        year = request.POST["year"]

        Movie.objects.create(name=name, year=year)

        return HttpResponse("created")

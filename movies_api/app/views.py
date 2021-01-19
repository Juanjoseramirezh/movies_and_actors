from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie 
from django.http import JsonResponse


@csrf_exempt
def movies(request):
    if request.method == 'GET':
        data = []

        movies = Movie.objects.all()
        for movie in list(movies):
            movie_data = {
                "name": movie.name,
                "year": movie.year
            }
            data.append(movie_data)

        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        name = request.POST["name"]
        year = request.POST["year"]

        Movie.objects.create(name=name, year=year)

        return HttpResponse("created")

    return HttpResponse('Method Not Allowed')
# from django.shortcuts import render
# from django.http import JsonResponse
# from . models import *


# def movie_list(request):
#     movies=Movie.objects.all()
#     data={'movies':list(movies.values())}
#     return JsonResponse(data,safe=False)


# def movie(request,pk):
#     movie=Movie.objects.get(id=pk)
#     print(type(movie))
#     data={
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active
#     }
#     return JsonResponse(data,safe=False)


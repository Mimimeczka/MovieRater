from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def test_response(request):
    filmy = Movie.objects.all()
    return render(request, 'lista_filmow.html', {'filmy': filmy})


@login_required
def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(test_response)

    return render(request, 'nowy_film.html', {'form': form})


@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(test_response)

    return render(request, 'nowy_film.html', {'form': form})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(test_response)

    return render(request, 'potwierdz.html', {'film': film})

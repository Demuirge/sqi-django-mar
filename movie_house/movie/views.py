from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Movie
from .forms import MovieForm

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, "movie/home.html", {"movies": movies})

def movies(request):
    movies = Movie.objects.all()
    return render(request, "movie/movies.html", {"movies": movies})

def movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "movie/movie.html", {"movie": movie})

@login_required
def add_movie(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            messages.success(request, "Movie added successfully")
            return redirect("movie:movies")
    
    context = {
        "form": form
    }
    return render(request, "movie/add-movie.html", context)

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.user != movie.added_by:
        messages.error(request, "You do not have permission to edit that movie")
        return redirect("movie:movies")

    form = MovieForm(instance=movie)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie edited successfully")
            return redirect("movie:movie", movie_id)
    
    context = {
        "movie": movie,
        "form": form
    }
        
    return render(request, "movie/edit-movie.html", context)

@login_required
def confirm_delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.user != movie.added_by:
        messages.error(request, "You do not have permission to delete that movie")
        return redirect("movie:movies")
    
    return render(request, "movie/confirm-delete-movie.html", {"movie": movie})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.user != movie.added_by:
        messages.error(request, "You do not have permission to delete that movie")
        return redirect("movie:movies")

    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted successfully")
        return redirect("movie:movies")
    
    return render(request, "movie/movies.html", {"movie": movie})
        





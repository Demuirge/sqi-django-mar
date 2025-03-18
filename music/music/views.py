from django.shortcuts import render, get_object_or_404

from .models import Artist, Album

# Create your views here.

# the_beatles = Artist.objects.create(name="The Beatles", debut=1960)
# drake = Artist.objects.create(name="Drake", debut=2009)
# taylor = Artist.objects.create(name="Taylor Swift", debut=2006)
# adele = Artist.objects.create(name="Adele", debut=2008)
# coldplay = Artist.objects.create(name="Coldplay", debut=1996)



def home(request):
    return render(request, "music/home.html")

def artist(request):
    artist_listing = Artist.objects.order_by("debut")
    return render(request, "music/artist.html", {"artist_listing" : artist_listing})

def album(request):
    album_listing = Album.objects.order_by("release_date")
    return render(request, "music/album.html", {"album_listing" : album_listing})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    albums = Album.objects.filter(artist = artist)
    return render(request, "music/artist_detail.html", {"artist": artist, "albums": albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, "music/album_detail.html", {"album": album})

from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
# Add Album Functions:
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : album_form})

# Edit Album Functions:
def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    # print(post.title)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'add_album.html', {'form' : album_form})

# Delete Album Functions:
def delete_album(request, id):
    album = models.Album.objects.get(pk=id) 
    album.delete()
    return redirect('homepage')
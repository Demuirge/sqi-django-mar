from django.shortcuts import render, redirect, get_object_or_404

from .models import Note
from .forms import NoteForm

# Create your views here.

def home(request):
    return render(request, "note_taking/home.html")

def notes(request):
    notes = Note.objects.all()
    return render(request, "note_taking/notes.html", {"notes": notes})

def search_note(request):
    query = request.GET.get("search")

    if query:
        notes = Note.objects.filter(title__icontains=query)
    
    context = {
        "query": query,
        "notes": notes
    }
    return render(request, "note_taking/search-note.html", context)

def note_category(request):
    category =Note.category
    notes = Note.objects.filter(category=category)

    context = {
        "category": category,
        "notes": notes
    }
    return render(request, "note_taking/note-category.html", context)

def create_note(request):
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_taking:notes")
    
    context = {
        "form": form
    }
    return render(request, "note_taking/create-note.html", context)

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = NoteForm(instance=note)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_taking:notes")
    
    context = {
        "note": note,
        "form": form
    }
    return render(request, "note_taking/edit-note.html", context)

def confirm_delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "note_taking/confirm-delete-note.html", {"note": note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
            note.delete()
            return redirect("note_taking:notes")
    
    context = {
        "note": note,
    }
    return render(request, "note_taking/notes.html", context)


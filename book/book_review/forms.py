from django import forms

from .models import Review, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","author","publication_date","book_image",]
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["book","reviewer_name","rating","comment"]

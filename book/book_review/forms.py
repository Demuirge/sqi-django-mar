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


class ReviewManualForm(forms.Form):
    reviewer_name = forms.CharField(max_length=255, widget=forms.TextInput())
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 1, "max":5}))
    comment = forms.CharField(widget=forms.Textarea())

class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating","comment"]

class ReviewManualUpdateForm(forms.Form):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 1, "max":5}))
    comment = forms.CharField(widget=forms.Textarea())


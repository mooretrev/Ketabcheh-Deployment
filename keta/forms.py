from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class SearchForm(forms.Form):
    ADVANCE_SEARCH_CHOICES = [
        ('isbn', 'ISBN(10 or 13)'),
        ('title', 'Title'),
        ('author', 'Author'),
        ('keywords', 'Keywords'),
    ]
    search_text = forms.CharField(label="Search", max_length=100)
    advance_search = forms.MultipleChoiceField(label="Advance Search", initial=['ISBN'], widget=forms.RadioSelect,  choices=ADVANCE_SEARCH_CHOICES)


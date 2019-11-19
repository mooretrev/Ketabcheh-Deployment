from django import forms

class SearchForm(forms.Form):
    ADVANCE_SEARCH_CHOICES = [
        ('isbn', 'ISBN(10 or 13)'),
        ('title', 'Title'),
        ('author', 'Author'),
    ]
    search_text = forms.CharField(label="Search", max_length=100, widget=forms.TextInput(attrs={'class':'cta-searchbar', 'type':'search', 'id':'site-search', 'name':'search-box'}))
    advance_search = forms.MultipleChoiceField(label="Advance Search by:", initial=['ISBN'], widget=forms.RadioSelect(),  choices=ADVANCE_SEARCH_CHOICES)


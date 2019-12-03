from django import forms

class SearchForm(forms.Form):
    ADVANCE_SEARCH_CHOICES = [
        ('title', 'Title'),
        ('isbn', 'ISBN(10 or 13)'),
    ]
    search_text = forms.CharField(label="Search", max_length=100, widget=forms.TextInput(attrs={'class':'cta-searchbar', 'type':'search', 'id':'site-search', 'name':'search-box'}))
    advance_search = forms.ChoiceField(label="Advance Search by:", initial=['title'], widget=forms.RadioSelect, choices=ADVANCE_SEARCH_CHOICES)


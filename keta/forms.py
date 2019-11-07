from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class SearchForm(forms.Form):
    search_text = forms.CharField(label="Search", max_length=100)
    advance_serach = forms.MultipleChoiceField(label="Advance Search", )

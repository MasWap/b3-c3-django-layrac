from django import forms

class VoteForm(forms.Form):
    vote = forms.IntegerField(label='Vote', min_value=0, max_value=5)
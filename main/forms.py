from django import forms

class StudentInputForm(forms.Form):
    unique_id = forms.IntegerField(help_text = "")
    name = forms.CharField(max_length = 20)
    clas = forms.CharField(max_length = 6)
    rollno = forms.IntegerField(help_text = "")
    g1 = forms.IntegerField(help_text = "")
    g2 = forms.IntegerField(help_text = "")
    g3 = forms.IntegerField(help_text = "")
from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description", required=False)
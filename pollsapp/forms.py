from django import forms 

class Create(forms.Form):
    QUESTION=forms.CharField()
    OPTION1=forms.CharField()
    OPTION2=forms.CharField()
    OPTION3=forms.CharField()
    OPTION4=forms.CharField()
    
    
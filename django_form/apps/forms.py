import django.forms as forms
class contactForm(forms.Form):
    name = forms.CharField(label="User Name: "we, help_text="Enter your name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField(label="User Age")
    weights = forms.FloatField(label="User Weight")
    balance = forms.DecimalField(label="Balance")
    choose = forms.ChoiceField(choices = [("sm","small"),("medium","medium"),("lg","large")])
    multichoose = forms.MultipleChoiceField(choices = [("sm","small"),("medium","medium"),("lg","large")])
    file = forms.FileField()
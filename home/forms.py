from django import forms
from . models import Product, UserProfile



class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class':'form-control p-3'}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':'form-control p-3'}))



class EditProductForm(forms.ModelForm):
        
        class Meta:
            model = Product
            fields = ['category','name','type','amount','summa', 'dollor']
       

            widgets = {
            'category': forms.Select(attrs={'class':'form-control '}),
            'name': forms.TextInput(attrs={'class':'form-control '}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'summa': forms.NumberInput(attrs={'class':'form-control'}),
            'dollor': forms.NumberInput(attrs={'class':'form-control'}),
            
            }

class createForm(forms.ModelForm):
     

     class Meta:
        model = Product
        fields = ['category','name','type','amount','summa', 'dollor']

        widgets = {
            'category': forms.Select(attrs={'class':'form-control '}),
            'name': forms.TextInput(attrs={'class':'form-control '}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'summa': forms.NumberInput(attrs={'class':'form-control'}),
            'dollor': forms.NumberInput(attrs={'class':'form-control'}),
            
            }
class CreateUserProfil(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control p-3 '}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':'form-control p-3'}))

    class Meta:
         model = UserProfile
         fields = ['role', 'rating']

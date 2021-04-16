from django import forms
from .models import Model_type, Car_type, Make, Category, Subcategory, Product, Order, Customer
from django.contrib.auth.models import User



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
        "mobile", "email", "payment_method"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", min_length=9, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    job = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Job'}), required=False)
    address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Phone'}), required=False)
    mobile = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Mobile'}), required=False)
    vat = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'VAT'}), required=False)
    class Meta:
        model = Customer
        fields = ["username", "password", "email","full_name", "address", "job", "phone", "mobile", "vat",]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Customer with this E-mail already exists.")

        return email


class CustomerLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ContactForm(forms.Form):
    name= forms.CharField(max_length=80, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email= forms.CharField(max_length=80, label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    comment= forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))



class MakeForm(forms.Form):
    make = forms.ModelChoiceField(queryset=Make.objects.none(), required=False)
    model_type = forms.ModelChoiceField(queryset=Model_type.objects.none(), required=False)
    car_type = forms.ModelChoiceField(queryset=Car_type.objects.none(), required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.none(), required=False)
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.none(), required=False
    )
    class Meta:
        fields = ('make', 'model_type', 'car_type', 'category', 'subcategory',)
    def __init__(self, make=None, model_type=None, car_type=None, category=None, subcategory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['make'].queryset = Make.objects.all()
        if make:
            self.fields['model_type'].queryset = Model_type.objects.filter(make=make)
        if model_type:
            self.fields['car_type'].queryset = Car_type.objects.filter(model_type=model_type)
        if car_type:
            self.fields['category'].queryset = Category.objects.filter(car_type=car_type)
        if category:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=category)


class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used in customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account does not exists..")
        return e


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Enter New Password',
    }), label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Confirm New Password',
    }), label="Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New Passwords did not match!")
        return confirm_new_password


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.validators import RegexValidator

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=70,
        required=True,
        widget=forms.EmailInput(attrs={"class": "input-register form-control", "placeholder": "Email"}),
    )
    first_name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={"class": "input-register form-control", "placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={"class": "input-register form-control", "placeholder": "Last Name"}),
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "input-register form-control", "placeholder": "Password"}),
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "input-register form-control", "placeholder": "Confirm Password"}),
    )
    marketing_consent_one = forms.BooleanField(
        required=False,
        label="I agree to receive marketing emails.",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    marketing_consent_two = forms.BooleanField(
        required=False,
        label="I agree to receive marketing emails.",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "marketing_consent_one",
            "marketing_consent_two",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = None
        user.marketing_consent_one = self.cleaned_data.get("marketing_consent_one")
        user.marketing_consent_two = self.cleaned_data.get("marketing_consent_two")
        if commit:
            user.save()
        return user


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email",
        max_length=70,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "input-register form-control", "placeholder": "Email", "autofocus": True}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "input-register form-control", "placeholder": "Password"}),
    )

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages["inactive"], code="inactive")
        return self.cleaned_data


class CustomUserUpdateForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=False,
        validators=[RegexValidator(r"^\d{10,15}$", message="Phone number must be between 10 and 15 digits.")],
        widget=forms.TextInput(attrs={"class": "input-register form-control", "placeholder": "Phone Number"}),
    )
    first_name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={"class": "input-register form-control", "placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={"class": "input-register form-control", "placeholder": "Last Name"}),
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "input-register form-control", "placeholder": "Email"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "marketing_consent_one",
            "marketing_consent_two",
            "address_one",
            "address_two",
            "city",
            "country",
            "province",
            "postal_code",
        ]
        widgets = {
            "marketing_consent_one": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "marketing_consent_two": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

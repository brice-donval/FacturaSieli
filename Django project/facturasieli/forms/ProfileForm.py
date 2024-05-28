from django import forms
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Profile, Role, Company

class ProfileForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)
    role = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True)

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'role', 'company')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        profile = Profile.objects.create_user(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password1'],
            company=self.cleaned_data['company']
        )
        
        profile.save()
        #self.save_m2m()  # Save the many-to-many data for roles
        return profile

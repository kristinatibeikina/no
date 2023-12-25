from django import forms

from .models import AbUser



class RegistrateForm(forms.ModelForm):
    class Meta:
        model = AbUser
        fields = ('username', 'password')

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



















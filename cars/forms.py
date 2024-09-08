from django import forms

from cars.models import Car, Brand


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 20000:
            self.add_error('value', 'O valor deve ser maior ou igual que 20000')
        return value
    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano deve ser maior ou igual que 1975')
        return factory_year
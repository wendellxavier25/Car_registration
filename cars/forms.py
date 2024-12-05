from django import forms
from .models import Car



class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'  


    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value is not None and value < 4000:
            self.add_error('value', 'minimum value is R$4.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1908:
            self.add_error('factory_year', 'he had no car before 1908')
        return factory_year
    
   
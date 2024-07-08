from django import forms
from django.core.exceptions import ValidationError

from .models import ApplicationData


class UploadFileForm(forms.ModelForm):

    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.xlsx'):
            raise ValidationError("Неподдерживаемый тип файла. Пожалуйста, загрузите файл в формате .xlsx")
        return file

    class Meta:
        model = ApplicationData
        fields = ['file']

from django.forms import ModelForm, DateInput
from .models import UseLog

class UseLogForm(ModelForm):
    class Meta:
        model = UseLog
        fields = ['date', 'context']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': "Select A Date",
                    'type': 'date'
                }
            )
        }
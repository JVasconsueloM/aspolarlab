from django import forms

from apps.examen.models import Examen


class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExamenForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

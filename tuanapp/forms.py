from django.forms import ModelForm

from tuanapp.models import Tuan


class TuanForm(ModelForm):
    class Meta:
        model = Tuan
        fields = ['rest_name', 'min_num', 'max_num', 'start_time']

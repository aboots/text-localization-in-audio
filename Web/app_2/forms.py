from django.forms import ModelForm
from .models import UserQueryRequest


class UserQueryRequestForm(ModelForm):
    class Meta:
        model = UserQueryRequest
        fields = "__all__"

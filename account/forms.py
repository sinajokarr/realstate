from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'age',
            'is_agent',
            'agency_name',
            'phone_number',
            'avatar',
        )

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'is_agent',
            'agency_name',
            'phone_number',
            'avatar',
        )

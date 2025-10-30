from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomCreationForm, CustomChangeForm

User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomCreationForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserUpdateViews(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = CustomChangeForm
    template_name = "account/update_account.html"
    success_url = reverse_lazy("PostListView")

    def get_object(self):
        return self.request.user

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
   
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f"Account created for {username}!")
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'user'
    slug_field = 'username'



    
    
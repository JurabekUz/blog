from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SingUpForm, EditProfileForm, PassChangeForm, UserProfileForm
from django.contrib.auth.views import PasswordChangeView
from core.models import Profile

'''
def delpost(request, pk):
    page_user = Profile.objects.get(id=pk)
    page_user.delete()

    return render(request, 'home.html')
'''


class DeleteProfilePage(generic.DeleteView):
    model = Profile
    success_url = reverse_lazy('home')


class UserCreateProfileView(generic.CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'registration/create_user_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserEditProfile(generic.UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'registration/edit_user_profile.html'
    #fields = '__all__'
    success_url = reverse_lazy('home')


class UserProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(UserProfileView,self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class PasswordsChange(PasswordChangeView):
    form_class = PassChangeForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('home')


def PasswordSuccess(request):
    return render(request,'registration/pass_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self): 
        return self.request.user


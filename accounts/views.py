from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .form import Reg, Ed
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

class Userdet(DetailView):
    model = User
    template_name = 'accounts/prof.html'
    context_object_name = 'userdata'

class editus(UpdateView):
    model = User
    template_name = 'accounts/edus.html'
    success_url = reverse_lazy('loginredirect')
    form_class = Ed
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request,user)
        return response
class Crus(CreateView):
    model = User
    template_name = 'accounts/reg.html'
    form_class = Reg
    success_url = reverse_lazy('loginredirect')
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

class Delus(DeleteView):
    model = User
    template_name = 'accounts/delus.html'
    success_url = reverse_lazy('home:home')

@login_required()
def loginredirect(request):
    return redirect('userdetails', pk=request.user.id)
@login_required
def logoutredirect(request):
    return render(request, 'registration/logout.html')
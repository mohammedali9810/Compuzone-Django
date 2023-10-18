from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from .models import comps, catg
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView

def home(request):
    products = comps.objects.all()
    return render(request, template_name='home/index.html', context={"products": products})

def products(request, id):
    product = get_object_or_404(comps, id=id)
    return render(request, template_name='home/products.html', context={"product": product})

def contact(request):
    return render(request, template_name='home/contact.html')

def about(request):
    return render(request, template_name='home/about.html')



def search(request):
    query = request.GET.get('query')
    comps_result = comps.objects.filter(name__icontains=query)

    context = {
        "products": comps_result,
        "query": query
    }
    return render(request, 'home/search.html', context)


# def delete(request, id):
#     comp = get_object_or_404(comps, id=id)
#
#     if comp:
#         comp.delete()
#         return redirect('/')
#     else:
#         return HttpResponse("Sorry, Computer Part Not Found !!")

class prodedform(forms.ModelForm):
    class Meta:
        model = comps
        exclude = ['owner']

class edit(UpdateView):
    model = comps
    template_name = 'home/addprod.html'
    form_class = prodedform
    success_url = reverse_lazy('home:home')
    def form_valid(self, form):
        if self.get_object().owner == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponseForbidden(render(self.request, 'home/forbid.html').content)

class delete(DeleteView):
    model = comps
    template_name = 'home/delete.html'
    success_url = reverse_lazy('home:home')
    def form_valid(self, form):
        if self.get_object().owner == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponseForbidden(render(self.request, 'home/forbid.html').content)

class add_product(CreateView):
    model = comps
    template_name = 'home/addprod.html'
    form_class = prodedform
    success_url = reverse_lazy('home:home')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def cat_det(request, category):
    cats = comps.objects.filter(category__name=category)
    context = {
        'comps': cats,
        'category': category
    }
    return render(request, 'home/cat_det.html', context)
def cat_list(request):
    categories = catg.objects.all()
    context = {
        'categories': categories}
    return render(request, 'home/cat.html', context)

def custom_404(request, exception):
    return render(request, 'custom_404.html', status=404)
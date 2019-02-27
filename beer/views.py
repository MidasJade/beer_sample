# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, FormView
from .models import Fermentable
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy, resolve


# Create your views here.
#=======================================================================
# Forms related to Fermentable object
#=======================================================================
def fermentable_list_view(request):
    f = queryset=Fermentable.objects.all().order_by('name')
    return render(request, 'fermentable_list.html', {'filter': f})

class FermentableCreateView(CreateView):
    model = Fermentable
    template_name = 'fermentable_create.html'

    fields = '__all__'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect(reverse('inventory_fermentable_list'))

class FermentableDetailView(DetailView):
    model = Fermentable
    template_name = 'fermentable_detail.html'

class FermentableUpdateView(UpdateView):
    model = Fermentable
    template_name = 'fermentable_update.html'
    fields = [
        'name',
        'description',
        'color',
        'extract',
        'moisture',
        'mash_required',
        'quantity'
    ]

    def get_object(self, queryset=None):
        print (self.kwargs)
        id = self.kwargs['pk']
        return self.model.objects.get(id=id)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('inventory_fermentable_list'))

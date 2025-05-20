from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.shortcuts import render, redirect
from .models import Zakladatel, Znacka, Druh
from .forms import ZakladateleForm, ZnackaForm, DruhForm


# Create your views here.
def index(request):
    context = {
        'zakladatele': Zakladatel.objects.all(),
        'znacky': Znacka.objects.all(),
        'druhy': Druh.objects.all(),
    }
    return render(request, 'index.html', context=context)




# automobilky
class AutomobilkyList(ListView):
    model = Znacka
    template_name = 'automobilky/automobilky_list.html'
    queryset = Znacka.objects.order_by('-rok_zalozeni')
    context_object_name = 'automobilky'


class AutomobilkyDetail(DetailView):
        model = Znacka
        template_name = 'automobilky/automobilky_detail.html'
        context_object_name = 'automobilky'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['druhy'] = Druh.objects.filter(znacka=self.object)
            return context


class AutomobilkyCreate(CreateView):
    model = Znacka
    form_class = ZnackaForm
    template_name = 'automobilky/create_automobilky.html'

    def get_success_url(self):
        return reverse_lazy('automobilky_detail', kwargs={'pk': self.object.pk})


def create_automobilka(request):
    if request.method == 'POST':
        form = ZnackaForm(request.POST, request.FILES)
        if form.is_valid():
            automobilka = form.save()
            return redirect('automobilky_detail', pk=automobilka.pk)
    else:
        form = ZnackaForm()

    return render(request, 'automobilky/create_automobilky.html', {'form': form, 'manual': False})

class AutomobilkyUpdate(UpdateView):
    model = Znacka
    form_class = ZnackaForm
    template_name = 'automobilky/update_automobilky.html'
    context_object_name = 'automobilky'

    def get_success_url(self):
        return reverse_lazy('automobilky_detail', kwargs={'pk': self.object.pk})

class AutomobilkyDelete(DeleteView):
    model = Znacka
    template_name = 'automobilky/delete_automobilky.html'
    context_object_name = 'automobilky'
    success_url = reverse_lazy('automobilky_list')





# zakladatele
class ZakladateleList(ListView):
    model = Zakladatel
    template_name = 'zakladatele/zakladatele_list.html'
    queryset = Zakladatel.objects.order_by('-narozeni')
    context_object_name = 'zakladatele'


class ZakladateleDetail(DetailView):
    model = Zakladatel
    template_name = 'zakladatele/zakladatele_detail.html'
    context_object_name = 'zakladatele'


class ZakladateleCreate(CreateView):
    model = Zakladatel
    form_class = ZakladateleForm
    template_name = 'zakladatele/create_zakladatele.html'

    # Po úspěšném uložení knihy přesměrování na detail knihy
    def get_success_url(self):
        return reverse_lazy('zakladatele_detail', kwargs={'pk': self.object.pk})


def create_zakladatel(request):
    if request.method == 'POST':
        form = ZakladateleForm(request.POST, request.FILES)
        if form.is_valid():
            zakladatel = form.save()
            return redirect('zakladatele_detail', pk=zakladatel.pk)
    else:
        form = ZakladateleForm()

    return render(request, 'zakladatele/create_zakladatele.html', {'form': form, 'manual': False})

class ZakladateleUpdate(UpdateView):
    model = Zakladatel
    form_class = ZakladateleForm
    template_name = 'zakladatele/update_zakladatele.html'
    context_object_name = 'zakladatel'

    def get_success_url(self):
        return reverse_lazy('zakladatele_detail', kwargs={'pk': self.object.pk})

class ZakladateleDelete(DeleteView):
    model = Zakladatel
    template_name = 'zakladatele/delete_zakladatele.html'
    context_object_name = 'zakladatel'
    success_url = reverse_lazy('zakladatele_list')





# druhy
class DruhyList(ListView):
        model = Druh
        template_name = 'druhy/druhy_list.html'
        queryset = Druh.objects.order_by('-rok_zalozeni')
        context_object_name = 'druhy'

        def get_queryset(self):
            znacka_id = self.request.GET.get('znacka')
            if znacka_id:
                return Druh.objects.filter(znacka_id=znacka_id).order_by('-rok_zalozeni')
            return Druh.objects.order_by('-rok_zalozeni')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['znacky'] = Znacka.objects.all()
            znacka_id = self.request.GET.get('znacka')
            context['vybrana_znacka'] = Znacka.objects.get(id=znacka_id) if znacka_id else None
            return context

class DruhyDetail(DetailView):
    model = Druh
    template_name = 'druhy/druhy_detail.html'
    context_object_name = 'druh'


class DruhyCreate(CreateView):
    model = Druh
    form_class = DruhForm
    template_name = 'druhy/create_druhy.html'

    def get_success_url(self):
        return reverse_lazy('druhy_detail', kwargs={'pk': self.object.pk})

def create_druhy(request):
    if request.method == 'POST':
        form = DruhForm(request.POST, request.FILES)
        if form.is_valid():
            druh = form.save()
            return redirect('druhy_detail', pk=druh.pk)
    else:
        form = DruhForm()

    return render(request, 'druhy/druhy_detail.html', {'form': form, 'manual': False})

class DruhyUpdate(UpdateView):
    model = Druh
    form_class = DruhForm
    template_name = 'druhy/update_druhy.html'
    context_object_name = 'druh'

    def get_success_url(self):
        return reverse_lazy('druhy_detail', kwargs={'pk': self.object.pk})

class DruhyDelete(DeleteView):
    model = Druh
    template_name = 'druhy/delete_druhy.html'
    context_object_name = 'druh'
    success_url = reverse_lazy('druhy_list')
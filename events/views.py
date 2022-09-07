from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Event


from django.views.generic.list import ListView

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'instituicao']
    template_name = 'event/createNewEvent.html'

    def get_success_url(self):
        return reverse('listEvents')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventListView(LoginRequiredMixin, ListView):

    model = Event
    paginate_by = 10
    template_name = 'event/listEvents.html'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

class EventDetailView(LoginRequiredMixin, DetailView):
    
    model = Event
    template_name = 'event/eventDetail.html'

    # def get_context_data(self, *args, **kwargs):

    #     context = super(Event, self).get_context_data(*args, **kwargs)

    #     return context
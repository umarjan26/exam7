from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class ChoiceCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choice.create(**form.cleaned_data)
        return redirect('detail', pk=poll_pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    success_url = reverse_lazy('detail')
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.poll.pk})
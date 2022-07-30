from django.urls import reverse, reverse_lazy

from webapp.forms import PollForm
from webapp.models import Poll

from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ("-created_at",)
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')


class DetailsView(DetailView):
    template_name = 'poll/detail_view.html'
    model = Poll
    context_object_name = 'poll'


class UpdatesView(UpdateView):
    model = Poll
    template_name = 'poll/update_view.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})



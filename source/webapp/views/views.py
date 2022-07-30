from webapp.models import Poll

from django.views.generic import ListView, DetailView


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

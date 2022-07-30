from webapp.models import Poll

from django.views.generic import ListView


class IndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/index.html'
    ordering = ("-created_at",)
    paginate_by = 5
    paginate_orphans = 0

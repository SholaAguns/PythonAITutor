from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Query, Response
from .utils import get_gpt_response

User = get_user_model()

# class IndexPage(TemplateView):
#     template_name = 'tutor_index.html'


def handle_request(request, pk):
    new_query = Query()
    if pk == 1:
        new_query.request = "schedule"
        subjects = request.POST.get('input')
        prompt = f"Create a weekly study schedule for me including the following subjects: {subjects}"
    elif pk == 2:
        new_query.request = "motivation"
        prompt = f"Give me some motivation to study with tough love"
    elif pk == 3:
        new_query.request = "quiz"
        topic = request.POST.get('input')
        prompt = f"Create a 15 question quiz based on the following topic: {topic}"
    else:
        return render(request, 'mytutor/tutor_index.html')

    response = Response()
    response.query = new_query
    response.text = get_gpt_response(prompt)
    new_query.save()
    response.save()
    return render(request, 'mytutor/response_detail.html', {'response' : response})

class ResponseDetail(LoginRequiredMixin, generic.DetailView):
    model = Response


class QueryList(generic.ListView):
    model = Query
    template_name = "notes/user_queries_list.html"

    def get_queryset(self):
        try:
            self.query_user = User.objects.prefetch_related("queries").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.query_user.queries.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_user"] = self.query_user
        return context



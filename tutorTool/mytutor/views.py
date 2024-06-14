from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Query, Response
from .utils import get_gpt_response

User = get_user_model()


@login_required()
def handle_request(request, pk):
    new_query = Query()
    response = Response()
    new_query.user = request.user

    if pk == 1:
        new_query.request = "schedule"
        subjects = request.POST.get('input')
        new_query.input = f"Create a weekly study schedule for me including the following subjects: {subjects}"
    elif pk == 2:
        new_query.request = "motivation"
        new_query.input = f"Give me some motivation to study with tough love"
    elif pk == 3:
        new_query.request = "quiz"
        topic = request.POST.get('input')
        new_query.input = f"Create a 15 question quiz based on the following topic: {topic}"
    else:
        return render(request, 'mytutor/tutor_index.html')

    new_query.save()

    response.text = get_gpt_response(new_query.input)


    response.query = Query.objects.get(id=new_query.id)
    response.save()

    return render(request, 'mytutor/response_detail.html', {'response' : response})


class ResponseDetail(LoginRequiredMixin, generic.DetailView):
    model = Response



@login_required()
def return_queries(request):
    context = {}
    context["queries"] = Query.objects.filter(user=request.user)

    return render(request, 'mytutor/user_queries_list.html', context)





from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .models import Response
from .utils import get_gpt_response

User = get_user_model()


@login_required()
def handle_request(request, pk):
    new_response = Response()
    new_response.user = request.user

    if request.method == 'POST':
        if pk == 1:
            new_response.request = "Study schedule"
            subjects = request.POST.get('input')
            new_response.input = f"Create a weekly study schedule for me including the following subjects: {subjects}. Provide your response in html friendly format"
        elif pk == 2:
            person = request.POST.get('input')
            new_response.request = "Motivation from " + person
            new_response.input = f"Give me some tough love motivation to study as posing as {person}. Provide your response in html friendly format"
        elif pk == 3:

            topic = request.POST.get('input')
            new_response.request = topic + " quiz"
            new_response.input = f"Create a 15 question quiz based on the following topic: {topic}. Include the answers further down in youb resposne so I hahve to scroll down to see them. Provide your response in html friendly format"
        else:
            return render(request, 'mytutor/tutor_index.html')


        new_response.text = get_gpt_response(new_response.input)
        new_response.save()

        return render(request, 'mytutor/response_detail.html', {'response' : new_response})
    else:
        return render(request, 'mytutor/tutor_index.html')


class ResponseDetail(LoginRequiredMixin, generic.DetailView):
    model = Response


class ResponseList(LoginRequiredMixin, generic.ListView):
    model = Response


@login_required()
def delete_response(request, pk):
    response = get_object_or_404(Response, pk=pk)
    response.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))










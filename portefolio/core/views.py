from django.shortcuts import render
import pkgutil
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q, Count, F
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View
from .forms import ContatcForm
from .models import Project



# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        
        context = {
            'projects':projects,
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):

        form = ContatcForm(request.POST)
        projects = Project.objects.all()
        if form.is_valid():
            
            new_post = form.save(commit=False)
            new_post.save()

        context = {
                    'form': form,
                    'projects':projects,
                }
        return render(request, 'index.html', context)

class ChatBotView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chatbot.html')



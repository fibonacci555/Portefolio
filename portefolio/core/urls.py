from django.urls import path

from .views import HomeView, ChatBotView
from django.views.static import serve


urlpatterns = [ 
     
    path('', HomeView.as_view(), name='home'),
    path('chatAI', ChatBotView.as_view(), name='chat')
    ]
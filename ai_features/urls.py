from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='ai-chat'),
    path('chat/history/', views.chat_history, name='chat-history'),
    path('upload/', views.upload_statement, name='upload-statement'),
    path('statements/', views.statement_history, name='statement-history'),
]

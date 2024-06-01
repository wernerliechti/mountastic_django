from django.urls import path
from .views import mountain_quiz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('quiz/', mountain_quiz, name='mountain_quiz'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
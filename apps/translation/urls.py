from django.urls import path
from .views import TranslationListView, translation_tool, TranslationDetailView, TranslationDeleteView

app_name = 'translation'
urlpatterns = [
    path('', TranslationListView.as_view(), name='list'),
    path('new/', translation_tool, name='create'),
    path('<int:pk>/', TranslationDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', TranslationDeleteView.as_view(), name='delete'),
]
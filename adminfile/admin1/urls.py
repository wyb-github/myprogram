from django.urls import path
from django.views.generic import TemplateView


from .views import GoodsAPI

urlpatterns = [
    path("",TemplateView.as_view(template_name='index.html')),
    path("category", TemplateView.as_view(template_name='category.html')),
    path("api/goods",GoodsAPI.as_view()),
]
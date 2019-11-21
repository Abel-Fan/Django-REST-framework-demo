from django.urls import path
from django.views.generic import TemplateView

from .views import index,GoodsView,GoodsOneView,Login

urlpatterns = [
    path("",TemplateView.as_view(template_name='index.html')),
    path("category", TemplateView.as_view(template_name='category.html')),
    path("api/goods",GoodsView.as_view()),
    path("api/goods/<int:id>", GoodsOneView.as_view()),
    path("api/login", Login.as_view()),
]
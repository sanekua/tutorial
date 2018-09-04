

# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # # ex: /polls/5/
#     # path('<int:question_id>/', views.detail, name='detail'),
#     # # ex: /polls/5/results/
#     # path('<int:question_id>/results/', views.results, name='results'),
#     # # ex: /polls/5/vote/
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include
from django.views import View



urlpatterns = [
    path('university/', views.index, name='index'),
    # path('university/', views.MyView.as_view(), name='index'),
    # path('', include('django.contrib.auth.urls')),
    # path(‘my_univer’, login_required(MyCustomView.as_view())),
]

from django.contrib import admin

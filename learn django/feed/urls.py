from django.urls import path
from .views import HomePageView
from .views import PostDetailsView, AddFormView

app_name="feed"

urlpatterns=[
    path('',HomePageView.as_view(),name='index'),
    path('detail/<int:pk>/',PostDetailsView.as_view(),name='detail' ),
    path('post/', AddFormView.as_view(),  name='post'),
]
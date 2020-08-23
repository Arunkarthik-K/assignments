from django.urls import include, path
from rest_framework import routers
from .views import pendinglistview, approvedlistview, createlistview, updatelistview, update2listview, deletelistview, delete2listview


urlpatterns = [
    path('pending/',pendinglistview.as_view()),
    path('pending/<int:id>',pendinglistview.as_view()),
    path('approved/',approvedlistview.as_view()),
    path('approved/<int:id>',approvedlistview.as_view()),
    path('create/',createlistview.as_view()),
    path('update/',updatelistview.as_view()),
    path('update/<int:id>',updatelistview.as_view()),
    path('update2/',update2listview.as_view()),
    path('update2/<int:id>',update2listview.as_view()),
    path('delete/',deletelistview.as_view()),
    path('delete/<int:id>',deletelistview.as_view()),
    path('delete2/',delete2listview.as_view()),
    path('delete2/<int:id>',delete2listview.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
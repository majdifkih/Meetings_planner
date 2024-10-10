from django.urls import path
from .views import detail,meetings_list_view

urlpatterns = [
    path('', meetings_list_view, name='meetings_list_view'),  # List of meetings and rooms

    path('detail/<int:id>/', detail, name='detail'),  # Meeting detail
   

]
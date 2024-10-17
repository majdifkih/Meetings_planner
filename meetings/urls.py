from django.urls import path
from .views import add_meeting, detail,meetings_list_view,del_meeting,update_meeting

urlpatterns = [
    path('', meetings_list_view, name='meetings_list_view'),  # List of meetings and rooms

    path('detail/<int:id>/', detail, name='detail'),  # Meeting detail
    
    path('newMeet', add_meeting, name='newMeet'), 
    path('delete/', del_meeting, name='del_meeting'),
    path('update/<int:id>/', update_meeting, name='update_meeting'),

]
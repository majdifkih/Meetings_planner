from .forms import MeetingForm
from .models import Room,Meeting  
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Meeting
def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings

    return render(request, 'meetings/meetings.html', {'meetings': meetings, })

 

 

def detail(request, id):

    meeting = get_object_or_404(Meeting, id=id)  # Correct model name and function

    return render(request, "meetings/details.html", {"meeting": meeting})

def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('meetings_list_view')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'meetings/new.html', {'form': form})

def del_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id) 
    if request.method == 'POST':
        meeting.delete()  
        return redirect('meetings_list_view')
    else:
        return HttpResponse('Error')



def update_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id) 
    
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save() 
            return redirect('meetings_list_view')
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'meetings/update.html', {'form': form, 'meeting': meeting})
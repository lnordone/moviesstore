from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MoviePetition
from .forms import MoviePetitionForm

@login_required
def petition_list(request):
    petitions = MoviePetition.objects.all().order_by('-created_at')
    return render(request, 'petitions/petition_list.html', {'petitions': petitions})

@login_required
def create_petition(request):
    if request.method == "POST":
        form = MoviePetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            messages.success(request, 'Petition created successfully!')
            return redirect('petition_list')
    else:
        form = MoviePetitionForm()
    return render(request, 'petitions/create_petition.html', {'form': form})
        
@login_required
def vote_petition(request, petition_id):
    petition = get_object_or_404(MoviePetition, id=petition_id)
    if request.user not in petition.voters.all():
        petition.voters.add(request.user)
        petition.votes_count += 1
        petition.save()
        messages.success(request, 'Vote recorderd successfully!')
    else:
        messages.warning(request, 'You have already voted on this petition!')
    return redirect('petition_list')
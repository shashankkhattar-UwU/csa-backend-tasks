from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Track
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    context={
        'tracks':Track.objects.all()
    }
    return render(request, 'song/home.html', context)

class TrackListView(ListView):
    model=Track
    template_name='song/home.html'
    context_object_name='tracks'
    ordering=['-views']
    
class TrackDetailView(LoginRequiredMixin, DetailView):
    model=Track
    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.newView()
        return item
    
class TrackCreateView(LoginRequiredMixin, CreateView):
    model=Track
    fields=['title', 'artist', 'image', 'audio']
    
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
    
class TrackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Track
    fields=['title', 'artist', 'image', 'audio']
    
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
    def test_func(self):
        track=self.get_object()
        if self.request.user == track.uploader:
            return True
        return False

class TrackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Track
    success_url='/'
    def test_func(self):
        track=self.get_object()
        if self.request.user == track.uploader:
            return True
        return False
    
def LikeTrack(request, pk):
    track=get_object_or_404(Track, id=request.POST.get('track_id'))
    track.likes.add(request.user)
    return HttpResponseRedirect(reverse('track-detail', args=[str(pk)]))
    
def DisLikeTrack(request, pk):
    track=get_object_or_404(Track, id=request.POST.get('track_id'))
    track.likes.remove(request.user)
    return HttpResponseRedirect(reverse('track-detail', args=[str(pk)]))
    
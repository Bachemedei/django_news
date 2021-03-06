from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm


class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy("news:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateStoryView(UserPassesTestMixin, generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy("news:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.get_object()})
        return kwargs

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False
    


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class DeleteStory(UserPassesTestMixin, generic.DeleteView):
    model = NewsStory
    success_message = "Story: %(title)s has been deleted"

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False

    def get_success_url(self):   
        storyId =self.kwargs['pk']
        story = self.get_object()
        print(story)
        author = story.author.username
        success_message = self.success_message % {'title': story.title}
        messages.success(self.request, success_message)
        print(success_message)
        return reverse_lazy("users:userProfile", kwargs = {'slug': author})

class ViewUsersStories(generic.DetailView):
    model = CustomUser
    template_name = 'news/usersStories.html'
    context_object_name = 'user'
    slug_field = 'username'
    

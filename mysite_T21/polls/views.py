# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, path 
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.conf import settings
from django.shortcuts import redirect

class IndexView(generic.ListView):
    '''link template file index.html to view'''
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    '''link template file detail.html to detail view for question model'''
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    '''link template file results.html to view'''
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    '''Vote view
        - checks if user is logged in to vote
        - redirected to login screen if they are not logged in
        - if logged in they are able to vote
        - Admin is a regarded as logged in user and will need to log out each session
        '''
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else: 
        return HttpResponseRedirect(reverse('user_auth:login') )   
        

        
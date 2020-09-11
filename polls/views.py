from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from polls.models import Question, Choice

def feed(request):
    questions = Question.objects.order_by('-mod_date')
    context = {'qns': questions}
    return render(request, 'polls/feed.html', context)

def vote(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/vote.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.no_of_votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('result', args=(question.id,)))
    else:
        return render(request, 'polls/vote.html', {'question': question})

def result(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'polls/result.html', {'question': question})

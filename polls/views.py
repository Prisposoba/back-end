import polls
from polls.models import Invention, Proposal
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def detail(request, invention_id):
    invention = get_object_or_404(Invention, pk=invention_id)
    return render(request, 'polls/details.html', {'invention': invention})

def results(request, invention_id):
    invention = get_object_or_404(Invention, pk=invention_id)
    return render(request, 'polls/results.html', {'invention':invention})

def vote (request, invention_id):
    invention = get_object_or_404(Invention, pk=invention_id)
    try:
        selected_proposal = invention.proposal_set.get(pk=request.POST['proposal'])
    except (KeyError, Proposal.DoesNotExist):
        return render(request, 'polls/details.html', {
            'invention': invention,
            'error_message': 'You didn`t select a choice',
        })
    else:
        selected_proposal.votes += 1
        selected_proposal.save()
        return HttpResponseRedirect(reverse('polls:results', args=(invention.id,)))


def index(request):
    latest_invention_list = Invention.objects.order_by('-publication_date')[:5]
    context = {'latest_invention_list': latest_invention_list}
    return render(request, 'polls/index.html', context)
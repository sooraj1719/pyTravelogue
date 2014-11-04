# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from journeys.models import Station
from entry.models import Entries
from django.db.models import Count
	
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    stations_list=Station.objects.all()
    #journey_list=Entries.objects.annotate(num_trains=Count('train_name')).order_by('-num_trains')[:]
    journey_list=Entries.objects.values('train_name').annotate(dcount=Count('train_name'))
    context_dict = {'stations': stations_list, 'entries':journey_list}
	
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('journeys/index.html', context_dict, context)
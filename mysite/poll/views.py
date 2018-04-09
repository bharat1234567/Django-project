from django.http import HttpResponse, Http404
from django.shortcuts import  redirect, render, get_object_or_404
from .models import Question
from django.template import loader


def index(request):
    return redirect("welcome")

# we need to return an object of HTTP-RESPONSE or 404 error.
# we also send back html files


def welcome(request):
    response = "we welcome you to our website!"
    return HttpResponse(response)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# here what we did is we loaded the template first, then we created a context which can be
# used by html file. then we send this context and request to html file using template.render
# after that whatever result came got wrapped in HTTP Response and sent it back to the user
def showtopfive(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    temp = loader.get_template('poll/top-five.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(temp.render(context, request))

# the above operation is a very common thing and django provides a common way to do it!!
# here we found the context, directly returned a rendered object!

def showtopfivealter(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/top-five.html', context)

# THIS shows how to use try catch block,raise an error!
def detailed(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poll/details.html', {'question': question})

# This above thing can be done using a simple method call:
# get_object_or_404 method. it will return the object or return 404 error
# this sits in django.shortcuts

def detail2(request,question_id):
    q = get_object_or_404(Question,pk=question_id)
    return render(request, 'poll/details.html',{'question':q})


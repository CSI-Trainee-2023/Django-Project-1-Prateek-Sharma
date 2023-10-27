from django.shortcuts import render
from .models import Question,Choice
from .forms import Create
from pollsapp.models import newpolls



# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    

    return render(request, 'vote.html', {'question':question, 'options': options})

def result(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST' :
        inputvalue = request.POST['choice']
        selection_option = options.get(id = inputvalue)
        selection_option.vote += 1
        selection_option.save()
    return render(request, 'result.html', {'question':question, 'options':options})

def create(request):

    fn=Create()
    data = {'form':fn}
    return render(request, 'create.html', data)

def saveform(request):
    n = ''
    if request.method =='POST':
        question= request.POST.get('QUESTION')
        option1 = request.POST.get('OPTION1')
        option2 = request.POST.get('OPTION2')
        option3 = request.POST.get('OPTION3')
        option4 = request.POST.get('OPTION4')
        en = newpolls(question=question,option1=option1,option2=option2,option3=option3,option4=option4)
        en.save()
        n= 'New Poll created successfully !!'
    return render(request, 'create.html', {'n':n} )
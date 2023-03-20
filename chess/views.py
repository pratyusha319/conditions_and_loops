from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':40,'b':20,'c':30}
    return render(request,'condition.html',d)
def if_else(request):
    d={'a':40,'b':60,'c':30}
    return render(request,'if_else.html',d)


def if_elif(request):
    d={'a':40,'b':60,'c':80}
    return render(request,'if_elif.html',d)

def nested(request):
    d={'a':40,'b':60,'c':30}
    return render(request,'nested.html',d)

def forloop(request):
    d={'name':'shanti'}
    return render(request,'forloop.html',d)




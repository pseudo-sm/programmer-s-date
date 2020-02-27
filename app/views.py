from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import requests
# Create your views here.

url = "https://api.hackerearth.com/v3/code/compile/"
run_url = "https://api.hackerearth.com/v3/code/run/"
def index(request):
    problems = Problems.objects.all()
    return render(request,"index.html",{"problems":problems})

def start(request):
    p1 = request.GET.get("p1")
    p2 = request.GET.get("p2")
    id = request.GET.get("id")
    problem = Problems.objects.get(sl=id)
    submission = Submissions(player1=p1,player2=p2,question=problem)
    submission.save()
    return JsonResponse({"uc":submission.pk},safe=False)

def gfg_compile(lang, code, _input=None, save=False):
    data = {
      'lang': lang,
      'source': code,
      "client_secret" : "9e94c82bb37aad13733fa9815ab23bfe522b6520",
      "input" : _input
    }

    r = requests.post(url,data=data)
    r = requests.post(run_url,data=data)
    return r

def compile(request):

    lang = request.GET.get("lang")
    code = request.GET.get("code")
    input = request.GET.get("input")
    result = gfg_compile(lang,code,input)
    print(result.json())
    return JsonResponse({"output" : result.json()},safe=False)

def start_exam(request):
    uc = request.GET.get("uc")
    request.session["uc"] = uc
    return JsonResponse(True,safe=False)

def submit(request):

    submission = request.session["uc"]
    code = request.GET.get("code")
    submission = Submissions.objects.get(pk=submission)
    submission.code = code
    submission.save()
    return JsonResponse(submission.pk,safe=False)

def editor(request):

    return render(request,"editor.html")
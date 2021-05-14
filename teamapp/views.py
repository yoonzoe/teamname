from django.shortcuts import render


def team(request):
    return render(request, "team.html")

def result(request):
    userinput = int(request.GET['input'])
    if userinput == 3:
        output = "3팀 입니다!"
    else:
        output = "try again"
    return render(request, "result.html", {'output' : output})

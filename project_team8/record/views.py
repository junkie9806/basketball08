from django.shortcuts import render, redirect
from .models import Record

def record_main(request):
    records = Record.objects.all()
    return render(request, 'record/record_main.html', {'records':records})
    # 다른 뷰 함수를 추가할 수 있습니다.


def record_write(request):
    records = Record.objects.all()
    if request.method == 'POST':
        record_name = request.POST.get('record_name')
        score = request.POST.get('score')
        assist = request.POST.get('assist')
        rebound = request.POST.get('rebound')
        steal = request.POST.get('steal')
        block = request.POST.get('block')
        record = Record(record_name=record_name, score=score, assist=assist, rebound=rebound, steal=steal, block=block)
        record.save()
        return redirect('main:record:record_main')
    return render(request, 'record/record_write.html', {'records':records})
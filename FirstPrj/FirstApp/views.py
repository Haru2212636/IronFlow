from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # 最初のページ表示用
    return render(request, "FirstApp/index.html")

def add_log(request):
    # HTMXからの送信（POSTリクエスト）を受け取った時の処理
    if request.method == "POST":
        exercise = request.POST.get("exercise", "")
        weight = request.POST.get("weight", "")
        
        # ページ全体ではなく、追加したい「1行分」のHTMLだけを作って返す
        html_fragment = f'<li style="padding: 8px 0; border-bottom: 1px solid #eee;"><strong>{exercise}</strong>: {weight} kg</li>'
        return HttpResponse(html_fragment)
    
    return HttpResponse("")

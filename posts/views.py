from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.generic.list import ListView

from posts.models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')


# fbv
def url_view(request):
    # return HttpResponse('<h1>url_view</h1>')
    print('url_view()')
    data = {'code':'001', 'msg':'OK'}
    return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method : {request.method}')
    
    if request.method == 'GET':
        print(f'request.GET : {request.GET}') # 데이터를 받을 때
    elif request.method == 'POST':  
        print(f'request.POST : {request.POST}') # 데이터를 추가 수정 삭제할 때
        
    return render(request, 'view.html')


# cbv
class class_view(ListView):
    model = Post
    ordering = ['-id']
    template_name = 'cbv_view.html'

# cbv를 fbv로    
def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list':object_list})
from django.shortcuts import render, redirect
from accounts.forms import UserCreateForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    # GET 요청 시 HTML 요청
    if request.method == 'GET':
        form = SignUpForm
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password2 = form.cleaned_data['password2']
            instance = form.save()
            return redirect('index')

        else:
            #리다이렉트
            return redirect('accounts:signup')
        
def login_view(request):
    # GET, POST 분리
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    else :
        form = AuthenticationForm(request, data=request.POST)
        # 데이터 유효성 검사
        if form.is_valid():  
            # 데이터 유효성 검사
            login(request, form.user_cache)
            # 응답
            return redirect('index')
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return render(request, 'accounts/login.html', {'form':form})
        #응답
        
def logout_view(request):
    # 데이터 유효성 검사
    if request.user.is_authenticated:
        logout(request)
    # 비즈니스 로직 처리 - 로그아웃
    return redirect('index')
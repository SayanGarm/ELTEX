from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .models import Profile
# from .decorators import allowed_roles

def StartPageSwitch(request):
    user = Profile.objects.get(user=request.user)
    
    if (user):
        if (user.groupExists()):
            if (user.is_teacher()):
                return TeacherPage.as_view()(request)
        else:
            return HttpResponse('Вы не имеете требуемой должности!')

        return StudentPage.as_view()(request)
    else:
        return redirect('login')

class StudentPage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        context = { 'profile': profile }

        return render(request, 'registration/user_home.html', context)

class TeacherPage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        context = { 'profile': profile,
                    'is_teacher': True
                  }

        return render(request, 'registration/moderator_home.html', context)

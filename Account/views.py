from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from LaboratoryWork.models import Article
from LaboratoryWork.forms import ArticleListForm
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

        articles = Article.objects.filter(author=request.user)
        articles_count = {
            'A': articles.filter(status='A').count(),
            'B': articles.filter(status='B').count(),
            'C': articles.filter(status='C').count()
        }
        
        context = { 'profile': profile,
                    'articles': articles,
                    'articles_count': articles_count,
                }

        return render(request, 'registration/user_home.html', context)

class TeacherPage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

      
        articles = Article.objects.all()
        articles_count = {
            'A': articles.filter(status='A').count(),
            'B': articles.filter(status='B').count(),
            'C': articles.filter(status='C').count()
        }
        
        context = { 'profile': profile,
                    'articles_count': articles_count,
                    'is_moder': True
                  }

        return render(request, 'registration/moderator_home.html', context)


class UsersListPage(View):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.get_student()

        context = { 'users': profiles }

        return render(request, 'registration/users_list.html', context)

class UserProfilePage(View):
    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)

        search_form = ArticleListForm(request.GET)

        articles = Article.objects.filter(author=profile.user)
        articles_count = {
            'A': articles.filter(status='A').count(),
            'B': articles.filter(status='B').count(),
            'C': articles.filter(status='C').count()
        }
        
        context = { 'profile': profile,
                    'articles': articles,
                    'articles_count': articles_count,
                    'search_form': search_form}

        return render(request, 'registration/user_page.html', context)
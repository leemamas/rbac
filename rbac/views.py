from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import re
from rbac.service.permission import *

# Create your views here.
def login(request):

    if request.method == 'POST':

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            request.session['user_id']=user.pk
            # permissions=user.roles.all().values('permissions__url').distinct()
            #
            # permissionsList=[]
            # for permission in permissions:
            #     permissionsList.append(permission['permissions__url'])
            #
            #
            # request.session['permissionsList']=permissionsList


            initial_session(request,user)

            return HttpResponse('login success!')
        else:
            msg='error!'

    return render(request, 'login.html', locals())


def users(request):
    print('xxxxx',request.session['user_id'])



    return HttpResponse('user view!')


def user_add(request):
    return HttpResponse('user add！')

def user_edit(request,id):
    permissionsList = request.session['permissionsList']

    current_path = request.path_info

    print(permissionsList)

    flag=False
    for permission in permissionsList:
        permission='^%s$'%permission
        ret=re.match(permission,current_path)
        if ret:
            flag=True
            break

    if flag:
        print('have permission!')
        return HttpResponse('user edit！edit:{}'.format(id))


    return HttpResponse('not permission!')

def user_delete(request,id):
    print('delete',id)
    return HttpResponse('user delete！')


def roles(request):
    return HttpResponse('roles views!')


def role_add(request):
    return HttpResponse('role add!')

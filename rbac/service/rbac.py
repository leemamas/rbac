from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse,redirect


class ValidPermission(MiddlewareMixin):

    def process_request(self, request):

        current_path = request.path_info

        #白名单
        whiteList = ['/login/', '/admin/.*']

        for url in whiteList:
            ret = re.match(url, current_path)
            if ret:
                return None

        #检验登录
        user_id=request.session.get('user_id')
        if not user_id:
            return redirect('/login/')


        permissionsList = request.session.get('permissionsList', [])

        flag = False

        for permission in permissionsList:
            permission = '^%s$' % permission
            ret = re.match(permission, current_path)
            if ret:
                flag = True
                break
        if not flag:
            return HttpResponse('没有权限！')

        return None

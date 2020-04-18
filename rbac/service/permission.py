

def initial_session(request,user):
    permissions = user.roles.all().values('permissions__url').distinct()

    permissionsList = []
    for permission in permissions:
        permissionsList.append(permission['permissions__url'])

    request.session['permissionsList'] = permissionsList
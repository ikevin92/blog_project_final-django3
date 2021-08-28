from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # extraer id del comentario
            id_comment = view.kwargs['pk']
            # se buscar por el id del comentario
            comment = Comment.objects.get(pk=id_comment)

            # extraer el usuario de la peticion
            id_user = request.user.pk
            id_user_comment = comment.user_id

            # se comparan los ids de los usuarios
            if id_user == id_user_comment:
                return True

            return False

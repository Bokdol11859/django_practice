from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.author == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

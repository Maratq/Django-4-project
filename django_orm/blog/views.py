from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

@login_required
@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    #Код для добавления нового поста
    if not request.user.has_perm('blog.add_post'):
        raise PermissionDenied
    return render(request)


class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    fields = ('name', 'content')
    template_name = "post.html"
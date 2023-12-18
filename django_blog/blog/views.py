from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post

# Create your views here.
def post_list(request):
    """
    Выдаёт все записи из таблицы Post. С модификатором Published
    :param request:
    :return:
    """
    all_posts = Post.objects.all()
    return render(request, "blog/post/list.html", {"posts": all_posts})

def post_detail(request, post_id: int):
    """
    Возвращает информацию об 1 записи по его id
    :param request:
    :param post_id:
    :return:
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post/detail.html", {"post": post})
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

def post_detail(request, year, month, day, post):
    """
    Возвращает информацию об 1 записи по его id
    :param request:
    :param post_id:
    :return:
    """
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish_date__year=year, publish_date__month=month, publish_date__day=day)
    return render(request, "blog/post/detail.html", {"post": post})
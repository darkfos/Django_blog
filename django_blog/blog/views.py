from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

# Create your views here.
def post_list(request):
    """
    Выдаёт все записи из таблицы Post. С модификатором Published
    :param request:
    :return:
    """
    all_posts = Post.published.all()
    return render(request, "blog/post/list.html", context=all_posts)

def post_detail(request, post_id: int):
    try:
        post = Post.published.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("No Post found")
    return render(request, "blog/post/detail.html", context=post)
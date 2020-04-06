from pprint import pprint

import status as status
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    return render(request, "blog/Home.html")


def posts(request):
    queryAll = Post.objects
    if request.GET.get('id'):
        queryAll = queryAll.filter(id=request.GET.get('id'))

    id = queryAll.values()
    # paginator = Paginator(id)
    data = {
        'post': list(id),
    }
    return JsonResponse(data, safe=False)


# def single_post_details(request):
#     post = Post.objects.all()
#     context = {
#         'post': post
#     }
#     return JsonResponse(str(context), safe=False)


def recent(request):
    context = {
        'post': list(Post.objects.values().order_by('-id')[:3]),
    }
    return JsonResponse(context, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    import json
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        title = body_data['title']
        body = body_data['body']

        if title and body:

            data = Post.objects.create(
                title=title,
                body=body
            )
            return JsonResponse(str(data), safe=False)
        else:
            return JsonResponse('Failed!', safe=False)


@csrf_exempt
def post_delete(request, id):
    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
    return JsonResponse({'messsage': 'delete successfully'}, status=204)


@csrf_exempt
@require_http_methods(["POST"])
def post_update(request):
    # receving API data
    received_id = request.POST.get('id')
    received_title = request.POST.get('title')
    received_body = request.POST.get('body')
    if received_id:
        existing_post = Post.objects.get(id=received_id)
        # updating object
        existing_post.title = received_title
        existing_post.save()

        existing_post.body = received_body
        existing_post.save()

        # debug
        print(existing_post.title, existing_post.body)
        return JsonResponse({'message': 'updated!'}, status=200)


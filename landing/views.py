from multiprocessing import context
import pstats
import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
# http응답을 위한 추가 기능삽입
from landing.models import Post


def index(request):
    return render(request, "landing/index.html")

def temp_test(request):

    context = {
        "weather": "맑음",
        "temperature": 5,
        "weather_data" : {
            "weather" : "흐림",
            "temperature": 5
        },
    
        "football_players": [
            {
                "name":"손흥민",
                "team":"토트넘"
            },
            {
                "name":"리오넬 메시",
                "team":"파리셍제르망"
            },
            {
                "name":"이강인",
                "team":"마요르카"
            }
        ]       
    }
                
    return render(request, "landing/temptest.html",context)## 컨텍스트를 리턴해주는거 까먹지 말자

def post_create(request):
    if request.method == "GET":
        # 꼭 대문자로 써야함
        return render(request, "landing/create.html")##urls.py에 연결하기 위함
    elif request.method == "POST":
        # 꼭 대문자로 써야함
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        new_post.save()
        # print(request.POST["title"])    
        # print(request.POST["content"])
        return HttpResponseRedirect("/landing/create/")
        # http응답을 요청하는 것//요청->응답(HTML을 달라(get) ->포스트 요청-> 계속적으로 로테이션이 돌아감))



def post_read_all(request):
    post_list = Post.objects.all()
    for post in post_list:
        print(post.content)
    context = {
        "posts": post_list##전부다 하는거
    }
    return render(request, "landing/read-all.html", context)


def post_read(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post":post##하나만
       
    }

    # print(post_id)
    return render(request, "landing/read.html", context)



        # render(request, "landing/create.html")

def post_update(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post":post
        }
        # 꼭 대문자로 써야함
        return render(request, "landing/update.html", context)
    elif request.method == "POST":
        # 꼭 대문자로 써야함
        target_post = Post.objects.get(id=post_id)
        target_post.title = request.POST["title"]
        target_post.content = request.POST["content"]
        target_post.save()


        # print(request.POST["title"])    
        # print(request.POST["content"])
        return redirect("landing:read", post_id)
        # http응답을 요청하는 것//요청->응답(HTML을 달라(get) ->포스트 요청-> 계속적으로 로테이션이 돌아감))


def post_delete(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post":post
        }
        return render(request, "landing/delete.html", context)
    elif request.method == "POST":
        target_post = Post.objects.get(id=post_id)
        target_post.delete()

def index(request):
    return render(request, "index.html")

def post_create(request):
        if request.method == "GET":
            return render(request, "landing/create.html")
        elif request.method == "POST":
        # print(request.POST["title"])
        # print(request.POST["content"])
            if request.FILES["image"]:
                print(request.FILES["image"])

            new_post = Post()
            new_post.title = request.POST["title"]
            new_post.content = request.POST["content"]
            if request.FILES["image"]:
                new_post.head_image = request.FILES["image"]

        new_post.save()

        # print(request.POST["title"])
        # print(request.POST["content"])
        # return HttpResponseRedirect(reverse("landing:read_all"))

        return redirect("landing:read_all")












# def create_post_page(request):
#     dummy_post_data = [
#         {
#             "title": "Title 1",
#             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ante mauris, eleifend id felis vitae, feugiat volutpat ex. Curabitur vehicula, leo ac aliquet aliquet, nibh lectus accumsan tortor, non bibendum mi arcu quis orci. Proin pellentesque sodales lectus, quis pulvinar odio commodo elementum. Sed erat nulla, accumsan a interdum eu, vehicula sed quam. Suspendisse in posuere libero. Proin ut nunc ac ante fermentum pretium ut non erat. Cras rutrum iaculis aliquet. Cras tincidunt feugiat nibh ut imperdiet.",
#         },
#         {
#             "title": "Title 2",
#             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ante mauris, eleifend id felis vitae, feugiat volutpat ex. Curabitur vehicula, leo ac aliquet aliquet, nibh lectus accumsan tortor, non bibendum mi arcu quis orci. Proin pellentesque sodales lectus, quis pulvinar odio commodo elementum. Sed erat nulla, accumsan a interdum eu, vehicula sed quam. Suspendisse in posuere libero. Proin ut nunc ac ante fermentum pretium ut non erat. Cras rutrum iaculis aliquet. Cras tincidunt feugiat nibh ut imperdiet.",
#         },
#         {
#             "title": "Title 3",
#             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ante mauris, eleifend id felis vitae, feugiat volutpat ex. Curabitur vehicula, leo ac aliquet aliquet, nibh lectus accumsan tortor, non bibendum mi arcu quis orci. Proin pellentesque sodales lectus, quis pulvinar odio commodo elementum. Sed erat nulla, accumsan a interdum eu, vehicula sed quam. Suspendisse in posuere libero. Proin ut nunc ac ante fermentum pretium ut non erat. Cras rutrum iaculis aliquet. Cras tincidunt feugiat nibh ut imperdiet.",
#         },
#         {
#             "title": "Title 4",
#             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ante mauris, eleifend id felis vitae, feugiat volutpat ex. Curabitur vehicula, leo ac aliquet aliquet, nibh lectus accumsan tortor, non bibendum mi arcu quis orci. Proin pellentesque sodales lectus, quis pulvinar odio commodo elementum. Sed erat nulla, accumsan a interdum eu, vehicula sed quam. Suspendisse in posuere libero. Proin ut nunc ac ante fermentum pretium ut non erat. Cras rutrum iaculis aliquet. Cras tincidunt feugiat nibh ut imperdiet.",
#         }
#     ]


#     new_post = Post()
#     random.shuffle(dummy_post_data)
#     post_data = dummy_post_data[0]
#     new_post.title = post_data["title"]
#     new_post.content = post_data["content"]
#     new_post.save()

#     return render(request, "landing/create.html")


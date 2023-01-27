from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from .models import Tweet
from .forms import TweetForm
from.serializers import TweetSerializer

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request, "pages/home.html", context = {}, status = 200)

def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data = request.POST or None)
    if serializer.is_valid():
        obj = serializer.save(user = request.user)
        next_url = request.POST.get("next") or None
        if next_url != None:
            return redirect(next_url)
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse({}, status = 400)

#/tweets
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)

#/tweets/{id}
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        #"image_path": obj.image.url,
    }
    status = 200

    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
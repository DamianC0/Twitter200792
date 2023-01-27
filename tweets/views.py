from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request, "pages/home.html", context = {}, status = 200)

#/create-tweet
@api_view(['POST'])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save(user = request.user)
        next_url = request.POST.get("next") or None
        if next_url != None:
            return redirect(next_url)
        return Response(serializer.data, status = 201)
    return Response({}, status = 400)

#/tweets
@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many = True)
    return Response(serializer.data)

#/tweets/{id}
@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id = tweet_id)
    if not qs.exists():
        return Response({}, status = 404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status = 200)
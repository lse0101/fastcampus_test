from django.shortcuts import render
from user.serializers import UserSerializer
from user.models import User

from django.shortcuts import render
from django.utils import timezone
from order.models import Shop,Menu,Order,Orderfood
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def user(request):
  if request.method == 'GET':
    user = User.objects.all()
    return render(request, 'user/user_list.html', {'user_list': user})
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def login(request):
  if request.method == 'POST':
    try:
      name = request.POST['name']
      request.session['user_id'] = User.objects.all().get(user_name=name).id
      print(request.session['user_id'])
      return render(request, 'user/success.html')
    except:
      return render(request, 'user/fail.html')
  elif request.method == 'GET':
    return render(request, 'user/login.html')


from django.http import HttpResponse
from django.template import loader

def index(request):
  name = request.GET.get("name",None)
  message = request.GET.get("message",None)
  return HttpResponse(f"<title>Hello</title><h1>{name}! {message}!</h1>")
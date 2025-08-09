from django.shortcuts import render
from django.views import View
# Create your views here.

from django_eventstream import send_event



class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')
    
    
class CheckNewUser(View):
    def post(self, request):
        send_event('new_user', {'message': 'New user connected.'})
        return render(request, 'base.html')
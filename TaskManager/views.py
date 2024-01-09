from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required


class IndexView(View):
    @staticmethod
    @login_required
    def get(request):
        return True

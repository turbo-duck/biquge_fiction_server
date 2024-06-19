from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.views import generic

from .models import FictionList, ChapterList, ChapterDetailList
import json
import re


def index(request):
    data_list = FictionList.objects.all()[:12]
    context = {
        "data_list": data_list,
    }
    return render(request, "fiction/index.html", context)


def detail(request, fiction_code):
    fiction_data = get_object_or_404(FictionList, fiction_code=fiction_code)
    chapter_list = get_list_or_404(ChapterList.objects.order_by('chapter_order'), fiction_code=fiction_code)
    context = {
        "fiction_code": fiction_code,
        "fiction_data": fiction_data,
        "chapter_list": chapter_list,
    }
    return render(request, "fiction/detail.html", context)


def chapter_detail(request, chapter_code):
    chapter_info = get_object_or_404(ChapterList, chapter_code=chapter_code)
    chapter_data = get_object_or_404(ChapterDetailList, chapter_code=chapter_code)
    chapter_data_list = json.loads(chapter_data.chapter_content)
    context = {
        "chapter_info": chapter_info,
        "chapter_data_list": chapter_data_list,
    }
    return render(request, "fiction/chapter_detail.html", context)


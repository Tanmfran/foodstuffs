from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import FoodItems


def index(request):
    all_food_items = FoodItems.objects.order_by('item_cost')[:5]
    context = {
        'all_food_items': all_food_items,
    }
    return render(request, 'polls/index.html', context)

def detail(request, food_id):
    food = get_object_or_404(FoodItems, id=food_id)
    return render(request, 'polls/details.html', {'food': food})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voti"
                        "ng on question %s." % question_id)
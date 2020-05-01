from unicodedata import decimal
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import FoodItems
from django.http import JsonResponse


class IndexView(generic.ListView):
    template_name = 'foods/index.html'
    context_object_name = 'all_food_items'

    def get_queryset(self):
        return FoodItems.objects.order_by('id')[:5]


class DetailView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        items = FoodItems.objects.all()
        all_food_items = []
        for item in items:
            dictionary_record = {}
            dictionary_record['id'] = item.id
            dictionary_record['item_name'] = item.item_name
            dictionary_record['item_cost'] = str(item.item_cost)
            dictionary_record['item_url'] = item.item_url
            all_food_items.append(dictionary_record)
        return Response(all_food_items, content_type="application/json")

class FoodStorage(APIView):
    def post(self, request):
        return

class ResultsView(generic.DetailView):
    model = FoodItems
    template_name = 'foods/result.html'

class AddFoodItem(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        try:
            item_name = request.data.get('item_name')
            item_cost = request.data.get('item_cost')
            quantity = request.data.get('quantity')
            item_url = request.data.get('item_url')
        except:
            return Response('Error getting required fields')
        if not FoodItems.objects.filter(item_url=item_url,
                                        item_name=item_name,
                                        item_cost=item_cost,
                                        quantity=quantity).exists():
            food_record = FoodItems(item_url=item_url,
                                    item_name=item_name,
                                    item_cost=item_cost,
                                    quantity=quantity).save()
            return Response('Added to database', status=200)
        return Response('Already Exists', status=200)


def update_quantity(request, food_id):
    food = get_object_or_404(FoodItems, id=food_id)
    try:
        selected_choice = request.POST['quantity']
    except (KeyError, food.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'foods/detail.html', {
            'fooditems': food,
            'error_message': "You didn't select a quantity.",
        })
    else:
        food.quantity = selected_choice
        food.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        total_cost = '$' + str(decimal(food.quantity) * food.item_cost)
        return {
            'fooditems': food,
            'total_cost': total_cost,
        }

from django.shortcuts import render
from .models import StudentModel, MarksModel
from .serializers import StudentSerializer, MarksSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from django.urls import reverse
import stripe
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class studentapi(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    
class marksapi(viewsets.ModelViewSet):
    queryset = MarksModel.objects.all()
    serializer_class = MarksSerializer

def index(request):
    request.session['key1'] = 'data 1'
    print(request.session['key1'])
    p= StudentModel.objects.get(stid = 1)
    a = StudentSerializer(p)
    print(a.data)
    

    
    print(settings.STRIPE_PUBLIC_KEY)
    print(settings.STRIPE_PRIVATE_KEY)
    return render(request,'profile_maker/index.html')

def thanks(request):
    return render(request,'profile_maker/thanks.html')

@csrf_exempt
def checkout(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
            'price':'price_1IL4EwJQjYBO6aQ5LnYCznlX',
            'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('thanks'))+'?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= request.build_absolute_uri(reverse('index')),
    )
    return JsonResponse({
        'session_id':session.id,
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY
    })


@csrf_exempt
def my_webhook_view(request):
  endpoint_secret = 'whsec_...'
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)
  if event['type'] == 'checkout.session.completed':
      session = event['data']['object']
  
  return HttpResponse(status=200)

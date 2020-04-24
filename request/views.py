from django.shortcuts import render
from django.http import HttpResponse
import datetime
from request.forms import ProfileForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.conf import settings 
import stripe
from .models import Profile
stripe.api_key = settings.STRIPE_SECRET_KEY # new

class ProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = '/paiement/'

    def form_valid(self, form):
        result = super().form_valid(form)
        self.request.session['id'] = form.instance.id
        return result

class PaiementView(TemplateView):
    template_name = "paiement.html"

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3000,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        profile = Profile.objects.get(pk=request.session['id'])
        profile.paid = True
        profile.save()
        return render(request, 'charge.html')
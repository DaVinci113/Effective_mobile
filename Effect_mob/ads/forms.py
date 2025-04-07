from django import forms
from .models import Ad, ExchangeProposal


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = '__all__'


class CreateProposalForm(forms.ModelForm):

    class Meta:
        model = ExchangeProposal
        fields = '__all__'

from django import forms
from .models import Ad, ExchangeProposal


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        exclude = ('user',)


class CreateProposalForm(forms.ModelForm):

    class Meta:
        model = ExchangeProposal
        fields = '__all__'

from django import forms
from .models import Ad, ExchangeProposal


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        exclude = ('user',)


class CreateProposalForm(forms.ModelForm):

    class Meta:
        model = ExchangeProposal
        fields = ['ad_sender_id', 'comment']

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     self.fields['ad_sender_id'].queryset = Ad.objects.filter(user=user)
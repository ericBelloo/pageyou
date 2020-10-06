from django import forms

# models
from apps.account.models import Account

STATUS_ACCOUNT = [
    ('DESEMBOLSADA', 'DESEMBOLSADA'),
    ('CERRADA', 'CERRADA')
]


class CreateAccountForm(forms.ModelForm):
    amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'field-account'}), label='Monto', required=False)
    status = forms.ChoiceField(widget=forms.Select(attrs={'disabled': True}), choices=STATUS_ACCOUNT,
                               initial='DESEMBOLSADA', required=False)

    class Meta:
        model = Account
        fields = ('amount', )

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        number = float(amount)
        if 10000 < number < 100000:
            return amount
        else:
            raise forms.ValidationError('El monto no es valido')


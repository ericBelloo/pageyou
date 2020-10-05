
from django import forms

# models
from apps.account.models import Account


STATUS_ACCOUNT = [
    ('DESEMBOLSADA', 'DESEMBOLSADA'),
    ('CERRADA', 'CERRADA')
]


class CreateAccountForm(forms.ModelForm):
    number_payments = forms.CharField(widget=forms.TextInput(attrs={'class': 'field-account'}))

    class Meta:
        model = Account
        fields = ('status', 'amount', 'group')
        widget = {
            'status': forms.Select(
                choices=STATUS_ACCOUNT, attrs={'disabled': True}),
            'amount': forms.TextInput(
                attrs={'required': True, 'class': 'field-account', }
            )
        }
        labels = {
            'status': 'Estado',
            'amount': 'Prestamo total*',
            'number_payments': 'Numero de pagos*'
        }

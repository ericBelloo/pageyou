from django.http import JsonResponse
from rest_framework.views import APIView
from apps.account.models import Calendar
from datetime import datetime
# models
from apps.account.api.serializers import TransactionsSerializer


class SaveTransaction(APIView):

    def post(self, request):
        try:
            account_id = request.data.get('account')
            calendar_id = request.data.get('calendar')
            payment_number = request.data.get('payment_number')
            calendar_amount = request.data.get('amount')
            date = request.data.get('date')

            calendar = Calendar.objects.get(id=calendar_id, account_id=account_id, payment_number=payment_number)
            calendar.amount = float(calendar.amount) - float(calendar_amount)
            if calendar.payment_date <= datetime.strptime(date, '%Y-%m-%d'):
                if calendar.amount == 0:
                    calendar.status = 'PAGADO'
                else:
                    calendar.status = 'PARCIAL'
            else:
                calendar.status = 'ATRAZADO'
            calendar.save()
        except Exception as err:
            raise err
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            """ Update calendar """
            context = {
                'success': True,
                'data': ''
            }
        else:
            context = {
                'success': False,
                'data': serializer.errors
            }
        return JsonResponse(context, safe=False)

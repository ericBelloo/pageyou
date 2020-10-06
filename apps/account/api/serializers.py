from rest_framework import serializers

# models
from apps.account.models import Transactions


class TransactionsSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=True, allow_null=False)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    account = serializers.IntegerField(required=True, allow_null=False)

    def create(self, validated_data):
        return Transactions.objects.create(**validated_data)

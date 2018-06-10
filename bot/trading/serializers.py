from rest_framework import serializers


class TradingSerializer(serializers.Serializer):

    count = serializers.IntegerField(
        required=False,
        default = 100,        
        min_value = 1,
        max_value = 1000
    )
    before = serializers.CharField(required=False)
    after = serializers.CharField(required=False)
    product_code = serializers.ChoiseField(
        required=False,
        choices = ['BTC_JPY']
    )

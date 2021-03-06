from rest_framework import serializers


class TradeSerializer(serializers.Serializer):

    count = serializers.IntegerField(
        required=False,
        default=100,
        min_value=1,
        max_value=1000
    )
    before = serializers.CharField(required=False)
    after = serializers.CharField(required=False)
    product_code = serializers.ChoiceField(
        required=False,
        choices=['BTC_JPY', 'FX_BTC_JPY', 'ETH_BTC']
    )
    from_date = serializers.DateTimeField(required=False)

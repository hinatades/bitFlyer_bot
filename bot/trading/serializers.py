from rest_frameworks import serializers

class TradingSerializer(serializers.Serializer):

    count = serializers.IntegerField(
        required=False,
        default = 100,        
        min_value = 1,
        max_value = 1000
    )
    before = serializers.CharField(reqired=False)
    after = serializers.CharField(required=False)

from django.db import models


class TICKs(models.Model):

    timestamp = models.DateField()
    product_code = models.CharField(max_length=50)
    tick_id = models.CharField(max_length=50)
    best_ask = models.CharField(max_length=50)
    best_ask_size = models.CharField(max_length=50)
    best_bid = models.CharField(max_length=50)
    best_bid_size = models.CharField(max_length=50)
    total_ask_depth = models.CharField(max_length=50)
    total_bid_depth = models.CharField(max_length=50)
    ltp = models.CharField(max_length=50)
    volume = models.SmallIntegerField()
    volume_by_product = models.CharField(max_length=50)
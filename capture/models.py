from django.db import models


class ShangHaiFutures(models.Model):
    """ 上海期货 """
    bourse_name = models.CharField(max_length=255, verbose_name='交易所名称')

    code = models.CharField(max_length=255, verbose_name='代码')
    name = models.CharField(max_length=255, verbose_name='名称')
    newest_price = models.CharField(max_length=255, verbose_name='最新价')
    amount_increase_price = models.CharField(max_length=255, verbose_name='涨跌额')
    amount_increase = models.CharField(max_length=255, verbose_name='涨跌幅')
    opening_price = models.CharField(max_length=255, verbose_name='开盘价')
    top_price = models.CharField(max_length=255, verbose_name='最高价')
    bottom_price = models.CharField(max_length=255, verbose_name='最低价')
    yesterday_price = models.CharField(max_length=255, verbose_name='昨收价')
    update_time = models.CharField(max_length=255, verbose_name='更新时间')

    insert_date = models.DateTimeField(auto_now=True,  verbose_name='插入对象的时间')


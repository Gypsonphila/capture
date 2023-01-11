from django.db import models


class ShangHaiFutures(models.Model):
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

    class Meta:
        db_table = 'shanghai_futures_table'
        verbose_name = verbose_name_plural = '上海期货交易所'

    def __str__(self):
        return self.name


class ZhengZhouFutures(models.Model):
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

    class Meta:
        db_table = 'zhengzhou_futures_table'
        verbose_name = verbose_name_plural = '郑州商品交易所'

    def __str__(self):
        return self.name


class DaLianFutures(models.Model):
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

    class Meta:
        db_table = 'dalian_futures_table'
        verbose_name = verbose_name_plural = '大连商品交易所'

    def __str__(self):
        return self.name


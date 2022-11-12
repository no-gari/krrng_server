from django.db import models
from api.user.models import User


class RecentSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    keyword = models.CharField(max_length=512, verbose_name='검색어')

    class Meta:
        verbose_name = '최근 검색어'
        verbose_name_plural = verbose_name


class TrendingSearch(models.Model):
    keyword = models.CharField(max_length=512, verbose_name='검색어')
    ranking = models.IntegerField(verbose_name='순위', help_text='숫자가 적을수록 상위에 노출됩니다.', default=0)

    class Meta:
        verbose_name = '인기 검색어'
        verbose_name_plural = verbose_name

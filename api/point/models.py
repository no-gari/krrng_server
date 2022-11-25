from django.db import models
from api.user.models import User


class PointLog(models.Model):
    user = models.ForeignKey(User, verbose_name='사용자', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='제목')
    reason = models.CharField(max_length=1024, verbose_name='지급, 회수 사유')
    amount = models.IntegerField(verbose_name='지급, 회수 금액', default=0, help_text='지급 시 양수를, 회수 시 음수를 입력해 주세요.')
    created_at = models.DateField(verbose_name='날짜', auto_now_add=True)

    class Meta:
        verbose_name = '포인트 로그'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.profile_set.last().nickname + '의 포인트 로그'

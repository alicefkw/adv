from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

class Posts(models.Model):
    title = models.CharField("Título", max_length = 255)
    resumo = models.CharField("Resumo", max_length=255, editable = False)
    content = models.TextField()
    #summary = models.CharField("Resumo", editable = False, max_length = 25, default = summary())
    #author = models.ForeignKey(User, max_length = 100, on_delete = models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, max_length = 100, on_delete = models.PROTECT)
    created_at = models.DateField("Criado em", auto_now_add = True)

    def __str__(self):
        return self.resumo()
    
    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Posts'
    
    def resumo(self):
        return f"{self.content[0:15]}..."
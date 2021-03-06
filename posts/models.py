from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from adm.manages import PostManager

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo do Post')
    exerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoria')
    foto = models.ImageField(upload_to='post_imagens/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    objects = PostManager()

    def foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            print("a url da foto é:", self.foto.url)
            return self.foto.url
        else:
            return "media/gw.jpg"



    def __str__(self):
        return self.titulo_post
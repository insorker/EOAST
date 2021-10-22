from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Picture(models.Model):
    shot = models.ImageField(upload_to='article')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shot.name


class Post(models.Model):
    # 标题
    title = models.CharField(verbose_name='标题', max_length=50)
    # 作者
    author = models.CharField(verbose_name='作者', max_length=50)
    # 摘要
    excerpt = models.CharField(verbose_name='摘要', max_length=200, blank=True)
    # 正文
    body = models.TextField(verbose_name='正文')
    # 时间
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modified_time = models.DateTimeField(verbose_name='修改时间')
    # 分类与标签
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 头图链接
    picture = models.ForeignKey(Picture, verbose_name='图片', on_delete=models.SET_NULL, null=True)
    # 浏览量
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Notice(models.Model):
    # 标题
    title = models.CharField(verbose_name='标题', max_length=50)
    # 正文
    body = models.TextField(verbose_name='正文')
    # 时间
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modified_time = models.DateTimeField(verbose_name='修改时间')
    # 图片链接
    picture = models.ForeignKey(Picture, verbose_name='图片', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

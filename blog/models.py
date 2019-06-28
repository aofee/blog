from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="名称")
    url = models.CharField(max_length=100, verbose_name="唯一URL")
    blog_num = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model) :
    name = models.CharField(max_length=100, verbose_name="名称")
    url = models.CharField(max_length=100, verbose_name="唯一URL")
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    url = models.CharField(max_length=100, verbose_name="唯一URL")
    descript = models.CharField(null=True, max_length=1000, verbose_name="描述")
    content = MDTextField(null=True, verbose_name="内容")
    views = models.IntegerField(default=0, verbose_name="阅读量")
    category = models.ManyToManyField(Category, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']







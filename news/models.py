from django.db import models


class ContactModel(models.Model):
    phone_number = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class CategoryModel(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class NewsModel(models.Model):
    title = models.CharField(max_length=180)
    cover = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField(CategoryModel, related_name='news')
    description = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

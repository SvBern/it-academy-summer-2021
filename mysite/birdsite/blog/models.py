from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:bird_list_by_category',
                       args=[self.slug])


class Bird(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='birds',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='birds/%Y/%m/%d',
                              blank=True)
    sound = models.FileField(upload_to='birds/%Y/%m/%d',
                             blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = ('slug',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:bird_detail',
                       args=[self.slug])

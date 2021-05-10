from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, primary_key=True)
    description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE,
    #                            related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    # tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + 'slug'
        super().save()


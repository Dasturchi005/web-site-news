from django.db import models
from django.utils.text import slugify




class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)
    


class TagModel(BaseModel):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name




class NewsModel(BaseModel):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='image_news/')
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    views = models.IntegerField(default=0)
    tag = models.ManyToManyField(TagModel, blank=True)



    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)
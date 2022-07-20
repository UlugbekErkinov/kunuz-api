from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='news/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='news', null =True, blank=True)
        
    is_main = models.BooleanField(default=False)
    is_editor_choice = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_investigation = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_videonews = models.BooleanField(default=False)
    is_photonews = models.BooleanField(default=False)
    is_adviced = models.BooleanField(default=False)
    def __str__(self):
        return self.title

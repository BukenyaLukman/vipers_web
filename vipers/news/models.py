from django.db import models



class Tags(models.Model):
    tag = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag



# New Category choices such as news articles, match reports,transfer news,

CATEGORY_CHOICES = (
    ('News', 'News'),
    ('Match Report', 'Match Report'),
    ('Transfer News', 'Transfer News'),
)
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    views = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.category}"



    

from django.db import models


class Blog(models.Model):
    class Meta:
        ordering = ['-date_created']

    title = models.CharField(max_length=254)
    text = models.TextField()
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title

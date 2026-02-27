from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tag-detail", kwargs={"pk": self.pk})

class Wallpaper(models.Model):
    image_url = models.CharField(max_length=500)
    source = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"Wallpaper by {self.creator} from {self.source}"

    def get_absolute_url(self):
        return reverse('wallpaper-detail', kwargs={'pk': self.id})

CONTEXTS = (
    ('H', 'Home Screen'),
    ('L', 'Lock Screen'),
    ('D', 'Desktop'),
)

class UseLog(models.Model):
    date = models.DateField("Date Used")
    context = models.CharField(
        verbose_name="Context:",
        max_length=1,
        choices=CONTEXTS,
        default=CONTEXTS[0][0]
    )
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE, related_name='use_logs')

    def __str__(self):
        return f"{self.get_context_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
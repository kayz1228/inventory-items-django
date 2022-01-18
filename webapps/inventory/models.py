from django.db import models

# Data Models for Item.
class Item(models.Model):
    name = models.CharField(max_length=50)
    article_no = models.IntegerField(default=None)
    stock = models.IntegerField(default=None)

    def __str__(self):
        return 'id:' + str(self.id) + ', article number:' + str(self.article_no) + ', name:' + str(self.name) + ', stock=' + str(self.stock)
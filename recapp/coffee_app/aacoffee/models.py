from django.db import models


class Coffee(models.Model):
    # id  # int (should be included by default)
    name = models.CharField(max_length=200, blank=False)  # varchar
    year = models.IntegerField(blank=False)  # int
    caffine_content = models.FloatField(blank=False)  # float
    caffine_percentage = models.FloatField(blank=False)  # float
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    # id  # int (should be included by default)
    title = models.CharField(max_length=200, blank=False)  # varchar
    # int foreign key to Coffee
    coffee = models.ForeignKey('Coffee', on_delete=models.CASCADE)
    text = models.TextField(blank=False)  # longtext
    rating = models.FloatField(blank=False)  # float
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# # Abstract Class to be applied for all models
# class TimeStampMixin(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

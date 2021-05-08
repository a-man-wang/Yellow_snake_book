from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
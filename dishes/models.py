from django.db import models

class Dishes(models.Model):
    name = models.CharField(max_length = 50, help_text= 'Название блюда')
    shelf_life_in_days = models.IntegerField(help_text = 'Срок годности в днях')
    category = models.ForeignKey('Category', on_delete = models.CASCADE, verbose_name = 'Категории' )
    restaraunt = models.ForeignKey('Restaraunt', on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Рестораны/кафе/магащины')
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'Название категории')
    
    def __str__(self):
        return self.name

class Restaraunt(models.Model):
    name = models.CharField(max_length = 20, help_text = 'Наименование ресторна/кафе/магазина' )
    
    def __str__(self):
        return self.name
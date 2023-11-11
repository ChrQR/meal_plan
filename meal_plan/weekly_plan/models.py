from django.db import models
import random

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)

class Weekly(models.Model):

    def populateWeek():
        try:
            meal_list = []
            while(len(meal_list) < 8):
                random_meal_id = random.randint(0, Meal.objects.count() - 1)
                random_meal = Meal.objects.all()[random_meal_id]
                meal_list.append(random_meal)
            return meal_list
        except:
            return False
    
    weekly_plan = populateWeek()
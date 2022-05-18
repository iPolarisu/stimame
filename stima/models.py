from django.db import models

# Create your models here.

class Steamapp(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=255, blank=True)
    release_date = models.DateField(blank=True, null=True)
    developer = models.TextField(max_length=255, blank=True, null=True)
    platforms = models.TextField(max_length=255, blank=True, null=True)
    categories = models.TextField(max_length=1000, blank=True, null=True)
    genres = models.TextField(max_length=255, blank=True, null=True)
    achievements = models.IntegerField(blank=True, null=True)
    positive_ratings = models.IntegerField(blank=True, null=True)
    negative_ratings = models.IntegerField(blank=True, null=True)
    average_playtime = models.FloatField(blank=True, null=True)
    median_playtime = models.FloatField(blank=True, null=True)
    owners = models.TextField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    header_image = models.TextField(max_length=255, blank=True, null=True)
    background = models.TextField(max_length=255, blank=True, null=True)
    detailed_description = models.TextField(max_length=100000, blank=True, null=True)
    about_the_game = models.TextField(max_length=100000, blank=True, null=True)
    
    def averageHours(self):
        return round(self.average_playtime/60, 1)

    def medianHours(self):
        return round(self.median_playtime/60, 1)
    
    def priceStr(self):
        if self.price == 0:
            return "0 - F2P"
        else:
            return self.price

    def rating(self):
        return round(self.positive_ratings/(self.positive_ratings + self.negative_ratings), 2)

    def ratingStr(self):
        return int(self.rating()*100)
    
    def stimaScore(self):
        rating = self.rating()
        price = self.price
        if price == 0:
            return round((self.averageHours())*rating, 2)
        else:
            return round((self.averageHours()/self.price)*rating, 2)
    
    class Meta:
        managed = False
        db_table = 'steamapp'
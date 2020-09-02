from django.db import models
from django.urls import reverse
# Create your models here.

# old way
# class jointTable(models.Model):
#     finch=models.ForeignKey
#     feeding=models.ForeignKey


class Toy (models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Finch(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    # this function is useful for anytime needs printing such as if it is called from forgeign key
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return '/finches/' + str(self.id)
        return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # add foreign key
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def __str__(self):
        # this displays the words
        return f'{self.get_meal_display()} on {self.date}'
        # this only display letters
        # return f'{self.meal} on {self.date}'

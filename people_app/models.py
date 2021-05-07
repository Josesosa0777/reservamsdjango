from django.db import models

# Create your models here.


class PeopleList(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    area = models.CharField(max_length=50)
    leader = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "/" + str(self.category) + "/" + str(self.email) + "/" + str(self.area) + "/" + str(self.leader)

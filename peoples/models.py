from django.db import models

# Create your models here.
class Team(models.Model):
    TEAM_CHOICES = (
        ('TI','TI'),
        ('DD','Design'),
        ('EVALUATION','Evaluation'),
        ('SECRATARY','Secreatary'),
    )
    name = models.CharField(choices=TEAM_CHOICES, max_length=20, default='TI')
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, unique=True)
    number = models.IntegerField(default=0)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


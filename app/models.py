from django.db import models

# Create your models here.

class Problems(models.Model):

    sl = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    mark = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Submissions(models.Model):

    id = models.AutoField(primary_key=True)
    player1 = models.CharField(max_length=200)
    player2 = models.CharField(max_length=200)
    question = models.ForeignKey(Problems,on_delete=models.CASCADE)
    code = models.TextField(null=True,blank=True)

    def __str__(self):

        return self.player1 + " & " +self.player2
    
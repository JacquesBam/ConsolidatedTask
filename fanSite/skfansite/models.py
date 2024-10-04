from django.db import models


# Create your models here.
class Author(models.Model):
<<<<<<< HEAD
=======
    '''Parent class to the Author class

    :param models.Model:
    '''
>>>>>>> docs
    author_name = models.CharField(max_length=50)
    dob = models.DateField('date of birth')
    author_id = models.IntegerField(primary_key=True)
    author_bio = models.CharField(max_length=1000)
    author_pic = models.ImageField(default='fallback.jpg', blank=True)


class Book(models.Model):
<<<<<<< HEAD
=======
    '''Parent class to the Book class

    :param models.Model:
    '''
>>>>>>> docs
    title = models.CharField(max_length=50)
    pub_date = models.DateField('date published')
    t_nail = models.ImageField(default='fallback.jpg', blank=True)
    b_id = models.IntegerField(unique=True, primary_key=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    blurb = models.CharField(max_length=1000, default="Lorem Ipsum")
    pages = models.IntegerField(default=0)

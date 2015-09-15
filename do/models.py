from django.db import models

class Category(models.Model):
    """ Defines the categories of possible todo items. """
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class User(models.Model):
    """ Defines a database user. """
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField()

    def __str__(self):
        return "%s (%s)" % (self.username, self.email)


class DoItem(models.Model):
    """ Defines a todo item for the database."""
    subject = models.CharField(max_length=1024)
    assignee = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_due = models.DateTimeField('date due')

    def __str__(self):
        return "%s [%s]" % (self.subject, str(self.category))

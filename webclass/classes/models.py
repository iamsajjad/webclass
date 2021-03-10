from django.db import models

# Create your models here.


class Comments(models.Model):

    primary      = models.AutoField(primary_key=True)
    owner        = models.CharField(max_length=300, default='unknown')
    text         = models.TextField(max_length=2000, default='unknown')
    date         = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.primary

    class Meta:
        ordering = ('primary',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.primary,
            self.text))


class Posts(models.Model):

    primary      = models.AutoField(primary_key=True)
    owner        = models.CharField(max_length=300, default='unknown')
    title        = models.CharField(max_length=300, default='unknown')
    text         = models.TextField(max_length=4000, default='unknown')
    hasFile      = models.BooleanField(default=False)
    postFile     = models.FileField(upload_to='uploads/')
    comments     = models.ManyToManyField(Comments)
    date         = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.primary

    class Meta:
        ordering = ('primary',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.primary,
            self.title))


class Classes(models.Model):

    primary      = models.AutoField(primary_key=True)
    owner        = models.CharField(max_length=300, default='unknown')
    name         = models.CharField(max_length=300, default='unknown')
    stage        = models.CharField(max_length=300, default='unknown')
    posts        = models.ManyToManyField(Posts)
    date         = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.primary

    class Meta:
        ordering = ('primary',)
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.primary,
            self.name))

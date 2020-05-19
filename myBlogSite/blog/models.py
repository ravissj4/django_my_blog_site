from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
	# each author will be connected to a User 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # means there will be a list of comments somewhere, some of them will 
    # have approved_comments = True and some = False
    # so, only grab those comments which are approved_comments = True and 
    # we can show them along with the post.
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
        
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
	# each commend will be connected to a blog post object
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
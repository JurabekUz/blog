from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(blank=True,null=True,max_length=200)
    fb_url = models.CharField(blank=True,null=True,max_length=200)
    twitter_url = models.CharField(blank=True,null=True,max_length=200)
    insta_url = models.CharField(blank=True,null=True,max_length=200)
    telegram_url = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=200, default='may title tag')
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100)
    snippet = models.CharField(max_length=255, default='Click link above to read blog post...')
    likes = models.ManyToManyField(User, related_name='blog_post')

    #postga tegishli like lar soni
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.auther)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')


class Comment(models.Model):  # comment Post modeliga bog'lanadi
    post = models.ForeignKey(Post,  # Post ga tegishli commentlar ko'p bo'lganligi uchun ForeignKey;
                              related_name='comment',  # Post modeldan turib commentga access olish uchun (post.comment)
                              on_delete=models.CASCADE # Agar Post o'chirlsa unga tegishli commentlar ham o'chishi uchun
                             )
    name = models.CharField(max_length=100) #comment egasining ismi. Anonim user ham comment qila oladi
    body = models.TextField() # izoh matni
    date_added = models.DateTimeField(auto_now_add=True) #izoh yozilgan vatqi o'z-o'zidan qo'shiladi

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



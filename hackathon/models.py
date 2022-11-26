from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=100, blank=True, null=True)
    point = models.IntegerField(default=0)
    avatar = models.CharField(default="/static/home/images/author.jpg", max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField( max_length=30, blank=True, null=True)
    create_date = models.DateField( auto_now_add=True, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    bio = RichTextUploadingField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_enable = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        db_table = 'UserProfile'


class GarbageType(models.TextChoices):
    RECYCLABLE = "RECYCLABLE"
    ORGANIC = "ORGANIC"
    HAZARDOUS = "HAZARDOUS"
    SOLID = "SOLID"
    LIQUID = "LIQUID"


class Garbage(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=GarbageType.choices)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    point = models.IntegerField(default=0)
    is_enable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Garbage'

class Blog(models.Model):
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
	) 
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey('Category', models.DO_NOTHING, null=True)
	title = models.CharField(max_length=100)
	photo = models.CharField(max_length=250, blank=True, null=True)
	description = RichTextUploadingField(blank=True, null=True)
	content = RichTextUploadingField(blank=True, null=True)
	status = models.CharField( max_length=1, choices=STATUS_CHOICES)
	views = models.PositiveIntegerField(default=0)
	slug = models.SlugField(unique=True, max_length=250, null=True, blank=True)
	create_date = models.DateField(auto_now_add=True, blank=True, null=True)
	edit_date = models.DateTimeField(blank=True, null=True) 
	is_enable = models.BooleanField(default=True, blank=True, null=True)
	note = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		slug = original_slug = slugify(self.title)
		i=0
		while Blog.objects.filter(slug=slug).exists():
			temp = Blog.objects.filter(slug=slug)
			if temp[0].slug == self.slug:
				break
			else:
				slug = '{}-{}'.format(original_slug, i)
				i += 1
		self.slug = slug
		super(Blog, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-create_date']
		managed = True
		db_table = 'Blog'

class Contact(models.Model):
	STATUS_CHOICES = (
		('c', 'Create'),
		('i', 'In Progress'),
		('d', 'Done')
	) 
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250)
	fullname = models.CharField(max_length=150)
	email = models.EmailField(max_length=150)
	message = models.TextField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='c')
	create_date = models.DateField(auto_now_add=True, blank=True, null=True)
	edit_date = models.DateTimeField(auto_now=True, blank=True, null=True) 
	note = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.message[:20]

	class Meta:
		managed = True
		db_table = 'Contact'

class Product(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        managed = True
        db_table = 'Product'

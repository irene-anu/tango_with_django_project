from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)  #This key can be used as primary key as it is unique throughout the database
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

# You can also specify additional attributes for each field, such as stating a default
# value with the syntax default='value', and whether the value for a field can be blank
# (or NULL¹¹) (null=True) or not (null=False)

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)  # this is a foreign key, help create one to many relationship with Category 
    # Cascade instructs Django to delete the pages associated with category when category is deleted. 
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    def __str__(self):
        return self.title
    
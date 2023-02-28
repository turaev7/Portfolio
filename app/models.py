from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.DateField()
    photo = models.ImageField(upload_to='static/img', null=True, blank=True)
    email = models.CharField(max_length=30)
    profile = models.CharField( max_length=50)
    phone = models.CharField(max_length=13)
    about = models.TextField()
    service_1 = models.CharField(max_length=15)
    service_1_info = models.CharField(max_length=200, null=True, blank=True)
    service_2 = models.CharField(max_length=15)
    service_2_info = models.CharField(max_length=200, null=True, blank=True) 
    service_3 = models.CharField(max_length=15)
    service_3_info = models.CharField(max_length=200, null=True, blank=True)




# for statisic - 1) work 2) projects 3) year experience 4) work time
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "My_info"
        verbose_name_plural = "My infos"

class Portfolio(models.Model):
    p_name = models.CharField(max_length=20)
    p_photo = models.ImageField(upload_to='static/img')
    p_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = "My_Portfolio"
        verbose_name_plural = "My_Portfolios"




class Total(models.Model):
    works = models.IntegerField()
    month_experience = models.IntegerField()
    total_clients = models.IntegerField()
    awards = models.IntegerField()


    def __str__(self):
        return f"{self.works}"

    class Meta:
        verbose_name = "Total"
        verbose_name_plural = "Totals"



class Blog(models.Model):
    blog_photo = models.ImageField(upload_to='static/img')
    blog_name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return f"{self.blog_name}"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

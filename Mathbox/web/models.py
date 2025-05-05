from django.db import models


CATEGORY = (
    ("1", "Kids"),
    ("2", "Students"),
    ("3", "Both")
)


class Faq(models.Model):
    question = models.CharField(max_length=270)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class CommmunityPost(models.Model):
    heading = models.CharField(max_length=270, blank=True, null=True)
    image = models.ImageField(upload_to="community_post/", blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class Exercises(models.Model):
    about = models.CharField(max_length=270)
    css = models.TextField(verbose_name="CSS Code")
    js = models.TextField(verbose_name="JavaScript Code")
    html = models.TextField(verbose_name="HTML Code")
    type = models.CharField(max_length=270, choices=CATEGORY)

    def __str__(self):
        return self.about
    

class Games(models.Model):
    name = models.CharField(max_length=270)
    image = models.ImageField(upload_to="game_images/")
    type = models.CharField(max_length=270, choices=CATEGORY)
    css = models.TextField(verbose_name="CSS Code")
    js = models.TextField(verbose_name="JavaScript Code")
    html = models.TextField(verbose_name="HTML Code")

    def __str__(self):
        return self.name


class Tools(models.Model):
    name = models.CharField(max_length=270)
    html = models.TextField(verbose_name="HTML code")
    css = models.TextField(verbose_name="CSS Code")
    js = models.TextField(verbose_name="JavaScript Code")

    def __str__(self):
        return self.name
    

class Kids(models.Model):
    title = models.CharField(max_length=270)
    content = models.TextField()
    item = models.CharField(max_length=270)

    def __str__(self):
        return self.title
    
class KidsPlay(models.Model):
    kids = models.ForeignKey('Kids', on_delete=models.CASCADE, related_name='plays')
    value = models.CharField(max_length=270, blank=True, null=True)
    link = models.CharField(max_length=270, blank=True, null=True)


class Student(models.Model):
    title = models.CharField(max_length=270)
    content = models.TextField()
    item = models.CharField(max_length=270)

    def __str__(self):
        return self.title
    
class StudentPlay(models.Model):
    kids = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='plays')
    value = models.CharField(max_length=270, blank=True, null=True)
    link = models.CharField(max_length=270, blank=True, null=True)
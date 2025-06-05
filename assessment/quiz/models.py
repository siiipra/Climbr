from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    student_class = models.CharField(max_length=20)
    subjects = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class TeachingPoint(models.Model):
    class_name = models.IntegerField()
    subject = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    text = models.TextField(verbose_name="Teaching Point Text")

    def __str__(self):
        return f"Class {self.class_name} - {self.subject} - {self.chapter}: {self.text[:50]}"

class QuestionBank(models.Model):
    BLOOMS_LEVELS = [
        ('R', 'Remembering'),
        ('U', 'Understanding'),
        ('A', 'Applying'),
        ('AN', 'Analyzing'),
        ('E', 'Evaluating'),
        ('C', 'Creating'),
    ]

    question_text = models.TextField(verbose_name="Question Text")
    question_image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    blooms_level = models.CharField(max_length=2, choices=BLOOMS_LEVELS)

    def __str__(self):
        return f"Q{self.id}: {self.question_text[:50]}"

class Choice(models.Model):
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='choice_images/', blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice {self.id} for Q{self.question.id}"

class TeachingPointQuestionMap(models.Model):
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    teaching_point = models.ForeignKey(TeachingPoint, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'teaching_point')

    def __str__(self):
        return f"Q{self.question.id} ↔ TP{self.teaching_point.id}"

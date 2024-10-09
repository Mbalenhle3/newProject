from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class SurveyQuestion(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text  # Use the correct field name


class Choice(models.Model):
    question = models.ForeignKey(SurveyQuestion, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Tracks the user who submitted the response
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text} - {self.choice.text}"
   

class PaymentProcedure(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='payment_procedures/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GymRule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='gym_rules/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GymNotice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class ReceiptSubmission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Link to the user submitting the receipt
    file = models.FileField(upload_to='receipts/')  # Field for file upload
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp for submission

    def __str__(self):
        return f"Receipt submitted by {self.user.username} on {self.submitted_at.strftime('%Y-%m-%d')}"


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    salary = models.IntegerField()  # Removed max_length
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMembershipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)  # Removed max_length
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.FullName

    
class MembershipPlan(models.Model):
    plan = models.CharField(max_length=50, default='Basic Plan')  # Add a default value
    price = models.IntegerField()



    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id


from django.db import models
from django.contrib.auth.models import User

class GymSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    max_capacity = models.PositiveIntegerField(default=10)  # Maximum members allowed
    bookings_count = models.PositiveIntegerField(default=0)  # Track how many members have booked
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.date} at {self.time} ({self.duration} min)"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(GymSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.slot}"


from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)  # Field to indicate if user is verified

    def __str__(self):
        return f"{self.user.username} - Verified: {self.is_verified}"



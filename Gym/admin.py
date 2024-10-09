# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from .models import GymRule
from .models import PaymentProcedure
from .models import SurveyQuestion, Choice, SurveyResponse
from .models import GymNotice,Enrollment,MembershipPlan
from .models import ReceiptSubmission,Attendance,Trainer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified')  # Show verification status in admin panel
    list_editable = ('is_verified',)  # Make the field editable in the list view

admin.site.register(UserProfile, UserProfileAdmin)



class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', 'submitted_at')
    list_filter = ('question', 'submitted_at')
    search_fields = ('user__username', 'question__text')

admin.site.register(SurveyQuestion)
admin.site.register(Choice)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(PaymentProcedure)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Attendance)
admin.site.register(Trainer)
admin.site.register(GymRule)

class GymNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at') 
admin.site.register(GymNotice, GymNoticeAdmin)

class ReceiptSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'submitted_at')  # Customize as needed

admin.site.register(ReceiptSubmission, ReceiptSubmissionAdmin)







def send_booking_permission_email(username, user_email):
    subject = 'Booking Permission Granted!'
    html_message = render_to_string('email/booking_permission.html', {'username': username})
    plain_message = strip_tags(html_message)
    from_email = 'your_email@gmail.com'  # Replace with your email

    send_mail(subject, plain_message, from_email, [user_email], html_message=html_message)

# Admin action to notify users
def notify_users(modeladmin, request, queryset):
    for user in queryset:
        send_booking_permission_email(user.username, user.email)
    modeladmin.message_user(request, "Emails sent to selected users.")

# Unregister the default User admin
admin.site.unregister(User)

# Custom User admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    actions = [notify_users]  # Add the custom action to the admin panel

from django.contrib import admin
from .models import GymSlot, Booking

class GymSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'duration', 'max_capacity', 'bookings_count')

admin.site.register(GymSlot, GymSlotAdmin)
admin.site.register(Booking)

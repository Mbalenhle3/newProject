from django.urls import path
from Gym import views
from .views import survey, survey_results  # Import the views
from .views import submit_receipt
from .views import submit_receipt, receipt_success
from .views import notify_users
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('rules',views.rules,name="Gym rules"),
    path('survey',views.survey,name="Gym Survey"),
    path('thank-you/', views.thank_you, name='thank_you'),  # Add this line
    path('survey/results/', survey_results, name='survey_results'),  # URL for survey results
    path('payments/', views.payment_procedures, name='payment_procedures'),
    path('notices',views.notices,name="Gym Notices"),
    path('submit-receipt/', submit_receipt, name='Receipts Submission'),
    path('receipt-success/', receipt_success, name='receipt_success'),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('attendance',views.attendance,name="attendance"),
    path('location/', views.location, name='location'),
    path('admin/notify-users/', notify_users, name='notify_users'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('available_slots/', views.available_slots, name='available_slots'),  # List of slots to book
    path('book_slot/<int:slot_id>/', views.book_slot, name='book_slot'),  # Booking a specific slot
    
]



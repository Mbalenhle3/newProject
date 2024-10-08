from django.shortcuts import render, redirect
from .models import ReceiptSubmission
from django.contrib.auth.decorators import login_required
from django.db import models 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import SurveyQuestion, Choice
from django.shortcuts import render, get_object_or_404, redirect
from .models import SurveyQuestion, Choice, SurveyResponse
from .models import PaymentProcedure
from .models import GymRule
from .models import GymNotice,MembershipPlan,Enrollment,Trainer,Attendance
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def Home(request):
    return render(request,"index.html")



def survey(request):
    if request.method == 'POST':
        for question in SurveyQuestion.objects.all():
            selected_choice_id = request.POST.get(f'question{question.id}')
            if selected_choice_id:
                selected_choice = get_object_or_404(Choice, id=selected_choice_id)
                # Store the user's response
                SurveyResponse.objects.create(
                    user=request.user,
                    question=question,
                    choice=selected_choice
                )
        return redirect('thank_you')  # Redirect to a 'Thank You' page after submitting

    questions = SurveyQuestion.objects.prefetch_related('choices').all()
    return render(request, 'survey.html', {'questions': questions})

def thank_you(request):
    return render(request, 'thank_you.html')  # A simple page thanking the user for submitting

def survey_results(request):
    # Fetch results from the database
    results = SurveyQuestion.objects.all()
    return render(request, 'survey_results.html', {'results': results})

def thank_you(request):
    return render(request, 'thank_you.html')
def rules(request):
    
    return render(request,"Gym_rules.html")








def signup(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')  # This should be the phone number
        email = request.POST.get('email')          # User's email address
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
      
        # Check username length
        if len(username) != 10:  # Ensure username is exactly 10 digits
            messages.info(request, "Phone Number Must be 10 Digits")
            return redirect('/signup')

        # Check if passwords match
        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup')
       
        # Check if username is taken
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Phone Number is Taken")
            return redirect('/signup')
        
        # Check if email is taken
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is Taken")
            return redirect('/signup')
        
        # Create user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()

        # Send confirmation email
        subject = 'Welcome to Our Gym!'
        html_message = render_to_string('email/signup_confirmation.html', {'username': username})
        plain_message = strip_tags(html_message)
        from_email = 'your_email@gmail.com'  # Replace with your email
        to = email  # Use the email provided by the user
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        messages.success(request, "User is Created. Please Login")
        return redirect('/login')
        
    return render(request, "signup.html")



def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')






def payment_procedures(request):
    payment_procedure = PaymentProcedure.objects.last()  # Get the latest payment procedure
    return render(request, 'payment_procedures.html', {'payment_procedure': payment_procedure})


def rules(request):
    gym_rule = GymRule.objects.last()  # Get the latest gym rule
    return render(request, 'gym_rules.html', {'gym_rule': gym_rule})

def notices(request):
    gym_notice = GymNotice.objects.last()  # Get the latest gym notice
    return render(request, 'gym_notices.html', {'gym_notice': gym_notice})

from django.shortcuts import render, redirect
from .models import ReceiptSubmission
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in
def submit_receipt(request):
    if request.method == 'POST':
        file = request.FILES.get('receipt')  # Get the uploaded file
        if file:
            ReceiptSubmission.objects.create(user=request.user, file=file)  # Save the receipt
            return redirect('receipt_success')  # Redirect to a success page or wherever you prefer

    return render(request, 'submit_receipt.html')  # Render the submission form
from django.shortcuts import render
def receipt_success(request):
    return render(request, 'receipt_success.html')



def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')



    return render(request,"enroll.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

from django.shortcuts import render

def location(request):
    return render(request, 'location.html')


@staff_member_required  # Ensures that only admin can access this view
def notify_users(request):
    if request.method == "POST":
        selected_users = request.POST.getlist('users')  # Assuming you get user IDs or usernames
        for user_id in selected_users:
            try:
                user = User.objects.get(id=user_id)
                send_booking_permission_email(user.username, user.email)
                messages.success(request, f"Email sent to {user.username}.")
            except User.DoesNotExist:
                messages.error(request, f"User with ID {user_id} does not exist.")

        return redirect('notify_users')  # Redirect to the same or another page
    
    # Get users to notify
    users = User.objects.all()  # Fetch all users, or filter as needed
    return render(request, 'admin/notify_users.html', {'users': users})

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_booking_permission_email(username, user_email):
    subject = 'Booking Permission Granted!'
    html_message = render_to_string('email/booking_permission.html', {'username': username})
    plain_message = strip_tags(html_message)
    from_email = 'your_email@gmail.com'  # Replace with your email

    send_mail(subject, plain_message, from_email, [user_email], html_message=html_message)


@staff_member_required  # Ensures that only admin can access this view
def notify_users(request):
    if request.method == "POST":
        selected_users = request.POST.getlist('users')  # Assuming you get user IDs or usernames
        for user_id in selected_users:
            try:
                user = User.objects.get(id=user_id)
                send_booking_permission_email(user.username, user.email)
                messages.success(request, f"Email sent to {user.username}.")
            except User.DoesNotExist:
                messages.error(request, f"User with ID {user_id} does not exist.")

        return redirect('notify_users')  # Redirect to the same or another page
    
    # Get users to notify
    users = User.objects.all()  # Fetch all users, or filter as needed
    return render(request, 'admin/notify_users.html', {'users': users})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GymSlot, Booking

def book_slot(request, slot_id):
    slot = get_object_or_404(GymSlot, id=slot_id)
    user = request.user

    if request.method == "POST":
        # Check if user has already booked this slot
        if Booking.objects.filter(user=user, slot=slot).exists():
            messages.error(request, "You have already booked this slot.")
            return redirect('available_slots')

        # Create the booking
        Booking.objects.create(user=user, slot=slot)
        slot.bookings_count += 1
        slot.save()

        # Send confirmation email
        subject = 'Booking Confirmation'
        message = f'Your booking for {slot.date} at {slot.time} has been confirmed.'
        from_email = 'your_email@gmail.com'  # Replace with your email
        send_mail(subject, message, from_email, [user.email])

        # Render booking confirmation page with slot details
        return render(request, "booking_confirmation.html", {'slot': slot})

    return render(request, "book_slot.html", {'slot': slot})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GymSlot, UserProfile

def available_slots(request):
    user = request.user

    # Check if the user is authenticated
    if not user.is_authenticated:
        return redirect('login')

    # Check if the user is verified
    user_profile = UserProfile.objects.get(user=user)
    
    if not user_profile.is_verified:
        # Display a message to contact admin and prevent access
        messages.error(request, "You are not allowed to book a slot. Please contact an admin.")
        return redirect('Home')  # Redirect to the home page or another page
    
    # If user is verified, show available slots
    slots = GymSlot.objects.all()  # Get all available gym slots
    return render(request, 'available_slots.html', {'slots': slots})

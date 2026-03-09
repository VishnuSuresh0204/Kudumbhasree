from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, "index.html")

def userRegister(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phone']
        password1=request.POST['password']
        image1=request.FILES['img']
        address1=request.POST['address']
        if User.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            user=Login.objects.create_user(
                username=email1,password=password1,usertype='user',viewPassword=password1,is_active=0)
            user.save()
            register=User.objects.create(
                Username=username1,Email=email1,Phone=phonenumber1,Password=password1,Image=image1,Address=address1,logid=user)
            register.save()
            messages.info(request,"Registered Successfully.Waiting for approval!")
            return redirect("/login")
    return render(request, "userRegister.html")

def production_StaffRegister(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phone']
        password1=request.POST['password']
        image1=request.FILES['img']
        address1=request.POST['address']
        if Production_Staff.objects.filter(email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            staff=Login.objects.create_user(
                username=email1,password=password1,usertype='staff',viewPassword=password1,is_active=0)
            staff.save()
            register=Production_Staff.objects.create(
                username=username1,email=email1,phone=phonenumber1,password=password1,image=image1,address=address1,logid=staff)
            register.save()
            messages.info(request,"Registered Successfully.Waiting for approval!")
            return redirect("/login")
    return render(request, "production_staffRegister.html")


def login(request):
    if request.POST:
        Email=request.POST['email']
        Password=request.POST['password']
        user=authenticate(username=Email,password=Password)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminHome")
            elif user.usertype=="user":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The User Page")
                return redirect("/userHome")
            elif user.usertype=="staff":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Staff Page")
                return redirect("/staffHome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
        else:
            messages.info(request,"Invalid Username Or Password")
            return redirect("/login")
    return render(request, "login.html")

# =======================================  ADMIN  ======================================

def adminHome(request):
    return render(request, "ADMIN/adminHome.html")


def viewUsers(request):
    user=User.objects.all()
    return render(request, "ADMIN/viewUsers.html",{'data':user})


def approveUsers(request):
    status=request.GET['status']
    id=request.GET['id']
    wor=Login.objects.get(id=id)
    wor.is_active=int(status)
    wor.save()
    if status == '1':
        messages.info(request," Approved successfully")
    else:
        Login.objects.filter(id=id).delete()
        messages.info(request," Rejected successfully")
    return redirect("/viewUsers")


def deleteUsers(request):
    id=request.GET['id']
    user=User.objects.get(id=id)
    Login.objects.filter(id=user.logid.id).delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewUsers")


def viewStaffs(request):
    staff=Production_Staff.objects.all()
    return render(request, "ADMIN/viewStaffs.html",{'data':staff})


def approveStaff(request):
    status=request.GET['status']
    id=request.GET['id']
    if status == '1':
        wor=Login.objects.get(id=id)
        wor.is_active=1
        wor.save()
        messages.info(request," Approved successfully")
    else:
        Login.objects.filter(id=id).delete()
        messages.info(request," Rejected successfully")
    return redirect("/viewStaffs")


def blockUser(request):
    id=request.GET['id']
    log=Login.objects.get(id=id)
    log.is_active=0
    log.save()
    messages.info(request,"User Blocked Successfully")
    return redirect("/viewUsers")


def unblockUser(request):
    id=request.GET['id']
    log=Login.objects.get(id=id)
    log.is_active=1
    log.save()
    messages.info(request,"User Unblocked Successfully")
    return redirect("/viewUsers")


def blockStaff(request):
    id=request.GET['id']
    log=Login.objects.get(id=id)
    log.is_active=0
    log.save()
    messages.info(request,"Staff Blocked Successfully")
    return redirect("/viewStaffs")


def unblockStaff(request):
    id=request.GET['id']
    log=Login.objects.get(id=id)
    log.is_active=1
    log.save()
    messages.info(request,"Staff Unblocked Successfully")
    return redirect("/viewStaffs")


def deleteStaffs(request):
    id=request.GET['id']
    staff=Production_Staff.objects.get(id=id)
    Login.objects.filter(id=staff.logid.id).delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewStaffs")


def addAttendence(request):
    user = User.objects.all()
    if request.method == 'POST':
        uid = request.POST['user']
        date = request.POST['date']
        status = request.POST['status']
        user_ins = User.objects.get(id=uid)
        atten=Attendance.objects.create(user_id=user_ins, date=date, attendence_status=status)
        atten.save()
        messages.info(request,"Attendence Added")
    return render(request, "ADMIN/addAttendence.html",{"users":user})


def viewUsersAttendence(request):
    date = request.GET.get('date')
    if date:
        atte = Attendance.objects.filter(date=date)
    else:
        atte = Attendance.objects.all()
    return render(request, "ADMIN/viewAttendence.html", {'data': atte, 'selected_date': date})


def viewLoans(request):
    loan=Loan.objects.all()
    return render(request, "ADMIN/viewLoanApplications.html",{'data':loan})

def approveLoan(request):
    loan_id = request.GET.get('id')
    loan = Loan.objects.get(id=loan_id)
    loan.loan_status = 'approved'
    loan.save()
    messages.success(request, "Loan approved.")
    return redirect('/viewLoans')


def rejectLoan(request):
    loan_id = request.GET.get('id')
    loan = Loan.objects.get(id=loan_id)
    loan.loan_status = 'Rejected'
    loan.save()
    messages.info(request, "Loan rejected.")
    return redirect('/viewLoans')


from decimal import Decimal
def loanDuration(request):
    loan_id = request.GET.get('id')
    loan = Loan.objects.get(id=loan_id)
    if request.method == "POST":
        try:
            duration = int(request.POST.get("duration_weeks"))
            if duration <= 0:
                messages.error(request, "Duration must be greater than 0.")
                return render(request, 'ADMIN/addLoanDuration.html', {'loan': loan})
            loan.duration_weeks = duration
            loan.weekly_payment = round(Decimal(loan.amount) / duration, 2)
            loan.loan_status="Approved"
            loan.save()
            applied_date = loan.applied_on
            for week in range(1, duration + 1):
                due_date = applied_date + timedelta(weeks=week)
                Payment.objects.create(
                    loan_id=loan,
                    week_number=str(week),
                    amount_paid=None,
                    payment_status="Pending",
                    due_date=due_date
                )
            messages.success(request, "Loan duration and weekly payment set successfully.")
            return redirect('/viewLoans')
        except (ValueError, ZeroDivisionError):
            messages.error(request, "Invalid input. Please enter a valid number.")
    return render(request, 'ADMIN/addLoanDuration.html', {'loan': loan})


from collections import defaultdict
from django.db.models import Sum, Max, Count

def viewWeeklyPayment(request):
    payments = Payment.objects.filter(payment_status="Paid")
    grouped_data = {}
    for p in payments:
        loan_id = p.loan_id.id
        if loan_id not in grouped_data:
            grouped_data[loan_id] = {
                'loan_id': p.loan_id.id,
                'username': p.loan_id.user_id.Username,
                'loan_amount': float(p.loan_id.amount),
                'purpose': p.loan_id.purpose,
                'duration_weeks': p.loan_id.duration_weeks,
                'weekly_payment': float(p.loan_id.weekly_payment),
                'loan_status': p.loan_id.loan_status,
                'total_paid': 0.0,
                'last_paid': p.due_date,
                'weeks_paid': 0
            }
        grouped_data[loan_id]['total_paid'] += float(p.amount_paid)
        grouped_data[loan_id]['weeks_paid'] += 1
        if p.due_date > grouped_data[loan_id]['last_paid']:
            grouped_data[loan_id]['last_paid'] = p.due_date
    for item in grouped_data.values():
        item['remaining'] = item['loan_amount'] - item['total_paid']
        item['payment_status'] = "Paid" if item['remaining'] <= 0 else "Pending"
    return render(request, 'ADMIN/viewWeeklyPayment.html', {'data': grouped_data.values()})



# =======================================  USER  =======================================

def userHome(request):
    return render(request, "USER/userHome.html")


def viewAttendence(request):
    uid = request.session.get('uid')
    user=User.objects.get(logid=uid)
    atten=Attendance.objects.filter(user_id=user)
    return render(request, "USER/viewAttendence.html",{'data':atten})


def applyForLoan(request):
    uid = request.session.get('uid')
    user=User.objects.get(logid=uid)
    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        purpose = request.POST.get("purpose")  
        if amount <= 1000:
            messages.error(request, "Loan amount must be greater than 1000.")
            return render(request, "USER/applyForLoan.html")
        Loan.objects.create(user_id=user,amount=amount,purpose=purpose)
        messages.success(request, "Loan application submitted successfully.")
        return redirect("/userHome")
    return render(request, "USER/applyForLoan.html")


from datetime import timedelta, date

def viewMyLoans(request):
    uid = request.session.get('uid')
    user = User.objects.get(logid=uid)
    loans = Loan.objects.filter(user_id=user)
    today = date.today()
    
    for loan in loans:
        payments = Payment.objects.filter(loan_id=loan)
        loan.all_payments = []
        for payment in payments:
            if payment.payment_status == "Paid":
                payment.status_curr = "Paid"
                payment.can_pay = False
            elif payment.due_date:
                if payment.due_date < today:
                    payment.status_curr = "Overdue"
                    payment.can_pay = True  # Overdue can always be paid
                else:
                    payment.status_curr = "Upcoming"
                    # Can pay if due_date is within today + 2 days
                    pay_window = today + timedelta(days=2)
                    payment.can_pay = payment.due_date <= pay_window
            else:
                payment.status_curr = "Upcoming"
                payment.can_pay = False

            loan.all_payments.append(payment)
            
    return render(request, 'USER/viewLoans.html', {'data': loans, 'today': today})


def makePayment(request): 
    if request.method == "POST":
        loan_id = request.POST.get('loan_id')
        week_number = request.POST.get("week_number")
    else:
        loan_id = request.GET.get('id')
        week_number = request.GET.get("week_number")

    try:
        loan = Loan.objects.get(id=loan_id, loan_status="Approved")
    except Loan.DoesNotExist:
        messages.error(request, "Loan not found or not approved.")
        return redirect('/viewMyLoans')

    if request.method == "POST":
        try:
            payment = Payment.objects.get(loan_id=loan, week_number=week_number)
        except Payment.DoesNotExist:
            messages.error(request, "Payment record not found.")
            return redirect('/viewMyLoans')
        
        if payment.payment_status == "Paid":
            messages.error(request, f"Week {week_number} is already paid.")
            return redirect(f"/makePayment?id={loan.id}&week_number={week_number}")
        payment.amount_paid = loan.weekly_payment
        payment.payment_status = "Paid"
        payment.paid_on = date.today()
        payment.save()
        paid_weeks = Payment.objects.filter(loan_id=loan, payment_status="Paid").count()
        print(paid_weeks)
        if paid_weeks >= int(loan.duration_weeks):
            loan.loan_status = "Completed"
            loan.save()
            messages.success(request, f"All {loan.duration_weeks} weeks paid. Loan marked as Completed.")
        else:
            messages.success(request, f"Payment for Week {week_number} recorded successfully.")
        return redirect('/viewMyLoans') 
    return render(request, "USER/makePayment.html", {'loan': loan, 'week_number': week_number})



# def makePayment(request):
#     loan_id = request.GET.get('id')
#     week=request.GET.get("week_number")
#     print(week,"weeeeeeek")
#     loan = Loan.objects.get(id=loan_id, loan_status="Approved")
#     if request.method == "POST":
#         week_number = request.POST.get("week_number")
#         if Payment.objects.filter(loan_id=loan, week_number=week_number, payment_status="Paid").exists():
#             messages.error(request, f"Week {week_number} is already paid.")
#             return redirect(f"/makePayment?id={loan.id}&week_number={week_number}")
#         Payment.objects.create(
#             loan_id=loan,week_number=week_number,amount_paid=loan.weekly_payment,payment_status="Paid",
#             paid_on = date.today())
#         paid_weeks = Payment.objects.filter(loan_id=loan, payment_status="Paid").count()
#         if paid_weeks >= int(loan.duration_weeks):
#             loan.loan_status = "Completed"
#             loan.save()
#             messages.success(request, f"All {loan.duration_weeks} weeks paid. Loan marked as Completed.")
#         else:
#             messages.success(request, f"Payment for Week {week_number} recorded successfully.")
#         return redirect('/viewMyLoans') 
#     return render(request, "USER/makePayment.html", {'loan': loan,'week_number':week})


def userViewProducts(request):
    pro=Product.objects.all()
    return render(request,"USER/viewProducts.html",{'data':pro})


def bookProduct(request):
    uid = request.session.get('uid')
    user=User.objects.get(logid=uid)
    pid = request.GET.get('id')
    product=Product.objects.get(id=pid)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))
        price = float(product.product_price)
        total = quantity * price
        current_stock = int(product.product_stock)
        if quantity > current_stock:
            messages.error(request, "Not enough stock available.")
            return redirect(f'/bookProduct?id={product.id}')
        Booking.objects.create(user_id=user,product_id=product,
            quantity=quantity,total=total)
        remaining_stock = current_stock - quantity
        product.product_stock = str(remaining_stock)
        if remaining_stock == 0:
            product.pstatus = "Out of Stock"
        product.save()
        messages.success(request, "Product booked successfully.")
        return redirect('/myBookings')  
    return render(request, "USER/bookProduct.html", {'product': product})


def myBookings(request):
    uid = request.session.get('uid')
    user=User.objects.get(logid=uid)
    book=Booking.objects.filter(user_id=user)
    return render(request, "USER/productBookings.html",{"bookings":book})


def addPayment(request):
    id=request.GET.get("id")
    booking=Booking.objects.get(id=id)
    price = request.GET.get("price")
    if request.method == "POST":
        booking.booking_status = "Paid"
        booking.save()
        messages.success(request, "Payment successful!")
        return redirect('/myBookings')
    return render(request, "USER/addPayment.html", {'booking': booking,'price': price})
    


# =======================================  STAFF  ======================================

def staffHome(request):
    return render(request, "PRODUCTION_STAFF/staffHome.html")


def addProducts(request):
    uid = request.session.get('uid')
    staff=Production_Staff.objects.get(logid=uid)
    if request.POST:
        pname=request.POST['product_name']
        pprice=request.POST['product_price']
        pdesc=request.POST['product_description']
        pstock=request.POST['product_stock']
        pprodu=request.POST['production_date']
        pexp=request.POST['expiry_date']
        pimg=request.FILES['product_img']
        proo=Product.objects.create(product_name=pname,product_price=pprice,
                production_date=pprodu,expiry_date=pexp,
                product_stock=pstock,product_description=pdesc,
                product_img=pimg,staff_id=staff)
        proo.save()
        messages.success(request, "Product added successfully.")
    return render(request, "PRODUCTION_STAFF/addProducts.html")


def viewProducts(request):
    uid = request.session.get('uid')
    staff=Production_Staff.objects.get(logid=uid)
    pro=Product.objects.filter(staff_id=staff)
    return render(request,"PRODUCTION_STAFF/viewProducts.html",{'data':pro})


def editProduct(request):
    uid = request.session.get('uid')
    staff=Production_Staff.objects.get(logid=uid)
    pid = request.GET.get('id')
    product=Product.objects.get(id=pid)
    if request.POST:
        product.product_name = request.POST.get("product_name")
        product.product_price = request.POST.get("product_price")
        product.production_date = request.POST.get("production_date")
        product.expiry_date = request.POST.get("expiry_date")
        product.product_stock = request.POST.get("product_stock")
        product.product_description = request.POST.get("product_description")
        if 'product_img' in request.FILES:
            product.product_img = request.FILES['product_img']
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect('/viewProducts')
    return render(request,"PRODUCTION_STAFF/editProduct.html", {"product": product})


def deleteProduct(request):
    pid = request.GET.get('id')
    product=Product.objects.filter(id=pid)
    product.delete()
    messages.info(request, "Product Deleted.")
    return redirect('/viewProducts')


def viewBookings(request):
    uid = request.session.get('uid')
    staff=Production_Staff.objects.get(logid=uid)
    book=Booking.objects.filter(product_id__staff_id=staff)
    return render(request, "PRODUCTION_STAFF/viewBookings.html",{"bookings":book})
    



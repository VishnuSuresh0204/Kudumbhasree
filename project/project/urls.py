"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index),
    path('userRegister/', views.userRegister),
    path('staffRegister/', views.production_StaffRegister),
    path('login/', views.login),
    
    
    # =======================================  ADMIN  ======================================
    path('adminHome/', views.adminHome),
    path('viewUsers/', views.viewUsers),
    path('approveUsers/', views.approveUsers),
    path('deleteUsers/', views.deleteUsers),
    path('viewStaffs/', views.viewStaffs),
    path('approveStaff/', views.approveStaff),
    path('blockUser/', views.blockUser),
    path('unblockUser/', views.unblockUser),
    path('blockStaff/', views.blockStaff),
    path('unblockStaff/', views.unblockStaff),
    path('deleteStaffs/', views.deleteStaffs),
    path('addAttendence/', views.addAttendence),
    path('viewUsersAttendence/', views.viewUsersAttendence),
    path('viewLoans/', views.viewLoans),
    path('approveLoan/', views.approveLoan),
    path('rejectLoan/', views.rejectLoan),
    path('loanDuration/', views.loanDuration),
    path('viewWeeklyPayment/', views.viewWeeklyPayment),
    
    
    # =======================================  USER  =======================================
    path('userHome/', views.userHome),
    path('viewAttendence/', views.viewAttendence),
    path('applyForLoan/', views.applyForLoan),
    path('viewMyLoans/', views.viewMyLoans),
    path('makePayment/', views.makePayment, name='make_payment'),
    path('userViewProducts/', views.userViewProducts),
    path('bookProduct/', views.bookProduct),
    path('myBookings/', views.myBookings),
    path('addPayment/', views.addPayment),
    
    
    # =======================================  STAFF  ======================================
    path('staffHome/', views.staffHome),
    path('addProducts/', views.addProducts),
    path('viewProducts/', views.viewProducts),
    path('editProduct/', views.editProduct),
    path('deleteProduct/', views.deleteProduct),
    path('viewBookings/', views.viewBookings),
]

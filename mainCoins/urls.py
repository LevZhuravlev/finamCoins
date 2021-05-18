from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', open, name='main'),
    path('login', MyProjectLoginView.as_view(), name='login'),
    path('logout', MyProjectLogout.as_view(), name='logout'),
    path('allequitiess', equitiess, name='allequitiess'),
    path('detail/<str:slug>/', studentDetail, name='studentdetailurlforstudent'),
    path('buyEquitiess/<str:slug>/', DoYouReallyWantToBuyEquitiess.as_view(), name='doYouReallyWantToBuyEquitiess'),
    path('successEquitiess/<str:slug>/', youBoughtEquitiess.as_view(), name='successEquitiess'),

    path('fimcoinadmin', fimCoinAdmin, name='fimcoinadmin'),

    path('fimcoinadminAllStudents', fimCoinAdminAllStudent, name='fimcoinadminAllStudents'),
    path('fimcoinadminAllTeacher', fimCoinAdminAllTeacher.as_view(), name='fimcoinadminAllTeacher'),
    path('fimcoinadminAllTeacher/<str:slug>/', teacherDetail.as_view(), name='teacherDetail'),
    path('fimcoinadminAllTeacher/<str:slug>/edit', fimCoinEditTeacher.as_view(), name='fimCoinAdminEditTeacher'),
    path('fimcoinadminAllTeacher/<str:slug>/delete', fimCoinDeleteTeacher.as_view(), name='fimCoinAdminDeleteTeacher'),

    path('fimcoinadminAllGroup/<str:slug>/', groupDetail.as_view(), name='groupDetail'),
    path('fimcoinadminAllGroup/<str:slug>/edit', fimCoinEditGroup.as_view(), name='fimCoinAdminEditGroup'),
    path('fimcoinadminAllGroup/<str:slug>/delete', fimCoinDeleteGroup.as_view(), name='fimCoinAdminDeleteGroup'),
    path('fimcoinadminAllGroup/<str:slug>/addStudentAtGroup', addStudentAtGroupForm.as_view(), name='addStudentAtGroup'),

    path('fimcoinadminAllTeacher/success/<str:slug>/', teacherDetailSuccess.as_view(), name='teacherDetailSuccess'),
    path('fimcoinadminAllTeacher/success/<str:slug>/logout', MyProjectLogout.as_view(), name='logout'),
    path('fimcoinadminAllTeacher/<str:slug>/logout',  MyProjectLogout.as_view(), name='logout'),
    path('fimcoinadminEquitiess', fimCoinAdminEquitiess, name='fimcoinadminEquitiess'),

    path('сreateGroup', fimCoinCreateGroup, name='fimCoinAdminCreateGroup'),
    path('сreateStudent', fimCoinCreateStudent, name='fimCoinAdminCreateStudent'),
    path('сreateTeacher', fimCoinCreateTeacher.as_view(), name='fimCoinAdminCreateTeacher'),

    path('fimcoinadmin/<str:slug>/', studentDetail, name='studentdetailurl'),
    path('fimcoinadmin/studentNotification/<str:slug>/', studentNotification, name='notification'),
    path('fimcoinadmin/addFimCoins/<str:slug>/', addFimCoinsDetail.as_view(), name='addFimCoins'),
    path('fimcoinadmin/<str:slug>/logout',  MyProjectLogout.as_view(), name='logout'),
    path('fimcoinadmin/<str:slug>/edit', fimCoinEditStudent.as_view(), name='fimCoinAdminEditStudent'),
    path('fimcoinadmin/<str:slug>/delete', fimCoinDeleteStudent.as_view(), name='fimCoinAdminDeleteStudent'),

]

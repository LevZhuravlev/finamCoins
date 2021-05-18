from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .form import *
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Equities, StudentsInfo, TeachersInfo, Groups
from .coinLogic import coinPrice, get_current_coin_price
from .equitiesChekingParser import foo

import datetime

d1 = datetime.datetime.today()



def open(request):
    if request.user.is_authenticated:

        if not chekingForTeacher(request):

            context = {}
            context['Equities'] = Equities.objects.order_by('price')
            try:
                context['Coins'] = StudentsInfo.objects.get(user_name=request.user).coins
            except:
                context['Coins'] = 0

            context['Differene'] = []
            context['Differene_proc'] = []
            coins = int(str(context['Coins']))
            for i in context['Equities']:
                foo()

                inFimCoinPrice = coinPrice(i.price)


                context['Differene'].append(round(inFimCoinPrice - coins))
                context['Differene_proc'].append(str(round((coins / inFimCoinPrice) * 100)) + '%')

            fusion = zip(context['Equities'], context['Differene'], context['Differene_proc'])
            return render(request, 'mainCoins/index.html', {'fusion': fusion, 'Coins': str(context['Coins']),  'Today': datetime.datetime.today()})

        else:
            return redirect('/fimcoinadmin')

    else:
        return redirect('/login')


def equitiess(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/fimcoinadmin')
        else:
            foo()
            context = {}
            context['Equities'] = Equities.objects.order_by('price')
            try:
                context['Coins'] = StudentsInfo.objects.get(user_name=request.user).coins
            except:
                context['Coins'] = 0

            context['Differene'] = []
            context['Differene_proc'] = []
            context['Today'] = datetime.datetime.today()
            coins = int(str(context['Coins']))
            for i in context['Equities']:
                inFimCoinPrice = (coinPrice(i.price))
                context['Differene'].append(round(inFimCoinPrice - coins))
                context['Differene_proc'].append(str(round((coins / inFimCoinPrice) * 100)) + '%')

            fusion = zip(context['Equities'], context['Differene'], context['Differene_proc'])
            return render(request, 'mainCoins/allequitiess.html', {'fusion': fusion, 'Coins': str(context['Coins']), 'Today': datetime.datetime.today()})

    else:
        return redirect('/login')



class MyProjectLoginView(LoginView):
    template_name = 'mainCoins/login.html'
    form_class = AuthUserForm
    success_url = '/'

    def get_success_url(self):
        return self.success_url


class MyProjectLogout(LogoutView):
    next_page = '/login'


# __________________ ⭐ Admin ⭐️ __________________

def fimCoinAdmin(request):
    if chekingForTeacher(request):
        teacher = TeachersInfo.objects.get(user_name=request.user)

        context = {}
        context['myGroups'] = teacher.group.all()
        context['Student'] = StudentsInfo.objects.all()

        return render(request, 'mainCoins/fimcoinadmin.html', context)

    else:
        return redirect('/')


class addFimCoinsDetail(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug=slug)
            bound_form = changeStudentCoinForm(instance=student)

            return render(request,
                          'mainCoins/addFimCoins.html',
                          {"form": bound_form,
                           "student": student
                           })

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug=slug)
            bound_form = changeStudentCoinForm(request.POST, instance=student)

            if bound_form.is_valid():
                bound_form.save()
            else:
                return render(request, 'mainCoins/addFimCoins.html',
                          {"form": changeStudentCoinForm(request.POST),  "student": student})

            return redirect('/')

        else:
            return redirect('/')


def studentDetail(request, slug):
    if request.user.is_authenticated:

        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug__iexact=slug)
            equities = student.equities.all()

            return render(request, 'mainCoins/studentDetail.html', {'student': student, 'equities': equities})
        else:
            try:
                currentSlug = StudentsInfo.objects.get(user_name=request.user).slug
            except:
                currentSlug = ''
            if currentSlug == slug:
                student = StudentsInfo.objects.get(slug__iexact=slug)
                allTeachers = TeachersInfo.objects.all()
                teachers = []
                for i in allTeachers:
                    for j in i.group.all():
                        if j == student.group:
                            teachers.append(i)


                equities = student.equities.all()
                return render(request, 'mainCoins/studentDetailForStudent.html', {'student': student, 'equities': equities, 'teachers': teachers})
            else:
                return redirect('/')

    else:
        return  redirect('/')

def fimCoinAdminAllStudent(request):
    if chekingForTeacher(request):
        teacher = TeachersInfo.objects.get(user_name=request.user)

        context = {}
        context['Groups'] = Groups.objects.all()
        context['Student'] = StudentsInfo.objects.all()
        context['isAllStudentInGroup'] = True

        for i in StudentsInfo.objects.all():
            if i.group == None:
                context['isAllStudentInGroup'] = False
                break

        return render(request, 'mainCoins/fimcoinadminAllStudents.html', context)

    else:
        return redirect('/')


def fimCoinAdminEquitiess(request):
    if chekingForTeacher(request):
        foo()
        context = {}
        context['Equities'] = Equities.objects.order_by('price')
        context['Current_coin_price'] = get_current_coin_price()
        context['TodayToday'] = datetime.datetime.today()
        return render(request, 'mainCoins/fimcoinadminEquitiess.html', context)

    else:
        return redirect('/')


# ___ Create ____
def fimCoinCreateGroup(request):
    if chekingForTeacher(request):

        if request.method == 'POST':
            bound_form = createGroupForm(request.POST)
            if bound_form.is_valid():
                new_group = bound_form.save()
                return redirect('/')
            return render(request, 'mainCoins/fimCoinAdminCreateGroup.html',
                          {"createGroup": createGroupForm(bound_form)})

        else:
            return render(request, 'mainCoins/fimCoinAdminCreateGroup.html', {"createGroup": createGroupForm})

    else:
        return redirect('/')



def fimCoinCreateStudent(request):
    if chekingForTeacher(request):
        if request.method == 'POST':
            bound_form = createStudentForm(request.POST)
            if bound_form.is_valid():
                new_student = bound_form.save()
                return redirect('/fimcoinadmin/' + new_student.slug)
            return render(request, 'mainCoins/fimCoinAdminCreateStudent.html',
                          {"createStudent": createGroupForm(bound_form)})

        else:
            return render(request, 'mainCoins/fimCoinAdminCreateStudent.html', {"createStudent": createStudentForm})

    else:
        return redirect('/')


class fimCoinEditStudent(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug=slug)
            bound_form = createStudentForm(instance=student)

            return render(request,
                          'mainCoins/fimCoinAdminEditStudent.html',
                          {"form": bound_form,
                           "student": student
                           })

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug=slug)
            bound_form = createStudentForm(request.POST, instance=student)

            if bound_form.is_valid():
                bound_form.save()

            return redirect('/fimcoinadmin/' + student.slug)

        else:
            return redirect('/')


class fimCoinDeleteStudent(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            getStudentUser = StudentsInfo.objects.get(slug=slug)
            student = User.objects.get(username=getStudentUser.user_name)
            return render(request,
                          'mainCoins/fimCoinAdminDeleteStudent.html',
                          {"student": student,
                           "getStudentUser": getStudentUser})

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            getStudentUser = StudentsInfo.objects.get(slug=slug)
            student = User.objects.get(username=getStudentUser.user_name)
            student.delete()
            return redirect('/')

        else:
            return redirect('/')


class fimCoinCreateTeacher(View):

    def get(self, request):

        if chekingForTeacher(request):
            form = createTeacherForm

            return render(request, 'mainCoins/fimCoinAdminCreateTeacher.html', {'createTeacherForm': form})

        else:
            return redirect('/')

    def post(self, request):

        bound_form = createTeacherForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            createdTeacher = TeachersInfo.objects.get(email=bound_form.cleaned_data['email'])
            createdTeacher.who_add_me = request.user
            createdTeacher.save()
            return redirect('fimcoinadminAllTeacher/success/' + createdTeacher.slug)

        else:
            return render(request, 'mainCoins/fimCoinAdminCreateTeacher.html', {"createTeacherForm": bound_form})


class fimCoinAdminAllTeacher(View):

    def get(self, request):
        if chekingForTeacher(request):
            teacher_list = TeachersInfo.objects.all()
            return render(request,
                          'mainCoins/fimcoinadminAllTeachers.html',
                          {'Teachers': teacher_list})

        else:
            return redirect('/')


class teacherDetail(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            teacherDetailSuccess = False
            teacher = TeachersInfo.objects.get(slug__iexact=slug)
            who_watching_this = request.user
            teacher_watching_this = TeachersInfo.objects.get(user_name=who_watching_this)
            try:
                teacher_who_add_me = TeachersInfo.objects.get(user_name=teacher.who_add_me)
            except:
                teacher_who_add_me = None

            return render(request,
                          'mainCoins/teacherDetail.html',
                          {'teacher': teacher,
                           'who_watching_this': who_watching_this,
                           'teacher_watching_this': teacher_watching_this,
                           'teacher_who_add_me': teacher_who_add_me,
                           'teacherDetailSuccess': teacherDetailSuccess
                           })

        else:
            return redirect('/')


class teacherDetailSuccess(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            teacherDetailSuccess = True
            teacher = TeachersInfo.objects.get(slug__iexact=slug)
            who_watching_this = request.user
            teacher_watching_this = TeachersInfo.objects.get(user_name=who_watching_this)
            try:
                teacher_who_add_me = TeachersInfo.objects.get(user_name=teacher.who_add_me)
            except:
                teacher_who_add_me = None

            return render(request,
                          'mainCoins/teacherDetail.html',
                          {'teacher': teacher,
                           'who_watching_this': who_watching_this,
                           'teacher_watching_this': teacher_watching_this,
                           'teacher_who_add_me': teacher_who_add_me,
                           'teacherDetailSuccess': teacherDetailSuccess})

        else:
            return redirect('/')


class fimCoinEditTeacher(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            teacher = TeachersInfo.objects.get(slug=slug)
            bound_form = createTeacherForm(instance=teacher)

            return render(request,
                          'mainCoins/fimCoinAdminEditTeacher.html',
                          {"form": bound_form,
                           "teacher": teacher
                           })

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            teacher = TeachersInfo.objects.get(slug=slug)
            bound_form = createTeacherForm(request.POST, instance=teacher)

            if bound_form.is_valid():
                bound_form.save()

            return redirect('/fimcoinadminAllTeacher/' + teacher.slug)

        else:
            return redirect('/')


class fimCoinDeleteTeacher(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            getTeacherUser = TeachersInfo.objects.get(slug=slug)
            teacher = User.objects.get(username=getTeacherUser.user_name)
            return render(request,
                          'mainCoins/fimCoinAdminDeleteTeacher.html',
                          {"teacher": teacher,
                           "getTeacherUser": getTeacherUser})

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            getTeacherUser = TeachersInfo.objects.get(slug=slug)
            teacher = User.objects.get(username=getTeacherUser.user_name)
            teacher.delete()
            return redirect('/fimcoinadminAllTeacher')

        else:
            return redirect('/')


class groupDetail(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            group = Groups.objects.get(slug__iexact=slug)
            return render(request, 'mainCoins/groupDetail.html', {'group': group})

        else:
            return redirect('/')


class fimCoinEditGroup(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            group = Groups.objects.get(slug=slug)
            bound_form = createGroupForm(instance=group)

            return render(request,
                          'mainCoins/fimCoinAdminEditGroup.html',
                          {"form": bound_form,
                           "group": group
                           })

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            group = Groups.objects.get(slug=slug)
            bound_form = createGroupForm(request.POST, instance=group)

            if bound_form.is_valid():
                bound_form.save()

            return redirect('/fimcoinadminAllGroup/' + group.slug)

        else:
            return redirect('/')


class fimCoinDeleteGroup(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            getGroup = Groups.objects.get(slug=slug)
            return render(request,
                          'mainCoins/fimCoinAdminDeleteGroup.html',
                          {"getGroup": getGroup})

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            getGroup = Groups.objects.get(slug=slug)
            getGroup.delete()
            return redirect('/fimcoinadmin')

        else:
            return redirect('/')


class addStudentAtGroupForm(View):

    def get(self, request, slug):
        if chekingForTeacher(request):
            group = Groups.objects.get(slug=slug)
            form = addStudentForm()
            return render(request,
                          'mainCoins/fimCoinAdminAddStudentAtGroup.html',
                          {"form": form,
                           "group": group
                           })

        else:
            return redirect('/')

    def post(self, request, slug):
        if chekingForTeacher(request):
            group = Groups.objects.get(slug=slug)
            bound_form = createGroupForm(request.POST, instance=group)

            if bound_form.is_valid():
                bound_form.save()

            return redirect('/fimcoinadminAllGroup/' + group.slug)

        else:
            return redirect('/')


def chekingForTeacher(request):
    if request.user.is_authenticated:
        try:
            TeachersInfo.objects.get(user_name=request.user)
            return True

        except:
            return False


from math import ceil


class whatisfimcoin(View):
    def get(self, request):
        return render(request, 'mainCoins/whatisfimcoin.html')

class DoYouReallyWantToBuyEquitiess(View):

    def get(self, request, slug):
        if request.user.is_authenticated:
            company = Equities.objects.get(slug=slug)
            company_price_coins = ceil(coinPrice(company.price))
            return render(request, 'mainCoins/studenWhantBuyEquitiess.html', {'company': company, 'company_price_coins': company_price_coins})

        else:
            return redirect('/')
    def post(self, request, slug):
        if request.user.is_authenticated:
            company = Equities.objects.get(slug=slug)
            company_price_coins = ceil(coinPrice(company.price))
            student = StudentsInfo.objects.get(user_name=request.user)
            student.coins = int(student.coins) - int(company_price_coins)
            student.notifications = student.notifications + "\n Студент хочет приобрести акцию компании " + str(company.company_name) + " по стоимости " + str(company.price) + "рублей"



            student.save()

            return render(request, 'mainCoins/studenWhantBoughtEquitiess.html', {'company': company, 'company_price_coins': company_price_coins})

        else:
            return redirect('/')


class youBoughtEquitiess(View):

    def get(self, request, slug):
        if request.user.is_authenticated:
            company = Equities.objects.get(slug=slug)
            company_price_coins = ceil(coinPrice(company.price))
            return render(request, 'mainCoins/studenWhantBoughtEquitiess.html', {'company': company, 'company_price_coins': company_price_coins})





def studentNotification(request, slug):
    if request.user.is_authenticated:
        if chekingForTeacher(request):
            student = StudentsInfo.objects.get(slug__iexact=slug)
            return render(request, 'mainCoins/studentNotification.html', {'student': student})


    return redirect('/')


class studentBuyEquitiess(View):

    def get(self, request):

        if chekingForTeacher(request):
            form = createTeacherForm

            return render(request, 'mainCoins/fimCoinAdminCreateTeacher.html', {'createTeacherForm': form})

        else:
            return redirect('/')

    def post(self, request):

        bound_form = createTeacherForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            createdTeacher = TeachersInfo.objects.get(email=bound_form.cleaned_data['email'])
            createdTeacher.who_add_me = request.user
            createdTeacher.save()
            return redirect('fimcoinadminAllTeacher/success/' + createdTeacher.slug)

        else:
            return render(request, 'mainCoins/fimCoinAdminCreateTeacher.html', {"createTeacherForm": bound_form})
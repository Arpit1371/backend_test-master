from django.shortcuts import render
from django.http import HttpResponse
from main.models import Company
from main.models import Employee

# Create your views here.


def companies_view(request):
    All_companies = Company.objects.all()
    All_employees = Employee.objects.all()

    employee_given = request.POST.get('employee', None)
    change_to_company = request.POST.get('company', None)

    print(change_to_company   )

    if(employee_given != None and change_to_company != None ):
        
        firstname, lastname = employee_given.split()
        print(firstname , lastname)

        for company in All_companies :
            if( company.name == change_to_company ):
                change_to_company_object= company 
        


        for employee in All_employees :
            if( employee.first_name == firstname and employee.last_name == lastname  ):

                employee.company = change_to_company_object
                employee.save()
                print('success')







    
    hashmap = {}
    for company in All_companies :
        hashmap[company.name] = []

    
    

    for employee in All_employees :
        if(employee.company != None ):
            hashmap[employee.company.name].append( employee )

    



    return render(request, 'companies.html', {"companies": Company.objects.all() , "hashmap" : hashmap})

def add_employee(request, company_name):
    company = company_name
    print(company)
    All_employees = Employee.objects.all()
    


    return render(request , 'form.html' ,  {'company': company, 'All_employees': All_employees} )


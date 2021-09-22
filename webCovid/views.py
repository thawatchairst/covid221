from django.shortcuts import render
import requests
import time
# Create your views here.


def formatdate(time1):

    for list1 in time1:
        for x,y in list1.items():
            if x =='update_date':
                date1 =y
    
    return date1

def index(request):
    req = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
    time.sleep(2)
    req_po = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces')
    
    jsonData_Po =req_po.json()
    jsonData = req.json()
    date1=formatdate(jsonData)
    Statuscode =req.status_code
    #return render(request ,'index.html')
    return render(request ,'index.html',{'status':Statuscode,'data':jsonData,'data_po':jsonData_Po,'dateT':date1})
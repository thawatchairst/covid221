from django.shortcuts import render
import requests
# Create your views here.




def index(request):
    req = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
    req_po = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces')
    jsonData_Po =req_po.json()
    jsonData = req.json()
    Statuscode =req.status_code
    #return render(request ,'index.html')
    return render(request ,'index.html',{'status':Statuscode,'data':jsonData,'data_po':jsonData_Po})
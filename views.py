# I have created this Website and File 
import re
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    parm={'name':"Suruchi",'place':"Delhi"}
    return render(request,'index.html',parm)
    #return  HttpResponse('hello<br/><h4><strong><a href="about/">ABOUT US</a></strong><br/><h4><strong><a href="contact/">Contact Us</a></strong> ')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def textanalyize(request):
    #get data from  form elements
    getDataTxt=request.POST.get('txt_analyz','default')
    getrmv_punc=request.POST.get('chk_rmv_punc','off')
    getuppr_cas=request.POST.get('chk_upprcase','off')
    getchk_nwlinermv=request.POST.get('chk_nwlinermv','off')
    getchk_extrspacermv=request.POST.get('chk_extrspacermv','off')
    getchk_chrcount=request.POST.get('chk_chrcount','off')

    #-----------Features code text
    
    if getrmv_punc =='on': #-----------removng punctuation
        analyzd=''
        punclst= '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''
        purp_msg='Removed Punctuation'   
        for txt in getDataTxt:
            if txt not in punclst:
                analyzd=analyzd+ txt
    if getuppr_cas=='on': #-----------Uppercase
        analyzd=''
        purp_msg='Change to uppercase'
        for txt in getDataTxt:
            analyzd=analyzd +txt.upper()     
    if getchk_nwlinermv=='on':
        analyzd=''
        purp_msg='New Line Remover'
        for txt in getDataTxt:
            if txt != '\n' and txt !='\r':
                analyzd=analyzd+txt
    if getchk_extrspacermv=='on':
        analyzd=''
        purp_msg='Extra space remover'
        for index, txt in enumerate(getDataTxt):
            if txt[index]==' ' and txt[index+1]==' ':
                pass
            else:
                analyzd=analyzd+txt

    if getchk_chrcount=='on':
        analyzd=''
        purp_msg='Counting Character'
        analyzd=len(getDataTxt)

    if (getchk_chrcount !='on' and getrmv_punc !='on' and getchk_extrspacermv !='on' and getuppr_cas !='on' and getchk_nwlinermv !='on' ):
        purp_msg='No option'
        analyzd='No option is selected'
    #-------------------------------------------
    #return analyzd
    #create dictionary for data collection
    parmtr={'purpose':purp_msg,'analyzed_txt':analyzd}

    #sending data to html file
    return render(request,'analyze.html',parmtr)
    #return HttpResponse('<center>CONTACT ME</center><br/><h4><strong><a href="/">HOME</a></strong> ')

from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.shortcuts import render
from django.http import HttpResponse
from .forms import simulaForm
from .models import EntradasMaisAlimentos


def index(request):
    dadossimulacao=simulaForm(request.POST)
    
    dados={
       	'dadossimulacao': dadossimulacao
   		}
    return render(request, 'index.html', dados)


def sim(request):
    """Calcula o saldo devedor, o valor de cada parcela e atribui um número inteiro para cada parcela
    depois esses valores são atribuidos a listas e essas listas são passadas para o template, justamente 
    com a variavael dadosdasimulacao, essa variavel vai conter os valores digitados no formulário com o 
    method get"""
    contador_parcela=1
    listaContadorParcela=[]
    listaDataParcela=[]
    listaResultado=[]
    listaSaldoDev=[]
    

    valor=float(request.GET['valor'])
    divisao=int(request.GET['divisao'])
    carencia=float(request.GET['carencia'])
    taxa=(float(request.GET['taxa'])/100)

    dataprimeiraparcela=datetime.now() +relativedelta(years=(carencia+1))
    strDataprimeiraparcela=str(dataprimeiraparcela.day)+'/'+str(dataprimeiraparcela.month)+"/"+str(dataprimeiraparcela.year)
    print(strDataprimeiraparcela)

    saldo_devedor=valor*(1+taxa)**(carencia+1)
    parcela=(saldo_devedor/divisao)
    listaResultado.append(parcela)
    listaSaldoDev.append(saldo_devedor)
    listaContadorParcela.append('1')
    listaDataParcela.append(strDataprimeiraparcela)
    n=divisao

    while n > 0:
        n=n-1
        saldo_devedor=saldo_devedor-parcela
        saldo_devedor=saldo_devedor*(1+taxa)
        if n>0:
            parcela=saldo_devedor/n
            contador_parcela+=1
            dataprimeiraparcela=dataprimeiraparcela+ relativedelta(years=1)
            strDataprimeiraparcela=str(dataprimeiraparcela.day)+'/'+str(dataprimeiraparcela.month)+"/"+str(dataprimeiraparcela.year)
            listaResultado.append(parcela)
            listaSaldoDev.append(saldo_devedor)
            listaContadorParcela.append(str(contador_parcela))
            listaDataParcela.append(strDataprimeiraparcela)
        else:
            break   

    dadossimulacao=simulaForm(request.GET)
    
    dados={
        "listaDataParcela":listaDataParcela,
        "listaSaldoDev":listaSaldoDev,
        "listaResultado":listaResultado,
        "listaContadorParcela":listaContadorParcela,
       	"dadossimulacao": dadossimulacao
   		}

    return render(request, 'result_sim.html', dados )

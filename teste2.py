inteiro=20160212
inte=str(inteiro)
o=0
ano=''
mes=''
dia=''
for i in inte:
    o=o+1
    if o<5:
        ano=ano+i
    elif o<7 and o>4:
        mes=mes+i
    else:
        dia=dia+i
print ano+"-"+mes+"-"+dia

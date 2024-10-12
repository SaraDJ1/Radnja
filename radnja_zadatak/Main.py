from Procenti import IzracunajProcente

cena_jakne = 1200
nova_cena_jakne = IzracunajProcente(cena_jakne)

cena_lopte = 3000

if (cena_jakne<cena_lopte):
    print("Jakna je idalje jeftinija")
elif(cena_jakne>cena_lopte):
    print("Jakna je skuplja od lopte")
else:
    print("Jakna je iste cene kao i lopta")


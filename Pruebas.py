import os 
import os.path
import getpass

#Aligiendo procesador y grafica
while True:
    print("¿Que procesador posee su equipo?")
    print("1.Intel")
    print("2.AMD")
    procesador=input("Elija una opcion: ")
    if (procesador=='1'):
        procesador= " intel-ucode "
        break
    elif (procesador=='2'):
        procesador=" amd-ucode "
        break
    else:
        print("Elija una opcion correcta")


while True:
    print("¿Que grafica posee su equipo?")
    print("1.Intel")
    print("2.AMD / ATI")
    print("3.Nvidia")
    grafica=input("Elija una opcion: ")
    if (grafica=='1'):
        grafica= " xf86-video-intel "
        break
    elif (grafica=='3'):
        grafica=" xf86-video-nouveau "
        break
    elif (grafica=='2'):
        print("¿Que grafica AMD / ATI posee su equipo?")
        print("1. AMD (modernas)")
        print("2. ATI (antiguas)")
        grafica = input("Elija una opcion:")
        if(grafica=='1'):
            grafica = " xf86-video-amdgpu "
            break
        elif(grafica=='2'):
            grafica = " xf86-video-ati "
            break


print(procesador)
print(grafica)






import subprocess
import os 
import os.path
import getpass


print("Bienvenido a la guia de instalación rapida de Arch")


#Actualizando repositorios
print("Seleccionando los 15 mejores sevidores replica")
subprocess.run('reflector --latest 15 --sort rate --save /etc/pacman.d/mirrorlist', shell=True)

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



#Instalando paquetes basicos
print("Instalando paquetes base...")
subprocess.run('pacstrap /mnt linux linux-firmware base base-devel nano os-prober grub networkmanager dhcpcd xterm efibootmgr netctl wpa_supplicant dialog sudo git python3 xorg-server xorg-apps xorg-xinit alacritty xf86-video-vesa archey3 '+procesador+grafica, shell=True)

#Guardando tabla de particiones
print("Guardando particiones")
subprocess.run('genfstab /mnt >> /mnt/etc/fstab', shell=True)

#Guardando el nombre de la maquina

hostname = input("Digite el nombre del equipo: ")
subprocess.run('arch-chroot /mnt echo '+hostname+' >> /mnt/etc/hostname', shell=True)
subprocess.run('arch-chroot /mnt echo "127.0.0.1 localhost" >> /mnt/etc/hosts', shell=True)
subprocess.run('arch-chroot /mnt echo "::1 localhost" >> /mnt/etc/hosts', shell=True)
subprocess.run('arch-chroot /mnt echo "127.0.1.1 '+hostname+'.localdomain '+hostname+'" >> /mnt/etc/hosts', shell=True)


#Buscando Continente
resultado =[]
for item in os.listdir("/mnt/usr/share/zoneinfo"):
    if os.path.isdir("/mnt/usr/share/zoneinfo/"+item):
        resultado.append(item)

print("Configurando zona horaria")
while True:
    print("Elija una region")
    for item in resultado:
        print(item)
    region = input("Escriba el nombre de la region: ").capitalize()
    
    regionTest = subprocess.run('ls /mnt/usr/share/zoneinfo/'+region, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if regionTest.returncode == 0:
        break
    else:
        print("Error al encontrar la region, verifiquelo e intente de nuevo")


#Buscando Paises del contiente elegido
resultado =[]
for item in os.listdir("/mnt/usr/share/zoneinfo/"+region):
    if os.path.isfile("/mnt/usr/share/zoneinfo/"+region+"/"+item):
        resultado.append(item)

while True:
    print("Elija un region")
    for item in resultado:
        print(item)
    pais = input("Escriba el nombre de la region: ")
    
    paisTest = subprocess.run('ls /mnt/usr/share/zoneinfo/'+region+"/"+pais, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if paisTest.returncode == 0:
        subprocess.run('arch-chroot /mnt ln -sf /usr/share/zoneinfo/'+region+'/'+pais+' /etc/localtime', shell=True)
        break
    else:
        print("Error al encontrar la region, verifiquelo e intente de nuevo")

print("Configurando Idiomas Predeterminados:")
#Agregando idiomas predeterminados
subprocess.run('arch-chroot /mnt echo es_CR ISO-8859-1 >> /mnt/etc/locale.gen', shell=True)
subprocess.run('arch-chroot /mnt echo es_CR.UTF-8 UTF-8 >> /mnt/etc/locale.gen', shell=True)
subprocess.run('arch-chroot /mnt echo en_US ISO-8859-1 >> /mnt/etc/locale.gen', shell=True)
subprocess.run('arch-chroot /mnt echo en_US.UTF-8 UTF-8 >> /mnt/etc/locale.gen', shell=True)
#Generando Idiomas
subprocess.run('arch-chroot /mnt locale-gen', shell=True)

print("Configurando Reloj del sistema")
subprocess.run('arch-chroot /mnt  hwclock -w', shell=True)
subprocess.run('arch-chroot /mnt timedatectl set-ntp true', shell=True)


print('Elija el idioma de su sistema.')
print('1. Español, Costa Rica')
print('2. Ingles, Estados Unidos')
idioma = input("Escriba un numero de la lista anterior:")
if idioma == '1':
    subprocess.run('arch-chroot /mnt echo LANG=es_CR.UTF8 > /mnt/etc/locale.conf', shell=True)
elif idioma == '2':
    subprocess.run('arch-chroot /mnt echo LANG=en_US.UTF8 > /mnt/etc/locale.conf', shell=True)
else:
    subprocess.run('arch-chroot /mnt echo LANG=es_CR.UTF8 > /mnt/etc/locale.conf', shell=True)

print('Elija el idioma de su teclado.')
print('1. Español, Latinoamerica')
print('2. Español, España')
print('3. Ingles, Estados Unidos Internacional')
teclado = input("Escriba un numero de la lista anterior:")

if teclado == '1':
    subprocess.run('arch-chroot /mnt echo KEYMAP=la-latin1 > /mnt/etc/vconsole.conf', shell=True)
elif teclado == '2':
    subprocess.run('arch-chroot /mnt echo KEYMAP=es > /mnt/etc/vconsole.conf', shell=True)
elif teclado == '3':
    subprocess.run('arch-chroot /mnt echo KEYMAP=us-acentos > /mnt/etc/vconsole.conf', shell=True)
else:
    subprocess.run('arch-chroot /mnt echo KEYMAP=la-latin1 > /mnt/etc/vconsole.conf', shell=True)

#Comprobando modalidad de arranque
print("Comprobando la modalidad de arranque...")
uefi = subprocess.run('ls /sys/firmware/efi/efivars', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if uefi.returncode == 0:
    print("Modalidad de arranque UEFI")
    print("Instalando GRUB...")
    subprocess.run("arch-chroot /mnt grub-install --efi-directory=/boot/efi --bootloader-id='Arch Linux' --target=x86_64-efi", shell=True)
else:
    print("Modalidad de arranque BIOS")
    print("Instalando GRUB...")
    subprocess.run('arch-chroot /mnt grub-install /dev/sda', shell=True)

print("Verificando sistemas instalados...")
subprocess.run('arch-chroot /mnt os-prober', shell=True)

print("Configurando GRUB...")
subprocess.run('arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg', shell=True)
print("Configurando usuarios...")
print("Usuario root")
subprocess.run('arch-chroot /mnt passwd', shell=True)
    
while True:
    userp = input("Escriba el nombre del usuario personal:")
    subprocess.run('arch-chroot /mnt useradd -m '+userp, shell=True)
    print("Introduzca la contraseña del usuario "+userp+": ")
    subprocess.run('arch-chroot /mnt passwd '+userp, shell=True)
    subprocess.run('arch-chroot /mnt sed -i "79a '+userp+' ALL=(ALL) ALL" /mnt/etc/sudoers', shell=True)
    print("¿Desea agregar otro usuario?")
    print("1.Si , 2. No")
    otrouser = input("Seleccione una opcion:")
    if otrouser != "1":
        break


print("Activando servicios de red...")
subprocess.run('arch-chroot /mnt systemctl enable NetworkManager.service', shell=True)


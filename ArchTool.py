import subprocess
import os 
import os.path



print("Bienvenido a la guia de instalación rapida de Arch")

#Comprobando modalidad de arranque
print("Comprobando la modalidad de arranque...")
uefi = subprocess.run('ls /sys/firmware/efi/efivars', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if uefi.returncode == 0:
    print("Modalidad de arranque UEFI")
    b_uefi = True
else:
    print("Modalidad de arranque BIOS")
    b_uefi = False

#Actualizando repositorios
print("Seleccionando los 10 mejores sevidores replica")
#subprocess.run('reflector --latest 10 --sort rate --save /etc/pacman.d/mirrorlist', shell=True)

#Instalando paquetes basicos
print("Instalando paquetes base...")
#subprocess.run('pacstrap /mnt linux linux-firmware base base-devel nano os-prober grub networkmanager dhcpcd xterm efibootmgr netctl wpa_supplicant dialog sudo git python3 xorg-server xorg-apps xorg-xinit', shell=True)

#Guardando tabla de particiones
print("Guardando particiones")
#subprocess.run('genfstab /mnt >> /mnt/etc/fstab', shell=True)

#Guardando el nombre de la maquina
if os.path.exists('/mnt/etc/hostname'):
    print("Nombre del equipo: ")
    subprocess.run(' cat /mnt/etc/hostname', shell=True)
else:
    hostname = input("Digite el nombre del equipo: ")
    subprocess.run('arch-chroot /mnt echo '+hostname+' >> /mnt/etc/hostname', shell=True)

#Buscando Continente
resultado =[]
for item in os.listdir("/mnt/usr/share/zoneinfo"):
    if os.path.isdir("/mnt/usr/share/zoneinfo/"+item):
        resultado.append(item)

print("Configurando zona horaria")
while True:
    print("Eliga una region")
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
    print("Eliga un region")
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
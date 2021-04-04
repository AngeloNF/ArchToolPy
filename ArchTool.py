import subprocess
import os 
import os.path



print("Bienvenido a la guia de instalación rapida de Arch")

#Comprobando modalidad de arranque
print("Comprobando la modalidad de arranque...")
uefi = subprocess.run('ls /sys/firmware/efi/efivars', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if uefi.stderr is None:
    print("Modalidad de arranque UEFI")
    b_uefi = True
if uefi.stdout is None:
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
hostname = input("Digite el nombre del equipo: ")

subprocess.run('arch-chroot /mnt echo '+hostname+' >> /mnt/etc/hostname', shell=True)

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
    
    regionTest = subprocess.run('ls /mnt/usr/share/zoneinfo/'+region, shell=True, stdout=subprocess.PIPE, stdout=subprocess.PIPE)
    if regionTest.stderr is None:
        break
    else:
        print("Error al encontrar la region, verifiquelo e intente de nuevo")

resultado =[]
for item in os.listdir("/mnt/usr/share/zoneinfo/"+region):
    if os.path.isdir("/mnt/usr/share/zoneinfo/"+region+"/"+item):
        resultado.append(item)

while True:
    print("Eliga un region")
    for item in resultado:
        print(item)
    pais = input("Escriba el nombre de la region: ").capitalize()
    
    paisTest = subprocess.run('ls /mnt/usr/share/zoneinfo/'+region+"/"+pais, shell=True, stdout=subprocess.PIPE)
    if paisTest.stderr is None:
        break
    else:
        print("Error al encontrar la region, verifiquelo e intente de nuevo")

import subprocess


print("Bienvenido a la guia de instalación rapida de Arch")

#Comprobando modalidad de arranque
print("Comprobando la modalidad de arranque...")
uefi = subprocess.run('ls /sys/firmware/efi/efivars', shell=True, stdout=subprocess.PIPE)
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





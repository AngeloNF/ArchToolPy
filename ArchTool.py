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

#Instalando paquetes basicos
print("Instalando paquetes base...")
subprocess.run('pacstrap /mnt linux linux-firmware base base-devel nano os-prober grub networkmanager dhcpcd xterm efibootmgr netctl wpa_supplicant dialog sudo git python3 xorg-server xorg-apps xorg-xinit', shell=True)

#Guardando tabla de particiones
print("Guardando particiones")
subprocess.run('genfstab /mnt >> /mnt/etc/fstab')

#Guardando el nombre de la maquina
#hostname = input("Digite el nombre del equipo: ")




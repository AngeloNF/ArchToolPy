import subprocess

print("Bienvenido a la guia de instalación rapida de Arch")
print("Comprobando la modalidad de arranque...")
uefi = subprocess.run('ls /sys/firmware/efi/efivars', shell=True, stdout=subprocess.PIPE)
if uefi.stderr is None:
    print("Modalidad de arranque UEFI")
if uefi.stdout is None:
    print("Modalidad de arranque BIOS")

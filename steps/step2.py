from func.colors import yellow

input("Did you set your partitions, format them and mount them on" + yellow("/mnt? "))

import os

os.system("pacstrap /mnt base base-devel net-tools xdg-user-dirs")
os.system("pacstrap /mnt python wget")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("cp -r /root/tali /mnt/tali")
os.system("mount --bind /tmp /mnt/tmp")
os.system("arch-chroot /mnt python tali/install.py")
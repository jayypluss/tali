from func.colors import cyan, green, yellow
from func.yes_no_dialog import yes_no_dialog

good_to_go = yes_no_dialog("Did you set your partitions, format them and mount them on " + yellow("/mnt") + "?")

if good_to_go:
  import os

  os.system("pacstrap /mnt base base-devel linux linux-firmware net-tools xdg-user-dirs")
  os.system("pacstrap /mnt python wget")
  os.system("genfstab -U /mnt >> /mnt/etc/fstab")
  os.system("cp -r /root/tali /mnt/tali")
  os.system("arch-chroot /mnt python tali/install.py --step 3")
else:
  # TODO: Make this a function, since this dialog is also used in step 1.
  print("\nPlease, set your partitions now, format and mount them on " + yellow("/mnt") + ".")
  print("If all you want to do is to wipe all partitions and install " + cyan("Arch Linux") + ", you can run " + green("tali/quick_partitioning.py") + ".")
  print("Otherwise, you can format your partitions yourself with " + green("parted") + " or a similar tool.")
  print("\nWhen you're done, run " + green("tali/install.py") + " again.\n")

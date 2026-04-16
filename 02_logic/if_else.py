print("===========================")
print("    IF-ELSE STATEMENT")
print("===========================\n")

# input from user
name = input("Masukkan nama Anda: ")
age = int(input("Masukkan umur Anda: "))

# if-else statement
if age >= 18:
    print("Halo " + name + "! Anda sudah dewasa.\n")
else:
    print("Halo " + name + "! Anda belum dewasa.\n")


# if elif else statement
nilai = int(input("Masukkan nilai Anda: "))
if nilai >= 90:
    print("Nilai Anda sangat baik.")
elif nilai >= 80:
    print("Nilai Anda baik.")
elif nilai >= 70:
    print("Nilai Anda cukup.")
else:
    print("Nilai Anda perlu diperbaiki.")
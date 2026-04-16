print("===========================")
print("    LOOPING IN PYTHON")
print("===========================\n")

# for loop
i = int(input("For Loop: Masukkan jumlah iterasi: "))
print("Hasil For Loop:")
for j in range(i):
    print("Iterasi ke -" , str(j + 1))

# while loop
wh = int(input("\nWhile Loop: Masukkan jumlah iterasi: "))
print("Hasil While Loop:")
l = 0
while l < wh:
    print("Iterasi ke -" , str(l + 1))
    l += 1

infinite = input("\nApakah Anda ingin membuat infinite loop? (y/n): ")
if infinite.lower() == 'y':
    print("Tekan Ctrl + C untuk menghentikan infinite loop.")
    while True:
        print("Infinite Loop berjalan...")

# x = int(input("Masukkan input: "))
# s = 0

# pas = True

# while pas:
#     if x > 0:
#         s=s+x
#         x=x-1
#     else:
#         print("Hasil akhir s :", s)
#         pas = False

# versi 2 barisan aritmatika bertingkat

x = int(input("Masukkan input: "))
s = 0

for i in range(1, x+1):
    s = s+i

print(s)
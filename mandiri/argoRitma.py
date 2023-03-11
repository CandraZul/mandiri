pas = True


while pas:
    adult = int(input("Masukkan adult: "))
    if adult <= 6:
        pas = False
    elif adult > 6:
        print("Adult tidak boleh lebih dari 6")

child = int(input("Masukkan children: "))
infant = int(input("Masukkan infant: "))

total = adult*255000 + child*150000 + infant*25000

if adult >= 4:
    total = total - total*0.2

print("Total harga tiket adalah " + str(total))
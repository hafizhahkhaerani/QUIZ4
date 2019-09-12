listGPA = [2.1,2.2,3,4]
def hadiah (listGPA):
    bonus = 500000
    hadiah = listGPA * bonus
    return hadiah
for GPA in listGPA :
    if GPA > 2.5:
        print("Selamat anda mendapatkan",hadiah(GPA))
    else :
        print("Maaf anda belum beruntung")



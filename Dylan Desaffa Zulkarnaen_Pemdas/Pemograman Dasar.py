def garis():
    print("----------")

def sort_asc(array):
    array = sorted(array)
    return(array)

def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)

def rata_rata(angka):
    return sum(angka)/len(angka)

garis()
print("masukkan tiga buah nilai")
nilai_a = int(input("nilai a : "))
nilai_b = int(input("nilai b : "))
nilai_c = int(input("nilai c : "))
angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

print("hasil akhir----")
print("urutan angka ascending : ", (sort_asc(angka)))
print("urutan angka descending : ", (sort_desc(angka)))
garis()
print()

print("angka terbesar : ",max(angka))

print("angka terkecil : ",min(angka))

print("rata rata : ",round(rata_rata(angka),2))

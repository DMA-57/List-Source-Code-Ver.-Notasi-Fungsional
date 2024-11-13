# Program     : listFunctions.py
# Deskripsi   : Fungsi-fungsi untuk operasi list.
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : Rabu, 30 October 2024
# ================================================================================================================
# DEFINISI DAN SPESIFIKASI TYPE LIST 
# List adalah tipe bentukan yang berisi kumpulan elemen satu tipe yang urutannya diperhitungkan

# Konstruksi elemen ke dalam list di posisi awal
# Konso: elemen, List --> List
# {Menambahkan elemen ke depan list}
def Konso(e, L):
    return [e] + L

# Konstruksi elemen ke dalam list di posisi akhir
# Konsi: List, elemen --> List
# {Menambahkan elemen ke akhir list}
def Konsi(L, e):
    return L + [e]
 
# Predikat untuk mengecek apakah list kosong
# isEmpty: List --> boolean
# {Mengembalikan True jika list kosong}
def IsEmpty(L):
    return L == []

# Predikat untuk mengecek apakah list hanya memiliki satu elemen
# isOneElmt: List --> boolean
# {Mengembalikan True jika list hanya memiliki satu elemen}
def IsOneElmt(L):
    if IsEmpty(L): return False
    else:
        return Tail(L) == [] and Head(L) == []

# Selektor elemen pertama
# FirstElmt: List tidak kosong --> elemen
# {Mengembalikan elemen pertama dari list}
def FirstElmt(L):
    if IsEmpty(L):
        return None
    return L[0]

# Selektor elemen terakhir
# LastElmt: List tidak kosong --> elemen
# {Mengembalikan elemen terakhir dari list}
def LastElmt(L):
    if IsEmpty(L):
        return None
    return L[-1]

# Selektor bagian list setelah elemen pertama
# Tail: List tidak kosong --> List
# {Mengembalikan list tanpa elemen pertama}
def Tail(L):
    if IsEmpty(L):
        return []
    return L[1:]

# Selektor bagian list sebelum elemen terakhir
# Head: List tidak kosong --> List
# {Mengembalikan list tanpa elemen terakhir}
def Head(L):
    if IsEmpty(L):
        return []
    return L[:-1]

# Operator jumlah elemen
# NbElmt: List --> integer
# {Mengembalikan jumlah elemen dalam list}
def NbElmt(L):
    if IsEmpty(L):  # Basis
        return 0
    else:           # Rekurens
        return NbElmt(Head(L)) + 1

# Selektor elemen ke-N dalam list
# ElmtKeN: integer >= 0, List --> elemen
# {Mengembalikan elemen ke-N dari list, jika ada}
def ElmtKeN(x, L):
    if x > NbElmt(L):
        return None
    if x == 0:
        return FirstElmt(L)
    else:
        return ElmtKeN(x - 1, Tail(L))

# Operator untuk mengecek keanggotaan elemen
# isMember: elemen, List --> boolean
# {Mengembalikan True jika elemen ada dalam list}
def isMember(x, L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return isMember(x, Tail(L))

# Operator untuk mengkopi list
# Copy: List --> List
# {Mengembalikan kopi dari list L}
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# Operator untuk membalik urutan list
# Inverse: List --> List
# {Mengembalikan list dengan urutan terbalik dari list L}
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# Operator untuk menggabungkan dua list
# Konkat: 2 List --> List
# {Menggabungkan dua list L1 dan L2}
def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konsi(Konkat(L1, Head(L2)), LastElmt(L2))

# Operator untuk menjumlahkan elemen dalam list integer
# SumElmt: List of integer --> integer
# {Mengembalikan jumlah semua elemen dalam list integer L}
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# Operator untuk menghitung rata-rata elemen dalam list integer
# AvgElmt: List of integer --> real
# {Mengembalikan rata-rata elemen dalam list integer L}
def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)

def max2(x, y):
    return x if x > y else y

# Operator untuk menemukan nilai maksimum
# MaxElmt: List of integer --> integer
# {Mengembalikan nilai maksimum dari list integer L}
def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        return max2(FirstElmt(L), MaxElmt(Tail(L)))
    
def count(x, L):
    if IsEmpty(L):
        return 0
    else:
        if FirstElmt(L) == x:
            return 1 + count(x, Tail(L))
        else:
            return count(x, Tail(L))


# Operator untuk mencari nilai maksimum dan jumlah kemunculannya
# MaxNB: List of integer --> <integer, integer>
# {Mengembalikan nilai maksimum dari L dan jumlah kemunculannya}
def MaxNB(L):
    # return [MaxElmt(L), count(MaxElmt(L), L)]
    return Konso(MaxElmt(L), Konso(count(MaxElmt(L), L), []))

# Operator untuk menambahkan dua list integer secara elemen per elemen
# AddList: 2 List of integer --> List of integer
# {Mengembalikan list yang elemen-elemennya adalah hasil penjumlahan elemen-elemen sepadan dari L1 dan L2}
def AddList(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):  
        return []
    elif IsEmpty(L1): 
        L1 = [0] * NbElmt(L2)
    elif IsEmpty(L2):  
        L2 = [0] * NbElmt(L1)
    return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# Operator untuk mengecek apakah list adalah palindrom
# isPalindrom: List of character --> boolean
# {Mengembalikan True jika list karakter L adalah palindrom}
def isPalindrom(L):
    if IsOneElmt(L):
        return True
    elif IsEmpty(L):
        return True
    else:
        if FirstElmt(L) != LastElmt(L): return False
        return isPalindrom(Tail(Head(L)))

# Operator untuk mengecek kesamaan antara dua list
# isEqual: 2 List --> boolean
# {Mengembalikan True jika kedua list memiliki elemen yang sama dalam urutan yang sama}
def isEqual(L1, L2):
    if NbElmt(L1) != NbElmt(L2):
        return False
    else:
        if IsEmpty(L1) and IsEmpty(L2):
            return True
        elif FirstElmt(L1) == FirstElmt(L2):
            return isEqual(Tail(L1), Tail(L2))
        else:
            return False

# Operator untuk menghapus satu elemen dari list
# Rember: elemen, list --> list
# {Menghapus elemen pertama x dari list L, jika ada}
def Rember(x, L):
    if IsEmpty(L):
        return []
    else:
        if x == FirstElmt(L):
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))

# Operator untuk menghapus semua elemen tertentu dari list
# MultiRember: elemen, list --> list
# {Menghapus semua elemen x dari list L}
def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if x == FirstElmt(L):
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

# Operator untuk mengurutkan list
# sortList: List of integer --> List
# {Mengurutkan elemen dalam list integer L dari terkecil ke terbesar}
def sortList(L):
    if IsEmpty(L):
        return L
    else:
        return Konsi(sortList (Rember(MaxElmt(L), L)), MaxElmt(L))

# Operator untuk memfilter elemen tertentu dari list
# filterList: List --> List
# {Mengembalikan list berisi semua elemen x di list L}
def filterList(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Konso(FirstElmt(L), filterList(x, Tail(L)))
        else:
            return filterList(x, Tail(L))

# Aplikasi fungsi

# Konstruksi elemen ke dalam list di posisi awal
# print(Konso(1, [2, 3, 4, 5]))   # --> [1, 2, 3, 4, 5]
# print(Konso('a', ['b', 'c']))    # --> ['a', 'b', 'c']

# # Konstruksi elemen ke dalam list di posisi akhir
# print(Konsi([1, 2, 3], 4))       # --> [1, 2, 3, 4]
# print(Konsi(['x', 'y'], 'z'))     # --> ['x', 'y', 'z']

# # Predikat untuk mengecek apakah list kosong
# print(IsEmpty([]))               # --> True
# print(IsEmpty([1, 2, 3]))        # --> False

# # Predikat untuk mengecek apakah list hanya memiliki satu elemen
# print(IsOneElmt([1]))            # --> True
# print(IsOneElmt([1, 2]))         # --> False

# # Selektor elemen pertama
# print(FirstElmt([1, 2, 3]))      # --> 1
# print(FirstElmt(['a', 'b', 'c']))# --> 'a'

# # Selektor elemen terakhir
# print(LastElmt([1, 2, 3]))       # --> 3
# print(LastElmt(['x', 'y', 'z'])) # --> 'z'

# # Selektor bagian list setelah elemen pertama
# print(Tail([1, 2, 3, 4]))        # --> [2, 3, 4]
# print(Tail(['a', 'b', 'c']))     # --> ['b', 'c']

# # Selektor bagian list sebelum elemen terakhir
# print(Head([1, 2, 3, 4]))        # --> [1, 2, 3]
# print(Head(['x', 'y', 'z']))     # --> ['x', 'y']

# # Operator jumlah elemen
# print(NbElmt([1, 2, 3]))         # --> 3
# print(NbElmt([]))                # --> 0

# # Selektor elemen ke-N dalam list
# print(ElmtKeN(1, [10, 20, 30]))  # --> 20
# print(ElmtKeN(0, [10, 20, 30]))  # --> 10

# # Operator untuk mengecek keanggotaan elemen
# print(isMember(3, [1, 2, 3, 4])) # --> True
# print(isMember('a', ['x', 'y'])) # --> False

# # Operator untuk mengkopi list
# print(Copy([1, 2, 3]))           # --> [1, 2, 3]
# print(Copy(['a', 'b', 'c']))     # --> ['a', 'b', 'c']

# # Operator untuk membalik urutan list
# print(Inverse([1, 2, 3]))        # --> [3, 2, 1]
# print(Inverse(['x', 'y', 'z']))  # --> ['z', 'y', 'x']

# # Operator untuk menggabungkan dua list
# print(Konkat([1, 2], [3, 4]))    # --> [1, 2, 3, 4]
# print(Konkat(['a'], ['b', 'c'])) # --> ['a', 'b', 'c']

# # Operator untuk menjumlahkan elemen dalam list integer
# print(SumElmt([1, 2, 3]))        # --> 6
# print(SumElmt([10, 20, 30]))     # --> 60

# # Operator untuk menghitung rata-rata elemen dalam list integer
# print(AvgElmt([1, 2, 3, 4]))     # --> 2.5
# print(AvgElmt([10, 20, 30]))     # --> 20.0

# # Operator untuk menemukan nilai maksimum
# print(MaxElmt([1, 5, 3, 9, 2]))  # --> 9
# print(MaxElmt([-1, -5, -3]))     # --> -1

# # Operator untuk mencari nilai maksimum dan jumlah kemunculannya
# print(MaxNB([1, 2, 3, 2, 3, 3])) # --> [3, 3]
# print(MaxNB([4, 4, 4, 2]))       # --> [4, 3]

# # Operator untuk menambahkan dua list integer secara elemen per elemen
# print(AddList([1, 2, 3], [4, 5, 6])) # --> [5, 7, 9]
# print(AddList([1, 2], [3, 4, 5]))    # --> [4, 6, 5]

# # Operator untuk mengecek apakah list adalah palindrom
# print(isPalindrom(['a', 'b', 'a']))  # --> True
# print(isPalindrom([1, 2, 3]))        # --> False

# # Operator untuk mengecek kesamaan antara dua list
# print(isEqual([1, 2, 3], [1, 2, 3])) # --> True
# print(isEqual([1, 2], [1, 2, 3]))    # --> False

# # Operator untuk menghapus satu elemen dari list
# print(Rember(2, [1, 2, 3, 2, 4]))    # --> [1, 3, 2, 4]
# print(Rember(5, [1, 2, 3]))          # --> [1, 2, 3]

# # Operator untuk menghapus semua elemen tertentu dari list
# print(MultiRember(2, [1, 2, 3, 2, 4])) # --> [1, 3, 4]
# print(MultiRember('a', ['a', 'b', 'a']))# --> ['b']

# # Operator untuk mengurutkan list
# print(sortList([3, 1, 4, 1, 5]))       # --> [1, 1, 3, 4, 5]
# print(sortList([10, 5, 2, 8]))         # --> [2, 5, 8, 10]

# # Operator untuk memfilter elemen tertentu dari list
# print(filterList(1, [1, 2, 3, 1, 4, 1])) # --> [1, 1, 1]
# print(filterList('b', ['a', 'b', 'c', 'b'])) # --> ['b', 'b']

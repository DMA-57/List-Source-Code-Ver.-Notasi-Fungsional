# Program     : setFunctions.py
# Deskripsi   : Fungsi-fungsi untuk operasi set.
# NIM/Nama    : Daffa Maulana Alfianto
# Tanggal     : Rabu, 06 November 2024
# ================================================================================================================
# DEFINISI DAN SPESIFIKASI TYPE HIMPUNAN 
# Set adalah tipe bentukan yang berisi kumpulan komponen unik dan tak berurut
from listFunctions import *

#DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x, L) menghapus sebuah elemen x dari list L 
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.

def Rember (x,L) :
    if IsEmpty(L):
        return []
    else:
        if x == FirstElmt(L):
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))

# MultiRember: elemen, list -> list
# {MultiRember(x, L) menghapus semua elemen x dari list L}

def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if x == FirstElmt(L):
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))


# MakeSet: list -> set
# {MakeSet(L) membentuk himpunan dari list dengan menghilangkan elemen ganda / tidak unik dari list L, rekursi yang dilakukan dengan mengabaikan kemunculan elemen ganda di list}
def MakeSet(L):
    if IsEmpty(L):
        return []
    else:
        if isMember(FirstElmt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet(Tail(L)))


# MakeSet1: list -> set
# {MakeSet1(L) membentuk himpunan dari list dengan menghilangkan elemen ganda / tidak unik dari list L dengan multiRember} 
def MakeSet1(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSet1(MultiRember(FirstElmt(L), Tail(L))))


# KonsoSet: elemen, set -> set
# {KonsoSet(e, H) menambahkan elemen e ke depan set H, tetapi hanya jika e belum ada di H.
# Hasil adalah set dengan elemen e di posisi pertama jika belum ada di H.}
def KonsoSet(e, H):
    if isMember(e, H):
        return H
    else:
        return Konso(e, H)

# KonsoSet:  set, elemen -> set
# {KonsoSet(e, H) menambahkan elemen e ke belakang set H, tetapi hanya jika e belum ada di H.
# Hasil adalah set dengan elemen e di posisi terakhir jika belum ada di H.}
def KonsiSet(H, e):
    if isMember(e, H):
        return H
    else:
        return Konsi(H, e)

# IsSet: list -> boolean
# {IsSet(L) menghasilkan True jika L adalah himpunan (tidak memiliki elemen duplikat).
# Menghasilkan False jika ada elemen yang muncul lebih dari sekali dalam L.}
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if isMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))


# IsSubset: 2 set -> boolean
# {IsSubset(H1, H2) menghasilkan True jika semua elemen di H1 terdapat di H2.
# Menghasilkan False jika ada elemen di H1 yang tidak ada di H2.}
def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if isMember(FirstElmt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False

# IsEqualSet: 2 set -> boolean
# {IsEqualSet(H1, H2) menghasilkan True jika H1 dan H2 memiliki elemen yang sama.
# Menghasilkan False jika terdapat elemen yang berbeda antara H1 dan H2.   }    
def IsEqualSet(H1, H2):
    return IsSubset(H1, H2) and IsSubset(H2, H1)

# IsEqualSet1: 2 set  -> boolean
# {IsEqualSet1(H1, H2) menghasilkan True jika H1 dan H2 memiliki elemen yang sama,
# tetapi menghitung elemen duplikat dan memeriksa satu per satu dengan Rember.}
def IsEqualSet1(H1, H2):
    if NbElmt(H1) != NbElmt(H2):
        return False
    else:
        if IsEmpty(H1):
            return True
        else:
            if isMember(FirstElmt(H1), H2):
                return IsEqualSet(Tail(H1), Rember(FirstElmt(H1),H2))
            else:
                return False

# IsIntersect: 2 set -> boolean
# {IsIntersect(H1, H2) menghasilkan True jika terdapat elemen yang sama di H1 dan H2.
# Menghasilkan False jika tidak ada elemen yang sama di antara H1 dan H2.}
def IsIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    else:
        if IsEmpty(H1):
            return False
        else: 
            if isMember(FirstElmt(H1), H2):
                return True
            else:
                return IsIntersect(Tail(H1), H2)
            
# MakeIntersect: 2 set -> set
# {MakeIntersect(H1, H2) menghasilkan himpunan yang berisi elemen-elemen yang ada di H1 dan H2.
# Hasil adalah list dengan elemen-elemen yang sama pada H1 dan H2 tanpa duplikat.}
def MakeIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    else:
        if IsEmpty(H1):
            return []
        else: 
            if isMember(FirstElmt(H1), H2):
                return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
            else:
                return MakeIntersect(Tail(H1), H2)

def MakeIntersect1(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    else:
        if IsEmpty(H2):
            return []
        else: 
            if isMember(FirstElmt(H2), H1):
                return Konso(FirstElmt(H2), MakeIntersect(H1, Tail(H2)))
            else:
                return MakeIntersect(H1, Tail(H2))

# MakeUnion: 2 set -> set
# {MakeUnion(H1, H2) menghasilkan himpunan yang berisi semua elemen dari H1 dan H2.
# Menghasilkan list dengan semua elemen unik dari H1 dan H2 digabung.  } 
def MakeUnion(H1, H2):
    if IsEmpty(H1):
        return H2
    else:
        if isMember(FirstElmt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))
        
# MakeUnion1: 2 set -> set
# {MakeUnion1(H1, H2) menghasilkan himpunan yang berisi semua elemen dari H1 dan H2.
# Elemen-elemen H2 ditambahkan di akhir H1 jika belum ada di H1.}
def MakeUnion1(H1, H2):
    if IsEmpty(H2):
        return H1
    else:
        if isMember(LastElmt(H2), H1):
            return MakeUnion(H1, Head(H2))
        else:
            return Konsi( MakeUnion(H1, Head(H2)), LastElmt(H2))
    



# NBIntersect: 2 set -> integer
# {NBIntersect(H1, H2) menghitung jumlah elemen yang sama di H1 dan H2.
# Menghasilkan jumlah elemen yang terdapat di kedua himpunan.}
def NBIntersect(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2): return 0
    else:
        if isMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)

# NBUnion: 2 set -> integer
#{ NBUnion(H1, H2) menghitung total elemen unik yang ada di H1 dan H2.
# Menghasilkan jumlah elemen setelah H1 dan H2 digabung tanpa duplikat.}
def NBUnion(H1, H2):
    if IsEmpty(H1): return NbElmt(H2)
    else:
        if isMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)

# sortSet: set -> set
# {sortSet(H) menghasilkan set yang berisi elemen-elemen dari H, diurutkan dari terbesar ke terkecil.
# Mengurutkan H berdasarkan elemen tanpa mengubah isi himpunan.}
def sortSet(H):
    if IsEmpty(H):
        return H
    else:
        return Konsi( sortSet(Rember(MaxElmt(H), H)), MaxElmt(H) )

# Aplikasi fungsi

# Menghapus satu elemen dari list
# print(Rember(2, [1, 2, 3, 2, 4]))           # --> [1, 3, 2, 4]
# print(Rember(5, [1, 2, 3]))                 # --> [1, 2, 3]

# # Menghapus semua elemen tertentu dari list
# print(MultiRember(2, [1, 2, 3, 2, 4]))      # --> [1, 3, 4]
# print(MultiRember('a', ['a', 'b', 'a']))    # --> ['b']

# # Membuat set dari list (menghapus duplikat)
# print(MakeSet([1, 2, 3, 2, 4]))             # --> [1, 3, 2, 4]
# print(MakeSet(['a', 'b', 'a']))             # --> ['b', 'a']

# # Membuat set dari list menggunakan MultiRember
# print(MakeSet1([1, 2, 2, 3, 4]))            # --> [1, 2, 3, 4]
# print(MakeSet1(['a', 'b', 'a']))            # --> ['a', 'b']

# # Menambahkan elemen ke dalam set
# print(KonsoSet(2, [1, 3, 4]))               # --> [2, 1, 3, 4]
# print(KonsoSet('a', ['b', 'c']))            # --> ['a', 'b', 'c']

# # Menambahkan elemen ke akhir set
# print(KonsiSet( [1, 2, 3], 4))               # --> [1, 2, 3, 4]
# print(KonsiSet( ['x', 'y'], 'z'))            # --> ['x', 'y', 'z']

# # Mengecek apakah list adalah set
# print(IsSet([1, 2, 3, 4]))                  # --> True
# print(IsSet([1, 2, 2, 3]))                  # --> False

# # Mengecek apakah H1 adalah subset dari H2
# print(IsSubset([1, 2], [1, 2, 3, 4]))       # --> True
# print(IsSubset([1, 5], [1, 2, 3]))          # --> False

# # Mengecek kesetaraan dua set
# print(IsEqualSet([1, 2, 3], [3, 2, 1]))     # --> True
# print(IsEqualSet([1, 2], [2, 3]))           # --> False

# # Mengecek kesetaraan dua set dengan perbandingan jumlah elemen
# print(IsEqualSet1([1, 2, 3], [3, 2, 1]))    # --> True
# print(IsEqualSet1([1, 2], [2, 3]))          # --> False

# # Mengecek apakah ada irisan antara dua set
# print(IsIntersect([1, 2, 3], [3, 4, 5]))    # --> True
# print(IsIntersect([1, 2], [4, 5]))          # --> False

# # Membuat irisan dari dua set
# print(MakeIntersect([1, 2, 3], [2, 3, 4]))  # --> [2, 3]
# print(MakeIntersect(['a', 'b'], ['b', 'c'])) # --> ['b']

# # Membuat irisan dengan cara kedua
# print(MakeIntersect1([1, 2, 3], [2, 3, 4])) # --> [2, 3]
# print(MakeIntersect1(['a', 'b'], ['b', 'c']))# --> ['b']

# # Membuat gabungan dari dua set
# print(MakeUnion([1, 2], [2, 3, 4]))         # --> [1, 2, 3, 4]
# print(MakeUnion(['a'], ['b', 'c']))         # --> ['a', 'b', 'c']

# # Membuat gabungan dengan cara kedua
# print(MakeUnion1([1, 2], [2, 3, 4]))        # --> [1, 2, 3, 4]
# print(MakeUnion1(['a'], ['b', 'c']))        # --> ['a', 'b', 'c']

# # Menghitung jumlah elemen irisan
# print(NBIntersect([1, 2, 3], [2, 3, 4]))    # --> 2
# print(NBIntersect(['a', 'b'], ['b', 'c']))   # --> 1

# # Menghitung jumlah elemen gabungan
# print(NBUnion([1, 2], [2, 3, 4]))           # --> 4
# print(NBUnion(['a'], ['b', 'c']))           # --> 3

# # Mengurutkan set
# print(sortSet([3, 1, 4, 5]))             # --> [1, 3, 4, 5]
# print(sortSet([10, 5, 2, 8]))               # --> [2, 5, 8, 10]

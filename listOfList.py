# Program     : listOfList.py
# Deskripsi   : Fungsi-fungsi untuk operasi set.
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : Rabu, 06 November 2024
# ================================================================================================================
# DEFINISI DAN SPESIFIKASI TYPE HIMPUNAN 

from listFunctions import *

# KONSTRUKTOR
#KonsLo : Atom/List, List of list → List of list
# { KonsLo(L,S) diberikan sebuah atom/list L dan sebuah List of List S, membentuk
# list baru dengan L sebagai elemen pertama List of list: L o S→ S'}
def KonsLo(L, S):
    return [L] + S

#KonsLi : List of list, Atom/List, → List of list
# # KonsL•(S,L) diberikan sebuah List of list S dan sebuah atom/list L, membentuk list baru 
# dengan L sebagai elemen terakhir List of list: S • L→ S'
def KonsLi(S, L):
    return S + [L]


# PREDIKAT DASAR
# IsEmpty : List of list → boolean
# { IsEmpty(S) benar jika S adalah list of list kosong }
def IsEmpty(S):
    return S == []
# Selektor elemen pertama
# FirstList: List of list tidak kosong → Atom/List
# { FirstList(S) menghasilkan elemen pertama list of list S, mungkin sebuah list atau
# atom }
def FirstList(S):
    if IsEmpty(S):
        return None
    return S[0]

# Selektor elemen terakhir
# LastList : List of list tidak kosong → Atom/List
# { LastList(S) menghasilkan elemen terakhir list of list S, mungkin list atau atom }
def LastList(S):
    if IsEmpty(S):
        return None
    return S[-1]

# TailList : List of list tidak kosong → List of list
# { TailList(S) menghasilkan "sisa" list of list S tanpa elemen pertama list of list S }
def TailList(S):
    if IsEmpty(S):
        return S
    else:
        return S[1:]
    
# HeadList : List of list tidak kosong → List of list
# { HeadList(S) menghasilkan "sisa" list of list S tanpa elemen terakhir list of list S }
def HeadList(S):
    if IsEmpty(S):
        return S
    else:
        return S[:-1]

# IsOneElmt : List of list -> boolean
# { IsOneElmt(S) benar jika S adalah list of list dengan 1 elemen}
def IsOneElmt(S):
    if IsEmpty(S):
        return False
    else:
        return IsEmpty(HeadList(S)) or IsEmpty(TailList(S))

# IsAtom : Atom/List → boolean
# { IsAtom(S) menghasilkan true jika list adalah atom, yaitu terdiri dari sebuah atom }
def IsAtom(S):
    return not isinstance(S, list)


# IsList : Atom/List → boolean
# { IsList(S) menghasilkan true jika S adalah sebuah list (bukan atom) }
def IsList(S):
    return  isinstance(S, list)

# IsEqS: 2 List of list → boolean
# { IsEqS(S1,S2) bernilai true jika S1 identik dengan S2: semua elemennya sama }
def IsEqS(S1, S2):
    if NbElmt(S1) != NbElmt(S2):
        return False
    else:
        if IsEmpty(S1) and IsEmpty(S2):
            return True
        else:
            if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
                return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1), TailList(S2))
            elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
                return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
            else:
                return False

#IsMemberS : elemen, List of list → boolean
#{ IsMemberS (A,S) true jika A adalah anggota S }
def IsMemberS(A, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == A:
                return True
            else:
                return IsMemberS(A, TailList(S))
        else:
            if IsMemberS(A, FirstList(S)):
                return True
            else:
                return IsMemberS(A, TailList(S))


# IsMemberLS : List, List of list → boolean
# { IsMemberLS (L,S) true jika L adalah anggota S}
def IsMemberLS(A, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
                return IsMemberLS(A, TailList(S))
        else:
            if IsEqS(FirstList(S), A):
                return True
            elif IsMemberLS(A, FirstList(S)):
                return True
            else:
                return IsMemberLS(A, TailList(S))


# Rember*: elemen, List of list → List of list
# { Rember*(a,S) menghapus semua kemunculan a pada list of list S. List kosong tetap
# menjadi list kosong }
def Rember(a, S):
    if IsEmpty(S):
        return S
    else:
        if IsAtom(FirstList(S)):
            if a == FirstList(S):
                return Rember(a, TailList(S))
            else:
                return KonsLo(FirstList(S), Rember(a, TailList(S)))
        else:
            return KonsLo(Rember(a, FirstList(S)), Rember(a, TailList(S)))
        
# MaxList : List of list tidak kosong → integer
# { MaxList(S) menghasilkan nilai elemen (atom) yang maksimum dari S }

def max2(x, y):
    return x if x > y else y

def MaxList(S):
    if IsEmpty(S):
        return float('-inf')  
    else:
        if IsAtom(FirstList(S)):
            return max2(FirstList(S), MaxList(TailList(S)))
        else:
            return max2(MaxList(FirstList(S)), MaxList(TailList(S)))
        
        

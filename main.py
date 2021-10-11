def list_is_progresion(l):
    if len(l) < 2:
        return True
    r = l[1] - l[0]
    for i in range(2,len(l)):
        if l[i]-l[i-1] != r:
            return False
    return True


def get_longest_arithmetic_progression(l):#verifica lista de marime maxima cu proprietatea ca toate elementele se afla in progresie aritmetica
    lis = []
    for  i in range(len(l)):
        for j in range(i, len(l)):
            if list_is_progresion and len(lis) < len(l[i:j+1]):
                lis = l[i:j+1]
    return lis


def test_get_longest_arithmetic_progression(): # testeaza functia (Toate elementele sunt in pr0gresie aritmetica)
    assert get_longest_arithmetic_progression([2,4,6]) == [2,4,6]
    assert get_longest_arithmetic_progression([1]) == [1]


def list_is_div(l, k):
    for x in l:
        if k % x != 0:
            return False
    return True


def test_is_div():
    assert list_is_div([],2) is True

def get_longest_div_k(l, k):#verifica daca toate elementele din lista sunt div de k
    lis = []
    for  i in range(len(l)):
        for j in range(i, len(l)):
            if list_is_div(l[i:j + 1], k) and len(lis) < len(l[i:j+1]):
                lis = l[i:j+1]
    return lis


def test_get_longest_div_k(): # testeaza functia (Toate elementele sunt div cu k)
    assert get_longest_div_k([2,2,2,2], 4) == [2,2,2,2]
    assert get_longest_div_k([], 2) == []


def number_is_palindrome(n):
    r = 0
    c = n
    while c > 0:
        r = r*10 + c%10
        c = c//10
    if n == r:
        return True
    return False


def list_is_palindromes(l):
    for i in range(len(l)):
        if number_is_palindrome(l[i]) is False:
            return False
    return True




def get_longest_all_palindromes(l): #verifica daca Toate numerele sunt palindroame.
    lis = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if list_is_palindromes(l[i:j+1]) == 1 and len(l[i:j+1]) > len(lis):
                lis = l[i:j+1]
    return lis

def test_get_longest_all_palindromes(): #functie de test (Toate numerele sunt palindroame.)
    assert get_longest_all_palindromes([121,11]) == [121,11]
    assert get_longest_all_palindromes([]) == []

def menu():
    print("1.Citire date.")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea 2")
    print("4.Determinare cea mai lungă subsecvență cu proprietatea 3")
    print("5.Iesire")


def main():
    test_get_longest_div_k()
    test_get_longest_all_palindromes()
    test_get_longest_arithmetic_progression()
    k = 0
    l = []

    while True:
        
        menu() #afiseaza meniul
        optiune = int(input("Alege optiunea: "))

        if optiune == 1: #citeste valorile ce urmeaza a fi folisite
            k = int(input("Citeste-l pe k(optional): ")) 
            l = input("Citeste lista(despartite cu virgula): ")
            l = l.split(",")
            for x in range(0,len(l)):
                l[x] = int(l[x])
        
        elif optiune == 2: #apelam proprietatea 1
            print(get_longest_div_k(l,k))
        elif optiune == 3:#apelam proprietatea 2
            print(get_longest_arithmetic_progression(l))
        elif optiune == 4:#apelam proprietatea 3
            print(get_longest_all_palindromes(l))

        elif optiune == 5:
            break
        else:
            print("Nu exista o astfel de optiune")


if __name__=="__main__": 
    main()

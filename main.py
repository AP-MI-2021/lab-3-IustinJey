def list_is_progresion(l):
    if len(l) < 2:
        return True
    r = l[1] - l[0]
    for i in range(2,len(l)):
        if l[i]-l[i-1] != r:
            return False
    return True


def get_longest_arithmetic_progression(l):
    lis = []
    for  i in range(len(l)):
        for j in range(i, len(l)):
            if list_is_progresion and len(lis) < len(l[i:j+1]):
                lis = l[i:j+1]
    return lis


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([2,4,6]) == [2,4,6]
    assert get_longest_arithmetic_progression([1]) == [1]


def list_is_div(l, k):
    for x in l:
        if k % x != 0:
            return False
    return True


def test_is_div():
    assert list_is_div([],2) is True

def get_longest_div_k(l, k):
    lis = []
    for  i in range(len(l)):
        for j in range(i, len(l)):
            if list_is_div(l[i:j + 1], k) and len(lis) < len(l[i:j+1]):
                lis = l[i:j+1]
    return lis


def test_get_longest_div_k():
    assert get_longest_div_k([2,2,2,2], 4) == [2,2,2,2]
    assert get_longest_div_k([], 2) == []


def menu():
    print("1.Citire date.")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea 2")
    print("4.Iesire")


def main():
    test_get_longest_div_k()
    k = 0
    l = []

    while True:
        
        menu()
        optiune = int(input("Alege optiunea: "))

        if optiune == 1:
            k = int(input("Citeste-l pe k(optional): "))
            l = input("Citeste lista(despartite cu virgula): ")
            l = l.split(",")
            for x in range(0,len(l)):
                l[x] = int(l[x])
        
        elif optiune == 2:
            proprietate = int(input("Alege Proprietatea(1 sau 2): "))
            if proprietate == 1:
                print(get_longest_div_k(l,k))
            if proprietate == 2:
                print(get_longest_arithmetic_progression(l))

        elif optiune == 3:
            break
        else:
            print("Nu exista o astfel de optiune")


if __name__=="__main__": 
    main()

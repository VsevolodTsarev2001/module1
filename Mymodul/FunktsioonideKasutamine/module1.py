def Summa(arv1:int,arv2:int,arv3=0)->int:
    """ Funktsioon tagastab kolme arvu summa
        Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3 
    return s
def IntKontroll() -> any:
    """ Funktsioon tagastab sissestatud andme õiges formaadis
        IntKontroll()
    :rtype: any
    """
    x = input("Sisestage andme: ")
    try:
        x = int(x)
        return "int"
    except:
        try:
            x = float(x)
            return "float"
        except:
            return "str"0

def arithmetic(x: int, y: int, op:str) -> float:
    """ Funktsioon tagastab kolme arvu summa
        arithmetic(x, y, op)
    :param int x: x sisestab kasutaja
    :param int y: y sisestab kasutaja
    :param str op: str sisestab kasutaja
    :rtype: int
    """
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if x == 0 or y == 0:
            print("jagamine nulliga ei ole võimalik")

sr = 0
пр = 0
def  часть (a,l,h):
    глобальный sr
    глобальный PR
    p = a [l]
    б = л
    для i в диапазоне (1 +l,h + 1):
        если  a [ i ] <= p :
            б + = 1
            пр + = 1
            a [i], a [b] = a [b], a [i]
    пр + = 1
    a [l],a [b] = a [b], a [l]
    вернуть б

def  qsort (a, l, h):
    глобальный sr
    глобальный PR
    sr+= 1
    если  l < h :
        p = часть (a, l, h)
        qsort (a , l, p - 1)
        qsort (a , p + 1 , h)
    вернуть а , ст , пр


c = список(карта( int , input().split()))
печать(qsort(c, 0, len (c) - 1))
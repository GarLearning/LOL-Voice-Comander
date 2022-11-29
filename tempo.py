import voz as v
"""
top
    tp
    flash
    ignite
    curar
jungle
    flash
    ignite
    curar
mid
    flash
    ignite
    tp
adc
    flash
    curar
suporte
    flash
    ignite
    curar
"""


def time_fen(voz):
    if voz[1] == "flash":
        sec = 300
    elif voz[1] == "tp":
        sec = 360
    elif voz[1] == "i":
        sec = 210
    elif voz[1] == "teste":
        sec = 45
    else:
        sec = 0
    print(sec)
    #return sec


fala = v.recvoz()
print(fala)
time_fen(fala)

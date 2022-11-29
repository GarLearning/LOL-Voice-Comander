import cronometro
import tempo
import voz
import sintz

# Just worked on version 3.6

v = voz.recvoz()
print(v)
t = tempo.time_fen(v)
voi = cronometro.crono(t)
sintz.sintz(voi)

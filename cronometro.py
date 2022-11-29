def crono(sec):
    from datetime import timedelta
    from sys import stdout
    from time import sleep

    tempo = timedelta(seconds=sec)
    print('\n')

    while str(tempo) != '0:00:00':
        stdout.write("\r%s" % tempo)
        stdout.flush()
        tempo = tempo - timedelta(seconds=1)

        sleep(1)

    stdout.write("\r0:00:00")
    stdout.flush()

    print("\ntempo finalizado")#som de tempo finalizado
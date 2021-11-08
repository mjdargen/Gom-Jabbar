# Gom Jabbar - gom_jabbar.py
# Michael D'Argenio
# mjdargen@gmail.com
# https://dargenio.dev
# https://github.com/mjdargen

import multiprocessing
from gj_processes import audio, ultra


def main():
    # creating a pipe to communicate between processes
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating processes
    audio_process = multiprocessing.Process(target=audio, args=(parent_conn,))
    ultra_process = multiprocessing.Process(target=ultra, args=(child_conn,))

    # be sure to kill processes if keyboard interrupted
    try:
        # starting audio process
        audio_process.start()
        # starting ultrasonic sensor process
        ultra_process.start()

        # wait until audio is finished
        audio_process.join()
        # if audio finished, kill ultrasonic sensor process
        ultra_process.terminate()
    except KeyboardInterrupt:
        print('Interrupted')
        audio_process.terminate()
        ultra_process.terminate()


if __name__ == '__main__':
    main()

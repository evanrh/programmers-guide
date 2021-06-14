import socket
import signal
import sys

defaultPassword = 'a-really-good-secret'
outputPassword = 'a-better-secret'
defaultPin = 8006

class Server:
    def __init__(self, password, pin):
        # Default INET TCP socket
        self.sock = socket.socket()
        self.sock.bind(("", 32006)) # Empty string means all interfaces
        self.bufSize = 1024
        self.pw = password
        self.pin = pin

    def run(self):
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        with conn:
            print("Connection from: " + str(addr))
            conn.send("Welcome to this \"secure\" server\n".encode())
            while True:
                data = conn.recv(self.bufSize).decode()
                if not data:
                    break
                elif data.strip() == " ".join([self.pw, str(self.pin)]):
                    print("Correct passphrase entered: ", data.strip())
                    msg = " ".join(["Correct!", f"The password is {outputPassword}"]) + '\n'
                    num = conn.send(msg.encode())
                    if num <= 0:
                        print(f"Did not send message. Only :{num}: bytes sent")
                    break
                else:
                    msg = "Wrong! Try again.\n"
                    conn.send(msg.encode())

    def stop(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

def main():
    serv = Server(defaultPassword, defaultPin)

    try:
        serv.run()
    except KeyboardInterrupt as e:
        print('Stopping from CTRL-C')
    except Exception as e:
        print(e)
    finally:
        print("Stopping server")
        serv.stop()

if __name__ == '__main__':
    main()

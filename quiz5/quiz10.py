deposito = 0
saldo = 500

class cuenta:
    def deposito(self, saldo):
        x = saldo - 200
        if saldo == 500:
            return x


    def retiro(self, saldo):
        m = saldo - 300
        if saldo == 500:
            return m




cuenta().deposito(saldo)
cuenta().retiro(saldo)

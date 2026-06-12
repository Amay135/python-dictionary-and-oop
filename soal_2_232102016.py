class Rekening:
    def __init__(self, saldo, limit):
        self.saldo = saldo
        self.limit = limit
        self.kredit_count = 0  

    def debit(self, jumlah):
        if jumlah > self.saldo:
            print("Gagal: Saldo tidak mencukupi.")
        elif jumlah > self.limit:
            print("Gagal: Jumlah debit melebihi limit.")
        else:
            self.saldo -= jumlah
            print(f"Berhasil: Debit {jumlah}. Saldo sekarang: {self.saldo}")

    def kredit(self, jumlah):
        if self.kredit_count >= 4:
            print("Gagal: Jumlah kredit sudah mencapai limit.")
        elif jumlah > self.limit:
            print("Gagal: Jumlah kredit melebihi limit.")
        else:
            self.saldo += jumlah
            self.kredit_count += 1
            print(f"Berhasil: Kredit {jumlah}. Saldo sekarang: {self.saldo}")

    def getSaldo(self):
        return self.saldo



rekening = Rekening(saldo=500, limit=1000)


rekening.kredit(300)   
rekening.debit(200)    
rekening.kredit(150)   
rekening.debit(800)    
rekening.kredit(1200)  
rekening.kredit(400)    
rekening.kredit(200)    

print(f"Saldo akhir: {rekening.getSaldo()}")

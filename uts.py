'''
Nama Angota :
1. Desta Ari Alfananda      (20051397008)
2. Dita Aulia 
3. Christopher Juliano W.S  (20051397050)
'''

class Cafe:
    def __init__(self):
        self.alternatif = ["QUBE", "Inti Kopi", "Kuni", "DeJavu"] #menentukan nama-nama cafe
        self.kriteria = ["Menu", "Rasa", "Harga", "Pelayanan"] #menentukan kriteria
        self.costbenefit = ["benefit", "benefit", "cost", "benefit"] #menentukan cost benefit
        self.kepentingan = [4, 5, 5, 3] #menentukan kepentingan nilainya dari 1-5
        self.alternatif_kriteria = [
            [20,32,41,55],
            [17,43,37,59],
            [54,72,24,96],
            [18,25,38,43]
        ] #menentukan nilai dari setiap alternatif
        self.bagi = []
        self.normal = []
        self.bobot = []
        
    def pembagi(self):
        for i in range(len(self.kriteria)):
            self.bagi.append(0)
            for j in range(len(self.alternatif)):
                self.bagi[i] = self.bagi[i] + (self.alternatif_kriteria[j][i]**2)
            self.bagi[i] = self.bagi[i]**(1/2)
        print (str(self.bagi)) 
        
    def normalisasi(self):
        for i in range(len(self.alternatif)):
            self.normal.append([])
            for j in range(len(self.kriteria)):
                self.normal[i].append(0)
                self.normal[i][j] = self.alternatif_kriteria[i][j]/self.bagi[j]
        print (self.normal)
        
    def terbobot (self):
        for i in range(len(self.alternatif)):
            self.bobot.append([])
            for j in range(len(self.kriteria)):
                self.bobot[i].append(0)
                self.bobot[i][j] = self.normal[i][j] * self.kepentingan[j]
        print(self.bobot)
        
    def aplus(self):
        self.ap = []
        for i in range(len(self.kriteria)):
            self.ap.append(0)
            if self.costbenefit[i] == "cost":
                for j in range(len(self.alternatif)):
                    if j == 0:
                        self.ap[i] = self.terbobot[j][i]
                    elif self.ap[i] > self.terbobot[j][i]:
                        self.ap[i] = self.terbobot[j][i]
            else :
                for j in range(len(self.alternatif)):
                    if j == 0:
                        self.ap[i] = self.terbobot[j][i]
                    elif self.ap[i] < self.terbobot[j][i]:
                        self.ap[i] = self.terbobot[j][i]
            
    def show(self):
        print("Alternatif : ", str(self.alternatif))
        print(self.pembagi())
        print(self.normalisasi())
        print(self.terbobot())
        
cafe = Cafe()
cafe.show()
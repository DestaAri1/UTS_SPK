'''
Nama Angota :
1. Desta Ari Alfananda      (20051397008)
2. Dita Aulia Oktavian      (20051397020)
3. Christopher Juliano W.S  (20051397050)
'''

alternatif = ["QUBE", "Inti Kopi", "Kuni", "DeJavu"] #menentukan nama-nama cafe
kriteria = ["Menu", "Rasa", "Harga", "Pelayanan"] #menentukan kriteria
costbenefit = ["benefit", "benefit", "cost", "benefit"] #menentukan cost benefit
kepentingan = [4, 5, 5, 3] #menentukan kepentingan nilai dari masing-masing kriteria 1-5
alternatif_kriteria = [
            [20,32,41,55],
            [17,43,37,59],
            [54,72,70,96],
            [18,25,38,43]
        ] #menentukan nilai dari setiap alternatif

#mencari matriks pembagi terlebih dahulu
pembagi = []
for i in range (len(kriteria)):
    pembagi.append(0)
    for j in range (len(alternatif)):
        pembagi[i] = pembagi[i] + (alternatif_kriteria[j][i]**2)
    pembagi[i] = pembagi[i]**(1/2)

#Menghitung matriks normalisasi
normalisasi = []
for i in range(len(alternatif)):
    normalisasi.append([])
    for j in range(len(kriteria)):
        normalisasi[i].append(0)
        normalisasi[i][j] = alternatif_kriteria[i][j]/pembagi[j]

#Menghitung matriks terbobot        
terbobot = []
for i in range(len(alternatif)):
    terbobot.append([])
    for j in range(len(kriteria)):
        terbobot[i].append(0)
        terbobot[i][j] = normalisasi[i][j] * kepentingan[j]
        
#menghitung jarak ideal positif negatif dengan A Plus dan A Min        
aplus = []
for i in range(len(kriteria)):
    aplus.append(0)
    if costbenefit[i] == "cost":
        for j in range(len(alternatif)):
            if j == 0:
                aplus[i] = terbobot[j][i]
            elif aplus[i] > terbobot[j][i]:
                aplus[i] = terbobot[j][i]
    else :
        for j in range(len(alternatif)):
            if j == 0:
                aplus[i] = terbobot[j][i]
            elif aplus[i] < terbobot[j][i]:
                aplus[i] = terbobot[j][i]

amin = []
for i in range(len(kriteria)):
    amin.append(0)
    if costbenefit[i] == "cost":
        for j in range(len(alternatif)):
            if j == 0:
                amin[i] = terbobot[j][i]
            elif amin[i] < terbobot[j][i]:
                amin[i] = terbobot[j][i]
    else :
        for j in range(len(alternatif)):
            if j == 0:
                amin[i] = terbobot[j][i]
            elif amin[i] > terbobot[j][i]:
                amin[i] = terbobot[j][i]  

#Menghitung jarak setiap alternatif dengan D Plus dan D min
dplus = []
for i in range(len(alternatif)):
    dplus.append(0)
    for j in range(len(kriteria)):
        dplus[i] = dplus[i] + ((aplus[j] - terbobot[i][j])**2)
        dplus[i] = dplus[i]**(1/2)

dmin = []
for i in range(len(alternatif)):
    dmin.append(0)
    for j in range(len(kriteria)):
        dmin[i] = dmin[i] + ((terbobot[i][j] - amin[j])**2)
        dmin[i] = dmin[i]**(1/2)

#Mencari nilai dari setiap cafe
hasil = []
for i in range(len(alternatif)):
    hasil.append(0)
    for j in range(len(kriteria)):
        hasil[i] = dmin[i] / (dmin[i] + dplus[i])
        
#mengurutkancafe dari nilai tertinggi ke rendah
alternatif_ranking = []
hasil_rangking = []
for i in range(len(alternatif)):
    hasil_rangking.append(hasil[i])
    alternatif_ranking.append(alternatif[i])
for i in range(len(alternatif)): #mengurutkan
    for j in range(len(alternatif)):
        if j > i:
            if hasil_rangking[j] > hasil_rangking[i]:
                tmphasil = hasil_rangking[i]
                tmpalternatif = alternatif_ranking[i]
                hasil_rangking[i] = hasil_rangking[j]
                alternatif_ranking[i] = alternatif_ranking[j]
                alternatif_ranking[j] = tmphasil
                alternatif_ranking[j] = tmpalternatif
        

print("Alternatif : ",str(alternatif))
print("Kriteria : ",str(kriteria))
print("Cost Benefit : ",str(costbenefit))
print("Kepentingan : ",str(kepentingan))
print("Alternatif Kriteria : ",str(alternatif_kriteria), "\n")
print("Hasil Matriks Pembagian : ",str(pembagi), "\n")
print("Hasil Matriks Normalisasi : ", str(normalisasi), "\n")
print("Hasil Matriks Terbobot : ", str(terbobot), "\n")
print("Nilai dari A^+ yaitu ", str(aplus))
print("Nilai dari A^- yaitu ", str(amin))
print("Nilai dari D^+ yaitu ", str(dplus))
print("Nilai dari D^- yaitu ", str(dmin),"\n")
print("Nama Cafe : ", alternatif)
print("Bernilai  : ",hasil, '\n')
print("Maka urutan rekomendasi cafe dengan metode topsis ini adalah :\n",alternatif_ranking)

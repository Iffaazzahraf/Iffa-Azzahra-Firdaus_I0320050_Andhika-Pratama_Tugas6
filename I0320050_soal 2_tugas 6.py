#menghitung nilai rata-rata
n = int(input("berapa jumlah data yang akan dimasukkan ?"))
data =[]
i =1
while i <=n:
    a = float(input("nilai ke-{}:".format(i)))
    data.append(float(a))
    i=1+i

average= sum(data)/n
print("nilai rata-rata dari data yang telah dimasukkan adalah",average)

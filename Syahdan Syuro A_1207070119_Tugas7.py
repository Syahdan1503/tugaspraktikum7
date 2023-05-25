
import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import cv2  #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt
import matplotlib.image as mpimg
from skimage import data#Mengimport data dari skimage

#Read Image
image = data.camera()
#Penerapan Histogram Equalization (HE)
image_equalized = cv2.equalizeHist(image)

#Penerapan Metode Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))

#Apply CLAHE to the original image
image_clahe = clahe.apply(image)

#Penerapan metode Contrast Stretching (CS)
# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')

# Apply Min-Max Contrasting
min = np.min(image)#Menghitung nilai minimum
max = np.max(image)#Menghitung nilai maksimum

for i in range(image.shape[0]):#Melakukan iterasi sebanyak jumlah baris
    for j in range(image.shape[1]):#Melakukan iterasi sebanyak jumlah kolom
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)#Fungsi rumus untuk melakukan kontrass streching
        
#Penerapan Metode Perkalian Konstanta
copyCamera = image.copy().astype(float) #Memmbuat salinan dari citra 'image' 

m1,n1 = copyCamera.shape#Mengambl dimensi baris 'm1' dan kolom 'n1' dari citra 'copy camera'
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):#Melakukan iterasi sebanyak jumlah baris 
    for kolom in range(0, n1-1):#Melakukan iterasi sebanyak jumlah kolom 
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9  #Pada setiap iterasi diatas nilai piksel dikalikan dengan 1.9      
        
#Plot Image
fig, axes = plt.subplots(5, 2, figsize=(20, 20))#Fungsi Subplot dengan ukuran 5x2 dan parameter 20, 20 yang menagtur ukuran keseluruhan plot
ax = axes.ravel()#Fungsi untuk membuat posisi rata pada grid gambar

ax[0].imshow(image, cmap=plt.cm.gray)#Menampilkan citra input pada sumbu pertama 
ax[0].set_title("Citra Input")#Memberi judul pada citra 
ax[1].hist(image.ravel(), bins=256)#Fungsi untuk membuat histogram dari 'Citra input'dan menampilkan nya pada sumbu kedua
ax[1].set_title('Histogram Input')#Memberi judul pada histogram

ax[2].imshow(image_equalized, cmap=plt.cm.gray)#Menampilkan citra hasil equalized pada sumbu ketiga
ax[2].set_title("Citra Output HE")#Memberi judul pada citra hasil equalized
ax[3].hist(image_equalized.ravel(), bins=256)#Fungsi untuk menampilkan histogram dari 'Citra output'
ax[3].set_title('Histogram Output HE Method')#Memberi judul pada histogram

ax[4].imshow(image_cs, cmap=plt.cm.gray)#Menampilkan citra hasil kontrass pada sumbu kelima 
ax[4].set_title("Citra Output CS")#Memberi judul pada citra 
ax[5].hist(image_cs.ravel(), bins=256)#Fungsi untuk membuat histogram pada citra 
ax[5].set_title('Histogram Output CS Method')#Memberi judul pada histogram

ax[6].imshow(image_clahe, cmap=plt.cm.gray)#Menampilkan citra hasil kontrass adaptif dengan metode CLAHE pada sumbu ketujuh
ax[6].set_title("Citra Grayscale CLAHE")#Memberi judul pada citra 
ax[7].hist(image_clahe.ravel(), bins=256)#Fungsi untuk membuat histogram 
ax[7].set_title('Histogram Output CLAHE Method')#Memberi judul pada histogram 

ax[8].imshow(output1, cmap=plt.cm.gray)#Menampilkan citra hasil perkalian konstan pada sumbu kesembilan
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#Memberi judul pada citra
ax[9].hist(output1.ravel(), bins=256)#Fungsi untuk membuat histogram
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#Memberi judul pada histogram

fig.tight_layout()#Menyesuaikan tata letak seluruh plot  
plt.show()

import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import cv2  #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt
from skimage import data#Mengimport data dari skimage 

img = data.camera() #Mengambil citra dari data camera

row, column = img.shape #Mengambil dimensi baris row dan kolom

img1 = np.zeros((row,column),dtype = 'uint8')#Membuat array
 

min_range = 10#Menentukan rentang minimum piksel
max_range = 60#Menentukan rentang maksimum piksel
 

for i in range(row):#Melakukan iterasi sebanyak jumlah baris
    for j in range(column):#Melakukan iterasi sebanyak jumlah kolom
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else:
            img1[i,j] = 0
            
fig, axes = plt.subplots(2, 2, figsize=(12, 12))#Fungsi subplot dengan ukuran 2x2 dan parameter 12,12 yang mengatur ukuran keseluruhan plot
ax = axes.ravel()#Fungsi untuk meratakan posisi pada grid gambar

ax[0].imshow(img, cmap=plt.cm.gray)#Menampilkan citra input pada sumbu pertama 
ax[0].set_title("Citra Input")#Memberi judul pada citra 
ax[1].hist(img.ravel(), bins=256)#Fungsi Membuat histogram 
ax[1].set_title('Histogram Input')#Memberi judul pada histogram 

ax[2].imshow(img1, cmap=plt.cm.gray)#Menampilkan citra hasil segmentasi pada sumbu ketiga
ax[2].set_title("Citra Output")#Memberi judul pada citra 
ax[3].hist(img1.ravel(), bins=256)#Fungsi untuk membuat histogram
ax[3].set_title('Histogram Output')#Memberi judul pada histogram

plt.show()

import matplotlib.pyplot as plt#Mengimport library dari matloblib dan menginisialisasi dengan plt
from skimage import data#Mengimport data dari skimage
from skimage.io import imread#Mengimport fungsi imread dari skimage
from skimage.color import rgb2gray #Mengimport rgb2gray
import numpy as np #Mengimport library dari numpy dengan inisialisasi np           
#load and plot image   
citra1 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\mobil.TIF')#Membaca citra mobil dan disimpan pada variabel citra1
citra2 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\boneka2.TIF')#Membaca citra boneka dan disimpan pada variabel citra2

print('Shape citra 1 : ', citra1.shape)#Mencetak ukuran citra1 dan memberinya judul 
print('Shape citra 2 : ', citra2.shape)#Mencetak ukuran citra2 dan memberinya judul

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Fungsi subplot dengan pada ukuran 1x2 dan parameter 10,10 yang mengatur ukura keseluruhan plot 
ax = axes.ravel()#Fungsi untuk meratakan posisi pada grid gambar

ax[0].imshow(citra1, cmap = 'gray')#Menmpilkan citra input pada sumbu pertama memnggunakan color map gray
ax[0].set_title("Citra 1") #Memberi judul judul pada citra 
ax[1].imshow(citra2, cmap = 'gray')#Fungsi untuk membuat histogram 
ax[1].set_title("Citra 2")#Memberi judul pada citra    


#Menyiapkan variable output
copyCitra1 = citra1.copy().astype(float)#Menyalin citra 1 dan menyimpannya dengan tyoe data float
copyCitra2 = citra2.copy().astype(float)#Menyalin citra2 dan menyimpnanya dengan type data float

m1,n1 = copyCitra1.shape#Mengambl dimensi baris 'm1' dan kolom 'n1' dari citra 'copycitra'
output1 = np.empty([m1, n1])#Membuat array kosong

m2,n2 = copyCitra2.shape#Mengambl dimensi baris 'm2' dan kolom 'n2' dari citra 'copycitra'
output2 = np.empty([m2, n2])#Membuat array kosong
print('Shape copy citra 1 : ', copyCitra1.shape)#Mencetak ukuran citra dari copyCitra1 dan memberinya judul
print('Shape output citra 1 : ', output1.shape)#Mencetak ukuran citra dari output1

print('m1 : ',m1)#Mencetak variabel m1
print('n1 : ',n1)#Mencetak variabel n1
print()

print('Shape copy citra 2 : ', copyCitra2.shape)#Mencetak ukuran citra dari copycitra 2
print('Shape output citra 3 : ', output2.shape)#Mencetak ukuran citra output dari output2  
print('m2 : ',m2)#Mencetak variabel m2
print('n2 : ',n2)#Mencetak variabel n2
print()

#Proses Filter Rerata Pada Citra Input 1
for baris in range(0, m1-1):#looping untuk mengiterasi setaip baris
    for kolom in range(0, n1-1):#looping untuk mengiterasi setiap kolom
        a1 = baris#Menyimpan nilai  baris pada variabel a1
        b1 = kolom#Menyimpan nilai kolom pada variabel b1
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1];#Menghitung jumlah piksel dalam lingkungan 
        output1[a1, b1] = (1/9 * jumlah)
#Proses Filter Rerata Pada Citra Input 2
for baris1 in range(0, m2-1):#looping untuk mengiterasi setaip baris
    for kolom1 in range(0, n2-1):#looping untuk mengiterasi setiap kolom
        a1 = baris1#Menyimpan nilai  baris pada variabel a1
        b1 = kolom1#Menyimpan nilai  kolom pada variabel b1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1];#Mengihitung jumlah piksel dalam lingkungan  
        output2[a1, b1] = (1/9 * jumlah)
#Plot Citra Input dan Output Hasil dari Filter Rerata
fig, axes = plt.subplots(2, 2, figsize=(10, 10))##Fungsi subplot dengan ukuran 2x2 dan parameter 10,10 yang mengatur ukuran keseluruhan plot
ax = axes.ravel()#Fungsi untuk meratak posisi citra pada grid

ax[0].imshow(citra1, cmap = 'gray')#Menampilkan variabel citra1 dengan colormap gray pada sumbu pertama 
ax[0].set_title("Input Citra 1")#Memberi judul pada citra

ax[1].imshow(citra2, cmap = 'gray')#Menampilkan variabel citra2 dengan colormap gray pada sumbu kedua
ax[1].set_title("Input Citra 1")#Memberi judul pada citra

ax[2].imshow(output1, cmap = 'gray')#Menampilkan variabel output1 dengan colormap gray pada sumbu ketiga
ax[2].set_title("Output Citra 1")#Memberi judul pada citra 

ax[3].imshow(output2, cmap = 'gray')#Menampilkan varibek output2 dengan colormap gray pada sumbu pertama
ax[3].set_title("Output Citra 2")#Memberikan judul pada citra
plt.show()

import matplotlib.pyplot as plt#Mengimport library dari matloblib dan menginisialisasi dengan plt
from skimage import data#Mengimport data dari skimage
from skimage.io import imread#Mengimport fungsi imread dari skimage
from skimage.color import rgb2gray #Mengimport rgb2gray
import numpy as np #Mengimport library dari numpy dengan inisialisasi np  
#load and plot image   
citra1 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\mobil.TIF')#Membaca citra mobil dan disimpan pada variabel citra1
citra2 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\boneka2.TIF')#Membaca citra boneka dan disimpan pada variabel citra2

print('Shape citra 1 : ', citra1.shape)#Mencetak ukuran citra1 dan memberinya judul 
print('Shape citra 2 : ', citra2.shape)#Mencetak ukuran citra2 dan memberinya judul

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Fungsi subplot dengan pada ukuran 1x2 dan parameter 10,10 yang mengatur ukura keseluruhan plot 
ax = axes.ravel()#Fungsi untuk meratakan posisi pada grid gambar

ax[0].imshow(citra1, cmap = 'gray')#Menmpilkan citra input pada sumbu pertama memnggunakan color map gray
ax[0].set_title("Citra 1") #Memberi judul judul pada citra 
ax[1].imshow(citra2, cmap = 'gray')#Fungsi untuk membuat histogram 
ax[1].set_title("Citra 2")#Memberi judul pada citra    


#Menyiapkan variable output
copyCitra1 = citra1.copy().astype(float)#Menyalin citra 1 dan menyimpannya dengan tyoe data float
copyCitra2 = citra2.copy().astype(float)#Menyalin citra2 dan menyimpnanya dengan type data float

m1,n1 = copyCitra1.shape#Mengambl dimensi baris 'm1' dan kolom 'n1' dari citra 'copycitra'
output1 = np.empty([m1, n1])#Membuat array kosong

m2,n2 = copyCitra2.shape#Mengambl dimensi baris 'm2' dan kolom 'n2' dari citra 'copycitra'
output2 = np.empty([m2, n2])#Membuat array kosong
print('Shape copy citra 1 : ', copyCitra1.shape)#Mencetak ukuran citra dari copyCitra1 dan memberinya judul
print('Shape output citra 1 : ', output1.shape)#Mencetak ukuran citra dari output1

print('m1 : ',m1)#Mencetak variabel m1
print('n1 : ',n1)#Mencetak variabel n1
print()

print('Shape copy citra 2 : ', copyCitra2.shape)#Mencetak ukuran citra dari copycitra 2
print('Shape output citra 3 : ', output2.shape)#Mencetak ukuran citra output dari output2  
print('m2 : ',m2)#Mencetak variabel m2
print('n2 : ',n2)#Mencetak variabel n2
print()

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output1[a1, b1] = dataA[5]   
for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output2[a1, b1] = dataA[5]       
        
#Plot Citra Input dan Output Hasil dari Filter Rerata
fig, axes = plt.subplots(2, 2, figsize=(10, 10))##Fungsi subplot dengan ukuran 2x2 dan parameter 10,10 yang mengatur ukuran keseluruhan plot
ax = axes.ravel()#Fungsi untuk meratak posisi citra pada grid

ax[0].imshow(citra1, cmap = 'gray')#Menampilkan variabel citra1 dengan colormap gray pada sumbu pertama 
ax[0].set_title("Input Citra 1")#Memberi judul pada citra

ax[1].imshow(citra2, cmap = 'gray')#Menampilkan variabel citra2 dengan colormap gray pada sumbu kedua
ax[1].set_title("Input Citra 1")#Memberi judul pada citra

ax[2].imshow(output1, cmap = 'gray')#Menampilkan variabel output1 dengan colormap gray pada sumbu ketiga
ax[2].set_title("Output Citra 1")#Memberi judul pada citra 

ax[3].imshow(output2, cmap = 'gray')#Menampilkan varibek output2 dengan colormap gray pada sumbu pertama
ax[3].set_title("Output Citra 2")#Memberikan judul pada citra
plt.show()


import matplotlib.pyplot as plt#Mengimport library dari matloblib dan menginisialisasi dengan plt
from skimage import data#Mengimport data dari skimage
from skimage.io import imread#Mengimport fungsi imread dari skimage
from skimage.color import rgb2gray #Mengimport rgb2gray
import numpy as np #Mengimport library dari numpy dengan inisialisasi np  
#load and plot image   
citra1 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\mobil.TIF')#Membaca citra mobil dan disimpan pada variabel citra1
citra2 = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\boneka2.TIF')#Membaca citra boneka dan disimpan pada variabel citra2

print('Shape citra 1 : ', citra1.shape)#Mencetak ukuran citra1 dan memberinya judul 
print('Shape citra 2 : ', citra2.shape)#Mencetak ukuran citra2 dan memberinya judul

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#Fungsi subplot dengan pada ukuran 1x2 dan parameter 10,10 yang mengatur ukura keseluruhan plot 
ax = axes.ravel()#Fungsi untuk meratakan posisi pada grid gambar

ax[0].imshow(citra1, cmap = 'gray')#Menmpilkan citra input pada sumbu pertama memnggunakan color map gray
ax[0].set_title("Citra 1") #Memberi judul judul pada citra 
ax[1].imshow(citra2, cmap = 'gray')#Fungsi untuk membuat histogram 
ax[1].set_title("Citra 2")#Memberi judul pada citra    


#Menyiapkan variable output
copyCitra1 = citra1.copy().astype(float)#Menyalin citra 1 dan menyimpannya dengan tyoe data float
copyCitra2 = citra2.copy().astype(float)#Menyalin citra2 dan menyimpnanya dengan type data float

m1,n1 = copyCitra1.shape#Mengambl dimensi baris 'm1' dan kolom 'n1' dari citra 'copycitra'
output1 = np.empty([m1, n1])#Membuat array kosong

m2,n2 = copyCitra2.shape#Mengambl dimensi baris 'm2' dan kolom 'n2' dari citra 'copycitra'
output2 = np.empty([m2, n2])#Membuat array kosong
print('Shape copy citra 1 : ', copyCitra1.shape)#Mencetak ukuran citra dari copyCitra1 dan memberinya judul
print('Shape output citra 1 : ', output1.shape)#Mencetak ukuran citra dari output1

print('m1 : ',m1)#Mencetak variabel m1
print('n1 : ',n1)#Mencetak variabel n1
print()

print('Shape copy citra 2 : ', copyCitra2.shape)#Mencetak ukuran citra dari copycitra 2
print('Shape output citra 3 : ', output2.shape)#Mencetak ukuran citra output dari output2  
print('m2 : ',m2)#Mencetak variabel m2
print('n2 : ',n2)#Mencetak variabel n2
print()

#Proses Filter Batas Pada Citra Input 1
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        
        a1 = baris
        b1 = kolom
        
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
        else :
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]
                
#Proses Filter Batas Pada Citra Input 2
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        
        a1 = baris1
        b1 = kolom1
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]                
#Plot Citra Input dan Output Hasil dari Filter batas
fig, axes = plt.subplots(2, 2, figsize=(10, 10))##Fungsi subplot dengan ukuran 2x2 dan parameter 10,10 yang mengatur ukuran keseluruhan plot
ax = axes.ravel()#Fungsi untuk meratak posisi citra pada grid

ax[0].imshow(citra1, cmap = 'gray')#Menampilkan variabel citra1 dengan colormap gray pada sumbu pertama 
ax[0].set_title("Input Citra 1")#Memberi judul pada citra

ax[1].imshow(citra2, cmap = 'gray')#Menampilkan variabel citra2 dengan colormap gray pada sumbu kedua
ax[1].set_title("Input Citra 1")#Memberi judul pada citra

ax[2].imshow(output1, cmap = 'gray')#Menampilkan variabel output1 dengan colormap gray pada sumbu ketiga
ax[2].set_title("Output Citra 1")#Memberi judul pada citra 

ax[3].imshow(output2, cmap = 'gray')#Menampilkan varibek output2 dengan colormap gray pada sumbu pertama
ax[3].set_title("Output Citra 2")#Memberikan judul pada citra
plt.show()

import matplotlib.pyplot as plt#Mengimport library dari matloblib dan menginisialisasi dengan plt
from skimage import data#Mengimport data dari skimage
from skimage.io import imread#Mengimport fungsi imread dari skimage
from skimage.color import rgb2gray #Mengimport rgb2gray
import numpy as np #Mengimport library dari numpy dengan inisialisasi np  

#Load Image
citra1 = imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\gedung.TIF')
print(citra1.shape)

plt.imshow(citra1, cmap='gray')#Menampilkan citra1 dengan colormap gray

#Proses Konvolusi
kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')#Menampilkan citra1 dengan color map gray pada sumbu pertama 
ax[0].set_title("Citra Input")#Memberi judul pada citra
ax[1].imshow(citraOutput, cmap = 'gray')#Menampilkan output citra 1 dengan colormap gray pada sumbu kedua 
ax[1].set_title("Citra Output")#Memberi judul pada citra 
plt.show()



# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
#jika menggunakan google colab jgn lupa load code di bawah ini
#from google.colab.patches import cv2_imshow


#bgr
img = cv2.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\naruto.JPG')

#rgb
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# tampilkan gambar awal tanpa filter
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5,5),np.float32)/25
print(kernel)

# lakukan filtering
naruto_filter = cv2.filter2D(img,-1,kernel)
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(naruto_filter)#Menampilkan citra1 dengan color map gray pada sumbu pertama 
ax[0].set_title("Citra filtering")#Memberi judul pada citra
ax[1].hist(naruto_filter.ravel(), bins=256)#Fungsi Membuat histogram 
ax[1].set_title('Histogram Input')#Memberi judul pada histogram 
plt.show()
cv2.imshow('Naruto',naruto_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
# salt and pepper
# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)

# plot pertama, gambar asli
plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])

# kedua, hasil filter
plt.subplot(122),plt.imshow(naruto_filter),
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Plot!
plt.show()

# ini adalah cara lain untuk membuat sebuah kernel, 
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]         
          ])/25
print(kernel)

# buat lagi filteringnya
naruto_filter = cv2.filter2D(img,-1,kernel)

# tampilkan
cv2.imshow('Image',naruto_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Highpass Filter

# sebenarnya kita tidak perlu melakukan filtering lagi. Cukup sekali saja 
# di bagian awal, selama notebook ini tetap terhubung
import cv2
import numpy as np
from matplotlib import pyplot as plt


# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\akainu.JPG',0)

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra 
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting 
plt.rcParams["figure.figsize"] = (20,20)


# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# Membuat histogram dari citra asli dengan skala warna 'gray'
plt.subplot(2, 3, 5)
plt.hist(img.ravel(), bins=256, color='gray')
plt.title('Histogram - Original')
plt.xlim(0, 255)

# Membuat histogram dari citra Laplacian dengan skala warna 'gray'
plt.subplot(2, 3, 6)
plt.hist(laplacian.ravel(), bins=256, color='gray')
plt.title('Histogram - Laplacian')
plt.xlim(0, 255)
plt.show()

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\batman.JPG',0)

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

# membaca gambar baymax 
img = cv2.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\Praktikum 7\batman.JPG',0)

# Hitungan threshold. 
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi 
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# menampilkan beberapa gambar sekaligus
for i in range(6):
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# masih menggunakan variabel img yang sama
#img = cv2.imread('images/baymax.jpg',0)

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

# menampilkan hasil
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



             
              
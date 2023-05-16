import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

st.title('Aplikasi Konsep Mol')

with st.sidebar :
    Pilihan = option_menu(menu_title=None,
              options=['Home','Massa ke Mol','Mol ke Massa','Volume Gas ke Mol','Mol ke Volume Gas','Jumlah Partikel ke Mol','Mol ke Jumlah Partikel','Molaritas ke Mol','Mol ke Molaritas','About Us'],
                         icons = ['house','bag-x','bag-x-fill','cloud-fog','cloud-fog-fill','geo','geo-fill','pie-chart','pie-chart-fill','mortarboard-fill'])
 

 #Pengertian Mol
if Pilihan == "Home" :
 
   """### gif from url"""
    st.markdown("![Alt Text](https://github.com/cikiwipkiii/deployment_webapppss/blob/main/gambar_1.gif)")
    
    st.write('\n')
    st.write('\n')
    
    st.markdown('Aplikasi Konsep :red[Mol] adalah aplikasi berbasis web streamlit yang berguna untuk membantu penggunanya memahami dan mengetahui rumus-rumus untuk mencari nilai :red[Mol] dari data-data yang sudah diketahui') 
    st.markdown('Sebelum kalian menggunakan web ini, kita kenalan dulu yuk sama istilah-istilah yang ada disini!')
    st.subheader('Pengertian Mol')
    st.markdown(':red[Mol] adalah jumlah suatu zat yang mengandung jumlah satuan dasar (atom, molekul dan ion) yang sama dalam atom-atom dalam 12 g isotop carbon (c-12)')
    st.subheader('Pengertian Molaritas')
    st.markdown('Molaritas adalah suatu ukuran kelarutan yang menyatakan jumlah mol suatu zat per volume larutan yang dilambangkan M dengan satuan mol/liter')
    st.subheader('Pengertian STP')
    st.markdown('STP atau Standard Temperature and Pressure adalah sebuah keadaan standar yang digunakan dalam pengukuran eksperimen. Memiliki nilai tetap yaitu 22,4')
    st.subheader('Pengertian Bilangan Avogadro')
    st.markdown('Bilangan Avogadro adalah banyaknya entitas dalam satu :red[Mol] yang merupakan jumlah atom karbon-12 dalam 12 gram (0,012 kilogram) karbon-12 dalam keadaan dasarnya')
    st.write('\n')
    
    st.image(Image.open("mol.png"))
    
    st.image(Image.open("tabel.png"))
    
    

#Diketahui Massa
if Pilihan =="Massa ke Mol" :
    st.latex(r'\boxed{n=\frac{Massa}{Ar}}') 
    Massa = st.number_input('Masukkan Nilai Massa (gram)')
    Ar = st.number_input('Masukkan Nilai Ar')

    tombol = st.button('hitung nilai Mol')

    if tombol:
        nilai_Mol = Massa/Ar
        st.success(f'Nilai Mol sebesar {nilai_Mol} n')
        st.balloons()
        
    
#Diketahui Mol
elif Pilihan =="Mol ke Massa" :
    st.latex(r'\boxed{m={mol}\enspace x\enspace {Ar}}') 
    Mol = st.number_input('Masukkan Nilai Mol (n)')
    Ar = st.number_input('Masukkan Nilai Ar')
    
    tombol = st.button('Hitung Nilai Massa')
    
    if tombol:
        nilai_Massa = Mol*Ar
        st.success(f'Nilai Massa sebesar {nilai_Massa} gram')
        st.balloons()
    

#Diketahui Volume
elif Pilihan == "Volume Gas ke Mol" :
    st.latex(r'\boxed{n=\frac{Volume}{STP}}') 
    Volume = st.number_input('Masukkan Nilai Volume')
    STP = st.number_input('Masukkan Nilai STP', value = 22.4, disabled = True)

    tombol = st.button('Hitung Nilai Mol')

    if tombol:
        nilai_Mol = Volume/STP
        st.success(f'Nilai Mol sebesar {nilai_Mol} n')
        st.snow()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Volume Gas" :
    st.latex(r'\boxed{V={mol}\enspace x\enspace {STP}}')
    Mol = st.number_input('Masukkan Nilai Mol')
    STP = st.number_input('Nilai STP ', value = 22.4, disabled = True)
    
    tombol = st.button('Hitung Nilai Volume')
    
    if tombol:
        nilai_Volume = Mol*STP
        st.success(f'Nilai Volume sebesar {nilai_Volume}')
        st.snow()
        
#Diketahui Jumlah Partikel
elif Pilihan == "Jumlah Partikel ke Mol" :
    st.latex(r'\boxed{n=\frac{JumlahPartikel}{BilAvogadro}}')
    Jumlah_Partikel = st.number_input('Masukkan Nilai Jumlah_Partikel')
    Bil_Avogrado = st.number_input('Masukkan Nilai Bil_Avogrado')
    
    tombol = st.button('Hitung Nilai Mol')
    
    if tombol:
        nilai_Mol = Jumlah_Partikel/Bil_Avogrado
        st.success(f'Nilai Mol sebesar {nilai_Mol} n')
        st.balloons()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Jumlah Partikel" :
    st.latex(r'\boxed{x={mol}\enspace x\enspace {BilAvogadro}}')
    Mol = st.number_input('Masukkan Nilai Mol')
    Bil_Avogrado = st.number_input('Masukkan Nilai Bil_Avogrado')
    
    tombol = st.button('Hitung Nilai Jumlah Partikel')
    
    if tombol:
        nilai_JumlahPartikel = Mol*Bil_Avogrado
        st.success(f'Nilai Jumlah Partikel sebesar {nilai_JumlahPartikel}')
        st.balloons()
        
#Diketahui Molaritas
elif Pilihan == "Molaritas ke Mol" :
    st.latex(r'\boxed{n={Molaritas}\enspace x\enspace {Volume}}')
    Molaritas = st.number_input('Masukkan Nilai Molaritas (mol/liter)')
    Volume = st.number_input('Masukkan Nilai Volume')
    
    tombol = st.button('Hitung Nilai Mol')
    
    if tombol:
        nilai_Mol = Molaritas*Volume
        st.success(f'Nilai Mol sebesar {nilai_Mol} n')
        st.snow()
        
        
#Diketahui Mol
elif Pilihan == "Mol ke Molaritas" :
    st.latex(r'\boxed{M=\frac{Mol}{Volume}}')
    Mol = st.number_input('Masukkan Nilai Mol')
    Volume = st.number_input('Masukkan Nilai volume')
    
    tombol = st.button('Hitung Nilai Molaritas')
    
    if tombol:
        nilai_Molaritas = Mol/Volume
        st.success(f'Nilai Molaritas sebesar {nilai_Molaritas} mol/liter')
        st.snow()
        
#Tentang Kita
elif Pilihan == "About Us" :
    
    st.header('YUK KENALAN SAMA KAMI :star2:')
    st.markdown('Assalamualaikum Wr. Wb. Perkenalkan kami dari Mahasiswa Politeknik AKA Bogor memperkenalkan web perhitungan konsep :red[Mol] yang telah berhasil kami buat. Terlebih untuk memenuhi kewajiban mata kuliah :green[Logika Pemrograman Komputer] dan memiliki tujuan mempermudah pekerjaan staff laboratorium serta para analis dalam menghitung jumlah :red[Mol] suatu zat')
    st.markdown('''Tim Penyusun :
1. Adyatma Fikry Fachrezi (NIM 2260002)
2. Faika Ahda Rosyadi (NIM 2260013)
3. Kalyca Agatha Zahra (NIM 2260024)
4. Nisa Widia Wulandari (NIM 2260035)
5. Rifqi Farihan Azis (NIM 2260046)
6. Zahda Aulia Bahrudin (NIM 2260057)''')
    st.markdown('Kami berharap web perhitungan :red[Mol] ini bermanfaat bagi para penggunanya. Wassalammualaikum Wr.Wb.')

else :
    st.write()


       

   

# looping program
while True:

    # masukkan nama lengkap
    nama_lengkap = input('Masukkan nama lengkap anda : ')

    # masukkan nim
    nim = input('Masukkan nim kamu : ')

    # masukkan jurusan
    jurusan = input('Masukkan jurusan kamu : ')

    # tampilkan hasil nya
    print(f"""
======HASIL=====
1. Nama lengkap kamu : {nama_lengkap}
2. NIM kamu : {nim}
3. Jurusan kamu : {jurusan}
    """)

    # tanya jika kamu ingin mengulang lagi
    tanya = input('Apakah kamu mau mengulang lagi?[y/n] : ')

    # cek jika kamu menekan y artinya iya 
    if tanya == 'y':
        # tetapkan program untuk looping
        continue

    # cek jika kamu menekan n artinya tidak
    elif tanya == 'n':
        # hentikan program
        break
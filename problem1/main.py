# input
student_score = 80
# Process: Your Solution Code Here
# Output "Nilai A"
def nilai_deskripsi(nilai):
    if nilai >= 80 and nilai <= 100:
        return "A"
    elif nilai >= 65 and nilai <= 79:
        return "B+"
    elif nilai >= 50 and nilai <= 64:
        return "B"
    elif nilai >= 35 and nilai <= 49:
        return "C"
    elif nilai >= 0 and nilai <= 34:
        return "D"
    else:
        return "Nilai tidak valid"

student_score = int(input("Masukkan nilai mahasiswa: "))

deskripsi_nilai = nilai_deskripsi(student_score)
print("Nilai:", deskripsi_nilai)

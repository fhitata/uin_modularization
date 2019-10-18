nama = 'fitrianingsih'
program = 'gaya'

print(f'program {program} oleh {nama}')

def hitung_gaya(massa,percepatan):
    gaya = massa / percepatan
    print(f'massa kg = {massa} kg per satuan percepatan = m/s^2')
    print(f'sehingga gaya = {gaya} Newton')
    return gaya

# massa = 1000
# percepatan = 20
gaya = hitung_gaya(1000, 20)
gaya = hitung_gaya(7000, 35)
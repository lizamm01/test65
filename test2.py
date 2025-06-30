import re
import time

def malumot_korish(funksiya):
    def wrapper(*args, **kwargs):
        print(f"\n[{funksiya.__name__}] funksiyasi ishga tushdi.")
        boshlanish_vaqti = time.time()
        natija = funksiya(*args, **kwargs)
        tugash_vaqti = time.time()
        print(f"Amal bajarilish vaqti: {round(tugash_vaqti - boshlanish_vaqti, 4)} sekund\n")
        return natija
    return wrapper


class KontaktMenedjer:
    def __init__(self):
        self.kontaktlar = []

    @malumot_korish
    def kontakt_qoshish(self, ism, telefon):

        if not re.fullmatch(r"[A-Za-z\s]+", ism):
            print("Xatolik! Ism faqat harflardan iborat bo'lishi kerak.")
            return


        if not re.fullmatch(r"(\+998)?\d{9}", telefon):
            print("Xatolik! Telefon raqam noto'g'ri kiritildi.")
            return

        self.kontaktlar.append({"ism": ism, "telefon": telefon})
        print(f"Kontakt qo'shildi: Ism: {ism}, Telefon: {telefon}")

    @malumot_korish
    def barcha_kontaktlarni_korish(self):
        if not self.kontaktlar:
            print("Kontaktlar ro'yxati bo'sh.")
        else:
            print("\nKontaktlar ro'yxati:")
            for i, kontakt in enumerate(self.kontaktlar, 1):
                print(f"{i}. {kontakt['ism']} - {kontakt['telefon']}")

    @malumot_korish
    def kontakt_ochirish(self, indeks):
        if 0 <= indeks < len(self.kontaktlar):
            ochirilgan = self.kontaktlar.pop(indeks)
            print(f"Kontakt o'chirildi: {ochirilgan['ism']} - {ochirilgan['telefon']}")
        else:
            print("Xatolik! Noto'g'ri raqam kiritildi.")


menedjer = KontaktMenedjer()

while True:
    print("\n Menyu:")
    print("1. Kontakt qo'shish")
    print("2. Hamma kontaktlarni ko'rish")
    print("3. Kontakt o'chirish")
    print("4. Chiqish")

    tanlov = input("Tanlang (1-4): ")

    if tanlov == '1':
        ism = input("Ismni kiriting: ")
        telefon = input("Telefon raqamni kiriting: ")
        menedjer.kontakt_qoshish(ism, telefon)

    elif tanlov == '2':
        menedjer.barcha_kontaktlarni_korish()

    elif tanlov == '3':
        menedjer.barcha_kontaktlarni_korish()
        try:
            raqam = int(input("O'chirmoqchi bo'lgan kontak idsini kiriting (1, 2, ...): ")) - 1
            menedjer.kontakt_ochirish(raqam)
        except ValueError:
            print("Xatolik! Raqam kiritish kerak.")

    elif tanlov == '4':
        print("Dastur yakunlandi. Xayr!")
        break

    else:
        print("Xatolik! To'g'ri tanlov kiriting.")
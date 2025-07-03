import re
import time

def log_qil(func):
    def owrap(*args, **kwargs):
        print(f"\n[{func.__name__}] funksiyasi chaqirildi.")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Amal bajarilish vaqti: {round(end - start, 4)} soniya\n")
        return result
    return owrap

class Kontaktlar:
    def __init__(self):
        self.royxat = []

    @log_qil
    def qoshuv(self, ism, raqam):
        if not re.fullmatch(r"[A-Za-z\s]+", ism):
            print("Xatolik! Ism faqat harflardan iborat bo'lishi kerak.")
            return
        if not re.fullmatch(r"(\+998)?\d{9}", raqam):
            print("Xatolik! Telefon raqam noto'g'ri kiritildi.")
            return

        self.royxat.append({"ism": ism, "raqam": raqam})
        print(f"Kontakt qo'shildi: {ism} - {raqam}")

    @log_qil
    def korish(self):
        if not self.royxat:
            print("Kontaktlar bo'sh.")
        else:
            print("Kontaktlar ro'yxati:")
            for i, kontakt in enumerate(self.royxat, 1):
                print(f"{i}. {kontakt['ism']} - {kontakt['raqam']}")

    @log_qil
    def ochirish(self, indeks):
        if 0 <= indeks < len(self.royxat):
            olingan = self.royxat.pop(indeks)
            print(f"O'chirildi: {olingan['ism']} - {olingan['raqam']}")
        else:
            print("Xatolik! Noto'g'ri indeks.")

class SMS(Kontaktlar):
    def __init__(self):
        super().__init__()
        self.smslar = []

    def yuborish(self):
        if not self.royxat:
            print("Kontaktlar yo'q.")
            return
        for i, kontakt in enumerate(self.royxat, 1):
            print(f"{i}. {kontakt['ism']} - {kontakt['raqam']}")
        tanlov = int(input("Qaysi kontaktga SMS yubormoqchisiz (raqamini kiriting): ")) - 1
        if 0 <= tanlov < len(self.royxat):
            matn = input("SMS matnini kiriting: ")
            sms = {"kimga": self.royxat[tanlov], "matn": matn}
            self.smslar.append(sms)
            print("SMS yuborildi!")
        else:
            print("Noto‘g‘ri tanlov.")

    def sms_korish(self):
        if not self.smslar:
            print("SMSlar bo'sh.")
        else:
            for i, sms in enumerate(self.smslar, 1):
                print(f"{i}. {sms['kimga']['ism']} - {sms['matn']}")

    def sms_ochirish(self, indeks):
        if 0 <= indeks < len(self.smslar):
            ochgan = self.smslar.pop(indeks)
            print(f"{ochgan['kimga']['ism']} ga yuborilgan SMS o‘chirildi.")
        else:
            print("Xatolik! Noto‘g‘ri indeks.")


sms = SMS()

while True:
    print("\n1. Kontaktlar")
    print("2. SMS")
    print("3. Chiqish")

    tanlov = input("Tanlovni kiriting (1-3): ")

    if tanlov == '1':
        while True:
            print("\n-- Kontaktlar --")
            print("1. Kontakt qo'shish")
            print("2. Kontaktlarni ko'rish")
            print("3. Kontaktni o'chirish")
            print("4. Orqaga")

            tanlov2 = input("Tanlovni kiriting (1-4): ")

            if tanlov2 == '1':
                ism = input("Ismni kiriting: ")
                raqam = input("Telefon raqamni kiriting: ")
                sms.qoshuv(ism, raqam)

            elif tanlov2 == '2':
                sms.korish()

            elif tanlov2 == '3':
                sms.korish()
                try:
                    index = int(input("Qaysi kontaktni o'chirmoqchisiz (raqamini kiriting): ")) - 1
                    sms.ochirish(index)
                except ValueError:
                    print("Xatolik! Raqam kiritilishi kerak edi.")
            elif tanlov2 == '4':
                break
            else:
                print("Noto'g'ri tanlov.")

    elif tanlov == '2':
        while True:
            print("\n-- SMS --")
            print("1. SMS yuborish")
            print("2. SMSlarni ko'rish")
            print("3. SMS o'chirish")
            print("4. Orqaga")

            tanlov3 = input("Tanlovni kiriting (1-4): ")

            if tanlov3 == '1':
                sms.yuborish()

            elif tanlov3 == '2':
                sms.sms_korish()

            elif tanlov3 == '3':
                sms.sms_korish()
                try:
                    index = int(input("Qaysi SMSni o'chirmoqchisiz (raqamini kiriting): ")) - 1
                    sms.sms_ochirish(index)
                except ValueError:
                    print("Xatolik! Raqam kiritilishi kerak edi.")
            elif tanlov3 == '4':
                break
            else:
                print("Noto‘g‘ri tanlov.")

    elif tanlov == '3':
        print("Dastur tugadi.")
        break
    else:
        print("Noto‘g‘ri tanlov.")
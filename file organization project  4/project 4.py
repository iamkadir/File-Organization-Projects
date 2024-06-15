import csv

class Kitap:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

class Library:
    def __init__(self, DosyaAdi):
        self.kitap = []
        self.load_data(DosyaAdi)

    def load_data(self, DosyaAdi):
        with open(DosyaAdi, 'r', encoding='utf-8') as file:
            oku = csv.reader(file)
            next(oku)  # İlk satırız cunku başlık
            for satir in oku:
                title, author, year, isbn = satir
                self.kitap.append(Kitap(title, author, year, isbn))

    def linear_arama(self, keyword):
        kitap_bul = []
        for kitap in self.kitap:
            if keyword.lower() in kitap.title.lower() or keyword.lower() in kitap.author.lower():
                kitap_bul.append(kitap)
        return kitap_bul
    
    def hash_arama(self, keyword):
        hash_table = {}
        for kitap in self.kitap:
            hash_table[hash(kitap.title.lower())] = kitap
            hash_table[hash(kitap.author.lower())] = kitap  

        key = hash(keyword.lower())
        if key in hash_table:
            return hash_table[key]
        else:
            return None

    def kitap_arama(self, keyword, method):
        if method == 'linear':
            result = self.linear_arama(keyword)
        elif method == 'hash':
            result = self.hash_arama(keyword)
        else:
            return "Geçersiz arama yöntemi!"

        if result:
            if isinstance(result, list):
                for kitap in result:
                    print(f"Kitap adı: {kitap.title}, Yazarı: {kitap.author}, Yayın Yılı: {kitap.year}, ISBN: {kitap.isbn}")
            else:
                print(f"Kitap adı: {result.title}, Yazarı: {result.author}, Yayın Yılı: {result.year}, ISBN: {result.isbn}")
        else:
            print("Kitap bulunamadı.")

# Kullanım örneği:
library = Library("tr_books.csv")
search_method = input("Arama yöntemi seçin (linear/hash): ")
keyword = input("Aranacak kitap adı veya yazarı: ")

library.kitap_arama(keyword, search_method)

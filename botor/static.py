from telegraph import Telegraph

ABOUT_US = '🧑‍🏫Biz haqimizda'
ADDRESS = '📍manzil'
CONTACT = '☎️Kontact'
COURSE = '📚Course'
My_CONTACT = '📲SHARE my contact'
MY_LOCATION = '📍SHARE my location'
FAQ = 'FAQ'
QUESTION = """
1 Ustozlarni malakasi qanday? 
2. Kursda SERTIFIKAT beriladimi?  
3. SERTIFIKATning qanday imtiyozlari mavjud?  
4. Bitirgandan keyin ishga kirishga GARANTIYA bormi? 
5. Sharoitlar talabga javob beradimi? 

Javooblarni olish uchun pastdagi tugmalarni bosing 
/quiz_1
/quiz_2
/quiz_3
/quiz_4
/quiz_5

"""
ANSWER = """
1. Ustozlarni malakasi qanday?  
Bizning ustozlarimiz o‘z sohasida tajribali va yuqori malakaga ega mutaxassislardir. Ular ko‘plab muvaffaqiyatli loyihalar amalga oshirgan hamda talabalarga o‘z bilimlarini tushunarli va samarali tarzda yetkazib bera olishadi.
"""
ANSWER_2 = """
2. Kursda SERTIFIKAT beriladimi?  
Ha, kursni muvaffaqiyatli tamomlagan barcha talabalar xalqaro va mahalliy me'yorlarga mos sertifikatga ega bo‘lishadi.
"""
ANSWER_3 = """
3. SERTIFIKATning qanday imtiyozlari mavjud?  
Sertifikat ko‘plab IT-kompaniyalar tomonidan tan olinadi va sizning bilim va ko‘nikmalaringizni tasdiqlaydi. Bu ishga joylashish jarayonida katta ustunlik bo‘lib xizmat qilishi mumkin.
"""
ANSWER_4 = """
4. Bitirgandan keyin ishga kirishga GARANTIYA bormi?  
Biz o‘z talabalarimizga sifatli bilim va ko‘nikmalarni berishga kafolat beramiz. Shuningdek, bizning hamkor kompaniyalarimiz bilan ishga joylashishga yordam beramiz. Ammo kafolatli ish joyi individual natijalar va sa’y-harakatlarga bog‘liq bo‘ladi.
"""
ANSWER_5 = """
5. Sharoitlar talabga javob beradimi?  
Ha, darslar zamonaviy texnologiyalar bilan jihozlangan qulay o‘quv muhitida o‘tadi. Talabalar uchun barcha kerakli sharoitlar, jumladan, kompyuterlar, internet va qulay o‘quv materiallari taqdim etiladi.
"""
telegraph=Telegraph()
telegraph.create_account(short_name="newseser")
respons=telegraph.create_page(
    title="FAQ",
    content=[
  {
            "tag": "h3",
            "children": [
                "faq"
            ]
    },
    {
            "tag": "h3",
            "children": ["1. Ustozlarni malakasi qanday?  "]
    },
    {
            "tag": "p",
            "children": [
                "Bizning ustozlarimiz o‘z sohasida tajribali va yuqori malakaga ega mutaxassislardir. Ular ko‘plab muvaffaqiyatli loyihalar amalga oshirgan hamda talabalarga o‘z bilimlarini tushunarli va samarali tarzda yetkazib bera olishadi.  "]
    },
        {
            "tag": "h3",
            "children": [
                "2. Kursda SERTIFIKAT beriladimi?  "]
        },
     {
            "tag": "h3",
            "children": [
                " Ha, kursni muvaffaqiyatli tamomlagan barcha talabalar xalqaro va mahalliy me'yorlarga mos sertifikatga ega bo‘lishadi."]
     },
     {
            "tag": "h3",
            "children": [
                "3. SERTIFIKATning qanday imtiyozlari mavjud?   "]
     },
     {
            "tag": "h3",
            "children": [
                " Sertifikat ko‘plab IT-kompaniyalar tomonidan tan olinadi va sizning bilim va ko‘nikmalaringizni tasdiqlaydi. Bu ishga joylashish jarayonida katta ustunlik bo‘lib xizmat qilishi mumkin.  "]
     },
     {
            "tag": "h3",
            "children": [
                "4. Bitirgandan keyin ishga kirishga GARANTIYA bormi?"]
    },
     {
            "tag": "h3",
            "children": [
                "Biz o‘z talabalarimizga sifatli bilim va ko‘nikmalarni berishga kafolat beramiz. Shuningdek, bizning hamkor kompaniyalarimiz bilan ishga joylashishga yordam beramiz. Ammo kafolatli ish joyi individual natijalar va sa’y-harakatlarga bog‘liq bo‘ladi."]
    },
     {
            "tag": "h3",
            "children": [
                "5. Sharoitlar talabga javob beradimi? "]
    },
    {
            "tag": "h3",
            "children": [
                "Ha, darslar zamonaviy texnologiyalar bilan jihozlangan qulay o‘quv muhitida o‘tadi. Talabalar uchun barcha kerakli sharoitlar, jumladan, kompyuterlar, internet va qulay o‘quv materiallari taqdim etiladi. "]
     },
        {
            "tag":"h3"
            "children":""
        }


],
    author_name="test bot",
    author_url="https://t.me/@tetrisesdefbot"
)
TELEGRAPH_LINK=f"<a href='{respons['url']}'>FAQ!</a>"


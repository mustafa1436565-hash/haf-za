import random
sen_p = 0
bot_p = 0
x = ["taş","kağıt","makas"]
while True:
    bot = random.choice(x)
    sen = input("Seç:").lower()
    print("Botun seçimi:",bot)
    if bot == sen:         
        print("Berabere")
    elif bot == "taş" and sen == "kağıt" or bot == "kağıt" and sen == "makas" or bot == "makas" and sen == "taş":        
        print("Kazandın")
        sen_p += 1
    elif bot == "taş" and sen == "makas" or bot == "makas" and sen == "kağıt" or bot == "kağıt" and sen == "taş":
        print("Kaybettin")
        bot_p += 1 
    else:
        print("Hatalı Giriş")
    print(f"Sen:{sen_p} Bot:{bot_p}")
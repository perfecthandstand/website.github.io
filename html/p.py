email = input("請輸入您的電子郵件地址： ")
domain = email.split('@')[-1]  # 獲取域名部分
print(email)
# 判斷域名屬於熱門還是自定義
if domain in ['gmail.com', 'yahoo.com', 'hotmail.com']:
    print("這是註冊在熱門域名之下的 Email 地址")
else:
    print(f"這是在 {domain.capitalize()} 之下自定義域")

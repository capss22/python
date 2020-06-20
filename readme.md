# 找出兩首詩共同的字
```
p1 = '紅豆生南國，春來發幾枝？願君多采擷，此物最相思。'
p2 = '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
s1 = set(p1)
s1.remove('，')
s1.remove('。')
s1.remove('？')
s2 = set(p2)
s2.remove('，')
s2.remove('。')
print(s1&s2)
```

# Hello world
```
print("Hello World")
```

# 求三數總和與平均
```
fir = int(input('請輸入第一次期中考成績？'))
sec = int(input('請輸入第二次期中考成績？'))
final = int(input('請輸入期末考成績？'))
sum = fir + sec + final
avg = sum/3
print('總分為', sum, '平均為', avg)
```
# 及格
```
score = int(input('請輸入一個成績？'))
if score >= 60:
    print('很好，請繼續保持下去')
```

# 密碼強度
```
def check(pwd):
    if pwd.isdigit():
        if len(pwd) < 6:
            return '不安全的密碼'
        else:
            return '可能是安全的密碼'
    elif pwd.isalpha():
        if len(pwd) < 6:
            return '不安全的密碼'
        else:
            return '可能是安全的密碼'
    elif len(pwd) < 6:
        return '不安全的密碼'
    elif len(pwd) < 10:
        return '安全的密碼'
    else:
        return '非常安全的密碼'
pwd = input('請輸入密碼？')
sec = check(pwd)
print(pwd, '為', sec)
```

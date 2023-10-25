for i in range(3):
    #文字だからダブルコーテーション
    print(i,"人目")
    name=input("名前を入れてください")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    #A and Bで両方を満たしている場合のみ
    if waist>=85 and age>=40:
        print(name,"さん、メタボです。痩せましょう。")
    else:
        print(name,"さん、腹囲は問題ありません")

    #整数に変換したい場合-----------> int() 小数点もある数に変換したい場合---> float()


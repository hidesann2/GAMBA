import random

Default_Balance = 20000
Small_Bet = 1000
Small_Range = range(1, 10)
Medium_Bet = 2000
Medium_Range = range(1,20)
Large_Bet = 3000
Large_Range = range(1,30)
AI_Bet = 5000
AI_Range = range(1,50)
Number_Bot = 0

def Easy_Mode():
    New_Balance = Default_Balance

    while True:
        Number_Bot = int(random.choice(Small_Range))

        while True:
            try:
                Number_User = int(input("Hãy nhập số của bạn (Lớn hơn 0, nhỏ hơn bằng 10 ) "))
                if 0 <= Number_User <= 10:
                    break
                else:
                    print("Vui lòng nhập lại số từ 0 tới 10")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")

        print(f"Số của bạn là :", Number_User)
        print(f"Số của bot là :", Number_Bot)

        if Number_User > Number_Bot:
            print(f"Bạn đã thắng UwU ")
            New_Balance += Small_Bet
            print(f"Điểm sau khi thắng của bạn là ", New_Balance)
        elif Number_User < Number_Bot:
            print(f"Bạn đã thua TvT ")
            New_Balance -= Small_Bet
            print(f"Điểm sau khi thua của bạn là ", New_Balance)
        else:
            print(f"Hòa, số điểm không đổi")

        Continue = input("Bạn có muốn chơi tiếp không? (Y/N): ")
        if Continue.lower() != "y":
            print(f"Điểm cuối cùng của bạn là ", New_Balance)
        break

def Medium_Mode():
    New_Balance = Default_Balance

    while True:
        Number_Bot = int(random.choice(Medium_Range))

        while True:
            try:
                Number_User = int(input("Hãy nhập số của bạn (Lớn hơn 0, nhỏ hơn bằng 20 ) "))
                if 0 <= Number_User <= 20:
                    break
                else:
                    print("Vui lòng nhập lại số từ 0 tới 20")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")

        print(f"Số của bạn là :", Number_User)
        print(f"Số của bot là :", Number_Bot)

        if Number_User > Number_Bot:
            print(f"Bạn đã thắng UwU ")
            New_Balance += Medium_Bet
            print(f"Điểm sau khi thắng của bạn là ", New_Balance)
        elif Number_User < Number_Bot:
            print(f"Bạn đã thua TvT ")
            New_Balance -= Medium_Bet
            print(f"Điểm sau khi thua của bạn là ", New_Balance)
        else:
            print(f"Hòa, số điểm không đổi")

        Continue = input("Bạn có muốn chơi tiếp không? (Y/N): ")
        if Continue.lower() != "y":
            print(f"Điểm cuối cùng của bạn là ", New_Balance)
        break
def Hard_Mode():
    New_Balance = Default_Balance

    while True:
        Number_Bot = int(random.choice(Large_Range))

        while True:
            try:
                Number_User = int(input("Hãy nhập số của bạn (Lớn hơn 0, nhỏ hơn bằng 30 ) "))
                if 0 <= Number_User <= 30:
                    break
                else:
                    print("Vui lòng nhập lại số từ 0 tới 30")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")

        print(f"Số của bạn là :", Number_User)
        print(f"Số của bot là :", Number_Bot)

        if Number_User > Number_Bot:
            print(f"Bạn đã thắng UwU ")
            New_Balance += Large_Bet
            print(f"Điểm sau khi thắng của bạn là ", New_Balance)
        elif Number_User < Number_Bot:
            print(f"Bạn đã thua TvT ")
            New_Balance -= Large_Bet
            print(f"Điểm sau khi thua của bạn là ", New_Balance)
        else:
            print(f"Hòa, số điểm không đổi")

        Continue = input("Bạn có muốn chơi tiếp không? (Y/N): ")
        if Continue.lower() != "y":
            print(f"Điểm cuối cùng của bạn là ", New_Balance)
        break
def Extreme_Mode():
    New_Balance = Default_Balance

    while True:
        Number_Bot = int(random.choice(AI_Range))

        while True:
            try:
                Number_User = int(input("Hãy nhập số của bạn (Lớn hơn 0, nhỏ hơn bằng 50 ) "))
                if 0 <= Number_User <= 50:
                    break
                else:
                    print("Vui lòng nhập lại số từ 0 tới 50")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ")

        print(f"Số của bạn là :", Number_User)
        print(f"Số của bot là :", Number_Bot)

        if Number_User > Number_Bot:
            print(f"Bạn đã thắng UwU ")
            New_Balance += AI_Bet
            print(f"Điểm sau khi thắng của bạn là ", New_Balance)
        elif Number_User < Number_Bot:
            print(f"Bạn đã thua TvT ")
            New_Balance -= AI_Bet
            print(f"Điểm sau khi thua của bạn là ", New_Balance)
        else:
            print(f"Hòa, số điểm không đổi")

        Continue = input("Bạn có muốn chơi tiếp không? (Y/N): ")
        if Continue.lower() != "y":
            print(f"Điểm cuối cùng của bạn là ", New_Balance)
        break

def Choose_Mode():
    while True:
        print(f"Chọn mức chơi : ")
        print(f"1/ Easy (1000)")
        print(f"2/ Medium (2000)")
        print(f"3/ Hard (3000)")
        print(f"4/ Extreme (5000)")
        print(f"5/ Exit ")
        Mode = input()
        if Mode == "1":
            Easy_Mode()
        elif Mode == "2":
            Medium_Mode()
        elif Mode == "3":
            Hard_Mode()
        elif Mode == "4":
            Extreme_Mode()
        elif Mode == "5":
            print("Gặp lại bạn sau :)")
        else:
            print("Vui lòng nhập giá trị phù hợp (1, 2, 3, 4 hay 5 ")

if __name__ == "__main__":
    Choose_Mode()
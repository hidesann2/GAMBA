import random
import os
import sys
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def The_Dice_Game():
    Default_Balance = 20000
    New_Balance = Default_Balance
    Dice = [1, 2, 3, 4, 5, 6]
    Roll_Dice_User = 0
    Roll_Dice_Bot = 0

    print(f"Thách đấu bot trong trò chơi tung xúc xắc ? (Y/N)")
    while True:
        Entry = input()
        if Entry.lower() == "y":
            print("Bạn muốn cược bao nhiêu điểm?")
            while True:
                try:
                    Bet = int(input())
                    if 1000 <= Bet <= New_Balance and Bet % 1000 == 0:
                        Roll_Dice_User = random.choice(Dice)
                        Roll_Dice_Bot = random.choice(Dice)
                        break
                    else:
                        print(
                            f"Số điểm cược không hợp lệ. Vui lòng nhập lại(tối đa {New_Balance} điểm, tối thiểu 1000 điểm, bước nhảy: 1000).")
                except ValueError:
                    print("Nhập số điểm cược hợp lệ!!!")

                while Roll_Dice_User == Roll_Dice_Bot:
                    Roll_Dice_Bot = random.choice(Dice)

            print(f"Giá trị xúc xắc của bạn là", Roll_Dice_User)
            print(f"Giá trị xúc xắc của bot là", Roll_Dice_Bot)

            if Roll_Dice_User > Roll_Dice_Bot:
                print(f"Bạn đã thắng UwU ")
                New_Balance += Bet
            elif Roll_Dice_User < Roll_Dice_Bot:
                print(f"Bạn đã thua TvT ")
                New_Balance -= Bet
            else:
                print("Hòa! Số điểm không đổi ")
                print(f"Bạn có muốn chơi tiếp không ? (Y/N)")
                continue

            print(f"Số điểm bạn {'thắng' if Roll_Dice_User > Roll_Dice_Bot else 'thua'} ở lần này là ", Bet)
            print(f"Số điểm của bạn ở lần {'thắng' if Roll_Dice_User > Roll_Dice_Bot else 'thua'} này là ", New_Balance)
            print(f"Bạn có muốn chơi tiếp không ? (Y/N)")

            if New_Balance == 0:
                print(f"Bạn đã hết điểm. GAME OVER! ")
                break

        elif Entry.lower() == "n":
            clear_console()
            main()

        else:
            print(f"Vui lòng nhập đúng format! (Y/N)")

def The_Guessing_Number_Game():
    import random

    Default_Balance = 20000
    Small_Bet = 1000
    Small_Range = range(1, 10)
    Medium_Bet = 2000
    Medium_Range = range(1, 20)
    Large_Bet = 3000
    Large_Range = range(1, 30)
    AI_Bet = 5000
    AI_Range = range(1, 50)
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
                main()
            else:
                print("Vui lòng nhập giá trị phù hợp (1, 2, 3, 4 hay 5 ")

    if __name__ == "__main__":
        Choose_Mode()

def main():
    while True:
        print(f"DANH SACH GAME")
        print(f"1/ The Dice Game")
        print(f"2/ The Guessing Number Game")
        print(f"3/ Quit")

        choice = input("Nhập vào lựa chọn của bạn (1, 2 hay 3): ")
        if choice == "1":
            The_Dice_Game()
        elif choice == "2":
            The_Guessing_Number_Game()
        elif choice == "3":
            print("Gặp lại bạn sau :)")
            sys.exit()
        else:
            print(f"Vui lòng nhập giá trị hợp lệ (1, 2 hay 3)")

if __name__ == "__main__":
    main()
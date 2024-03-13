import random

Default_Balance = 20000
New_Balance = Default_Balance
Dice = [1, 2, 3, 4, 5, 6]
Roll_Dice_User = 0
Roll_Dice_Bot = 0

print(f"Thách đấu bot trong trò chơi tung xúc xắc ? (Y/N)")
while True:
    Entry = input()
    print("Bạn muốn cược bao nhiêu điểm?")
    if Entry.lower() == "y":
        while True:
            try:
                Bet = int(input())
                if 1000 <= Bet <= New_Balance and Bet%1000==0:
                    Roll_Dice_User = random.choice(Dice)
                    Roll_Dice_Bot = random.choice(Dice)
                    break
                else:
                    print(f"Số điểm cược không hợp lệ. Vui lòng nhập lại(tối đa {New_Balance} điểm, tối thiểu 1000 điểm, bước nhảy: 1000).")
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

        print(f"Số điểm bạn {'thắng' if Roll_Dice_User>Roll_Dice_Bot else 'thua'} ở lần này là ", Bet)
        print(f"Số điểm của bạn ở lần {'thắng' if Roll_Dice_User>Roll_Dice_Bot else 'thua'} này là ", New_Balance)
        print(f"Bạn có muốn chơi tiếp không ? (Y/N)")

        if New_Balance ==0:
            print(f"Bạn đã hết điểm. GAME OVER! ")
            break

    elif Entry.lower()=="n":
        print(f"Gặp lại bạn sau :)")
        break

    else:
        print(f"Vui lòng nhập đúng format! (Y/N)")
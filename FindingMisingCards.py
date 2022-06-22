n = int(input())
#リストの作成で二変数それぞれでforを回す方法
all_cards = [(s,n) for s in ['S','H','C','D'] for n in range(1,14)]

cards_list = []
#入力した回数だけforを回す
for _ in range(n):
    suit,num = input().split()
    num = int(num)
    cards_list.append((suit,num))
for card in all_cards:
    if card not in cards_list:
        print(*card)

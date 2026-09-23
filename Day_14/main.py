from art import logo,vs
print(logo)
from game_data import data
import random
final_score=0
acc_b=random.choice(data)
game_continue=True
while game_continue:
    acc_a=acc_b
    acc_b=random.choice(data)
    if acc_a==acc_b:
        acc_b=random.choice(data)

    def format_data(account):
        acc_name=account['name']
        acc_description=account['description']
        acc_country=account['country']
        return f"{acc_name} ,{acc_description} , {acc_country}"

    print(f"compare A: {format_data(acc_a)}")
    print(vs)
    print(f"Against B: {format_data(acc_b)}")
    answer=input("Who has more followers? Type 'A' or 'B': ")
    print("\n"*20)

    if answer=='A':
        if acc_a['follower_count']>acc_b['follower_count']:
            final_score+=1
            print(f"You are wright , Final score:{final_score}")

        else:
            game_continue=False
            print(f"You are wrong , Final score:{final_score}")
    else:
        if acc_b['follower_count']>acc_a['follower_count']:
            final_score+=1
            print(f"You are wright , Final score:{final_score}")
        else:
            game_continue=False
            print(f"You are wrong , Final score:{final_score}")



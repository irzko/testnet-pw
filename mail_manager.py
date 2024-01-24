# import asyncio
import asyncio
import os
import generate_user
from mailtm import MailTM
import sqlite3
import pandas as pd

async def main():
    os.system("clear")
    con = sqlite3.connect("mailtm.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM accounts")
    accounts = cur.fetchall()
    df = pd.DataFrame(accounts, columns=["id", "address", "password"])

    print(df) 
    # for account in accounts:
    #     print(account[1])
    mailtm = MailTM()

    while True:
        address = input("Chọn Email: ")
        if (address == "Q" or address == "q"):
            break
        else:
            token_res = await mailtm.get_account_token(address=accounts[int(address)][1], password=accounts[int(address)][2])
            messages = await mailtm.get_messages(token_res.token)
            if (len(messages.hydra_member) == 0):
                print("Không có thư mới")
            else:
                print(messages.hydra_member[0].subject)
    con.close()


if __name__ == "__main__":
    asyncio.run(main())
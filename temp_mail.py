import generate_user

from mailtm import MailTM
import sqlite3

mailtm = MailTM()

async def create_account():
    domains = await mailtm.get_domains()
    domain = domains.hydra_member[0].domain
    # Create account
    address = generate_user.random_username() + "@" + domain
    password = generate_user.random_password()
    account = await mailtm.get_account(address, password)
    return {"id": account.id, "address": address, "password": password}

def save_account(id, address, password):
    con = sqlite3.connect("mailtm.db")
    cur = con.cursor()
    cur.execute("INSERT INTO accounts VALUES (?, ?, ?)", (id, address, password))
    con.commit()
    con.close()

async def get_token(address, password):
    token = await mailtm.get_account_token(address, password)
    return token

async def get_messages(token):
    messages = await mailtm.get_messages(token)
    return messages



        


        





def main () -> None:







    # save_to_csv([[account.id, address, password]])

    # print(token)

    # messages = await mailtm.get_messages(token, page)
    # accounts = read_from_csv()
    # print(accounts)

    con = sqlite3.connect("mailtm.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM accounts")
    # cur.execute("DELETE FROM accounts WHERE id = '65af62b9546b3dfcf80da075'")
    # con.commit()
    accounts = cur.fetchall()
    print(accounts)
    # print(accounts[0][1])
    # token = account_token.token
    # print(messages)

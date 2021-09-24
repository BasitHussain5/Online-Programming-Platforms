try:
    withdraw,account_balance = map(float, input().split())
    if withdraw <= account_balance-0.5 and withdraw % 5==0:
        print("%.2f"%(account_balance-withdraw-0.50))
    else:
        print("%.2f"%account_balance)
    
except:
    pass
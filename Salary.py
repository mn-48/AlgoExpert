
salary_sheet_Nazmul = [
    ("January", 49111),
    ("Febryary", 68000),
    ("March", 68000), #b1
    ("April", 60444),
    ("May", 68000), # b2
    ("June", 60444),
    ("July", 34000), # Start
    ("August", 68000),
    ("September", 68000),
    ("October", 68000),
    ("November", 64222),
    ("December", 68000),
    ("Bonus1", 23800),
    ("Bonus2", 23800),
]

total = 0
for shn in range(len(salary_sheet_Nazmul)):
    total += salary_sheet_Nazmul[shn][1]
# print("Without Bonus Salary Only: ",   744221)
print("Total: ", total)

sal_val = 62018

gatice = 25117
basic = int(sal_val*0.35*12)+8 + gatice
print(f"Basic: {basic} and Adjust: {total-basic}")

house_rent = int(sal_val*0.25*12)
print(f"House Rent: {house_rent} and Adjust: {total-basic-house_rent}")

medical_allowance = int(sal_val*0.15*12)
print(f"Medical Allowance: {medical_allowance} and Adjust: {total-basic-house_rent-medical_allowance}")

conveyance_allowance = int(sal_val*0.10*12)-gatice
print(f"Conveyance Allowance: {conveyance_allowance} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance}")

food_allowance = int(sal_val*0.10*12)
print(f"Food Allowance: {food_allowance} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance-food_allowance}")

mobile = int(sal_val*0.02*12)
print(f"mobile: {mobile} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance-food_allowance- mobile}")
internet = int(sal_val*0.02*12)
print(f"internet: {internet} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance-food_allowance-mobile- internet}")

newspaper_allowance = int(sal_val*0.01*12)
print(f"newspaper_allowance: {newspaper_allowance} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance-food_allowance -mobile- internet- newspaper_allowance}")

# eid_bonus_2 = int(sal_val*0.35*2)
eid_bonus_2 = int(23800*2)
print(f"Eid Bonus: {eid_bonus_2} and Adjust: {total-basic-house_rent-medical_allowance-conveyance_allowance-food_allowance- mobile- internet- newspaper_allowance-eid_bonus_2}")


print("************************************************************")
print(f"***************** Total earn: {total}***********************")
print("************************************************************")


print("_________________________ Total COST _______________________________")

cost_sheet = {
    "Bank Loan_payment": 230000,
    "house_rent": 8000*12, #96000
    "GasBill": 1080*12, # 12960
    "CurrentBill": 8000, #10000
    "Internet": 12*600, #7200
    "Food": 18000*12, # 216000
    "Cloth": 50000, 
    "Madicine": 60000,
    "Utility": 24000,
    "Bank": 80000,
    # "HandCash": 7661
}

total_cost = 0
for key, val in cost_sheet.items():
    total_cost += val
    print(key, val)

print(total_cost)
print("CashMy hand: ", total-total_cost)
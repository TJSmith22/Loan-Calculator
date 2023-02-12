"""
TJ Smith
CS230
Loan Calculator
"""
# Import functions needed
import numpy_financial as npf
import math

#Symbolic constant
SEPERATOR = 68

#Intro statement
print("Welcome to the CS230 Loan Calculator!\n")

# Sample or custom report validation
report_type = ""
correct = False
while not correct:
    report_type = input("[S]ample or [C]ustom Report: ").upper()
    if report_type not in ["S", "C"]:
        print("Error. Enter [S]ample or [C]ustom")
    else:
        correct = True

# sample amounts given in problem (used as string so they can change for the custom report)
loan_amt = 250000
int_rate = .0475
years = 20

# Custom report inputs
if report_type == "C":
    int_rate = float(input("Enter annual interest rate: "))
    loan_amt = float(input("Enter loan amount: "))
    years = 0
    while years < 3 or years >30:
        years = int(input("Enter the number of years (between 3 and 30): "))
        if years < 3 or years >30:
            print("Error. Enter number of years (between 3 and 30)")

# Monthly or Annual validation
calculation_type = ""
correct = False
while not correct:
    calculation_type = input("[M]onthly or [A]nnual Report: ").upper()
    if calculation_type not in ["M", "A"]:
        print("Error. Enter [M] or [A]")
    else:
        correct = True

# Output to print inputted information (loan amount, duration, int rate) as well as monthly payment
monthly_pmt = npf.pmt(int_rate/12, years*12, -1* loan_amt,fv=0,when='end')
print("=" * SEPERATOR)
print(f"{'Loan Amount:':<24} ${loan_amt:>12,.2f}")
print(f"{'Loan duration in months:':<24} {years * 12:>12}")
print(f"{'Annual Interest Rate:':<24} {int_rate*100:>12.2f}%")
print(f"{'Monthly Payment:':<24} ${monthly_pmt:>12,.2f}")
print("=" * SEPERATOR)

# calculating the correct values for loan information
int_total, prin_total, pmt_total, halfway, year = 0, 0, 0, 0, 0
halfway_unit = "Month"
for month in range (1, years * 12 + 1):
    if(month - 1) % 12 == 0:
        year +=1
    int_part = npf.ipmt(int_rate/12, month, years*12,-1*loan_amt)
    int_total += int_part
    prin_part = npf.ppmt(int_rate/12, month, years*12,-1*loan_amt)
    prin_total += prin_part
    pmt_total += monthly_pmt

#Output for monthly statement
    if prin_total > loan_amt / 2 and halfway ==0:
        halfway = month
    if calculation_type == "M":
        if (month-1) % 12==0 or month == 1:
            label = "Year: " + str(year)
            print(label.center(SEPERATOR, "-"))
            print(f"{'Month':<6}\t{'Principal':<12}\t{'Interest':<12}\t{'Payment':<12}")
        print(f"{month:>6}\t${prin_part:>12,.2f}\t${int_part:>12,.2f}\t${monthly_pmt:>12,.2f}")
        if month == years * 12:
            print("=" * SEPERATOR)
            print(f"{'Total':>6}\t${prin_total:>12,.2f}\t${int_total:>12,.2f}\t${pmt_total:>12,.2f}")
#Output for annual statement
    if calculation_type == "A":
        if month == 1:
            print(f"{'Year':<6}\t{'Principal':<12}\t{'Interest':<12}\t{'Payment':<12}\t{'% Paid':<8}")
        if month % 12 == 0:
            print(f"{year:<6}\t${prin_total:>12,.2f}\t${int_total:>12,.2f}\t${pmt_total:>12,.2f}{prin_total/loan_amt * 100:>8,.2f}%")
            if year % 8 == 0:
                print("")
        if month == years*12:
            print('=' * SEPERATOR)
            print(f"{'Total':<6}\t${prin_total:>12,.2f}\t${int_total:>12,.2f}\t${pmt_total:>12,.2f}{prin_total/loan_amt * 100:>8,.2f}%")
            halfway = math.ceil(halfway/12)
            halfway_unit = "Year"
# Halfway paid statement
print(f"\nLoan principal is half paid off as of {halfway_unit} {halfway}")










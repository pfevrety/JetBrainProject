import sys
import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', required=True, help="loan type")
parser.add_argument('--principal', required=False, help="loan principal")
parser.add_argument('--periods', required=False, help="loan periods")
parser.add_argument('--interest', required=False, help="loan interest")
parser.add_argument('--payment', required=False, help="month payment")

args = parser.parse_args()

if len(sys.argv) == 5:
    genre = args.type
    if genre == 'diff' and args.interest is not None:
        if args.payment != None:
            print("Incorrect parameters.")
        else:
            overpayment = 0
            for j in range(1, int(args.periods) + 1):
                d = int(args.principal) / int(args.periods) + (float(args.interest) / (12 * 100)) * (int(args.principal) - (int(args.principal) * (j - 1) / int(args.periods)))
                print(f"Month {j}: payment is {math.ceil(d)}")
                overpayment += math.ceil(d) - (int(args.principal) / int(args.periods))
            print()
            print(f"Overpayment = {round(overpayment)}")
    elif genre == "annuity" and args.periods is not None and args.principal is not None:
        mensualite = math.ceil((int(args.principal) * (float(args.interest) / (12 * 100)) * (1 + (float(args.interest) / (12 * 100)) ) ** int(args.periods)) / ((1 + (float(args.interest) / (12 * 100))) ** int(args.periods) - 1))
        print(f"Your annuity payment = {mensualite}!")
        overpayment = mensualite * int(args.periods) - int(args.principal)
        print(f"Overpayment = {round(overpayment)}")
    elif genre == "annuity" and args.periods is not None and args.principal is None:
        loan_principal = int(args.payment) / (((float(args.interest) / 12 / 100) * (1 + (float(args.interest) / 12 / 100)) ** int(args.periods)) / (((float(args.interest) / 12 / 100) + 1) ** int(args.periods) - 1))
        print(f"Your loan principal = {math.floor(loan_principal)}!")
        overpayment = int(args.payment) * int(args.periods) - loan_principal
        print(f"Overpayment = {math.ceil(overpayment)}")
    elif genre == "annuity" and args.periods is None:
        nb_months = math.ceil(math.log(int(args.payment) / (int(args.payment) - (float(args.interest) / 12 / 100) * int(args.principal)), 1 + (float(args.interest) / 12 / 100)))
        years = nb_months // 12
        months = nb_months % 12

        if months > 1 and years > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif months == 0 and years > 1:
            print(f"It will take {years} years to repay this loan!")
        elif months == 1 and years > 1:
            print(f"It will take {years} years and {months} month to repay this loan!")

        if months > 1 and years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 1 and years == 0:
            print(f"It will take {months} month to repay this loan!")

        if months > 1 and years == 1:
            print(f"It will take {years} year and {months} months to repay this loan!")
        elif months == 1 and years == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        elif months == 0 and years == 1:
            print(f"It will take {years} year to repay this loan!")
        overpayment = nb_months * int(args.payment) - int(args.principal)
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters.")
else:
        print("Incorrect parameters.")

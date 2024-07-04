from datetime import date

def main():
    day = int(input("Enter day of your date: ")) 
    month = int(input("Enter month of your date:"))
    year = int(input("Enter year of your date:"))
    inp_date = date(year,month,day)

    print(age_difference(inp_date), "years")

    
def age_difference(inp_date):
    today_date = date.today()
    difference = today_date.year- inp_date.year - ((today_date.month, today_date.day) <     
    (inp_date.month,inp_date.day))
    return difference

main()



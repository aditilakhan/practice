print("currency conversion for below countries:")
print("country name and codes:\nINDIA-INR\nUSA-USD\nEurope-EUR")

try:
    fromcountry = input("Enter fromcurrency code:")
    tocountry = input("Enter tocurrency code:")
    amount = float(input("enter amount for conversion:"))
    if fromcountry == "INR" and tocountry.upper()=="INR":
        rates=1
    elif fromcountry.upper()=="INR" and tocountry.upper()=="USD":
        rates=0.011
    elif fromcountry.upper() == "INR" and tocountry.upper()=="EUR":
        rates=0.011
    elif fromcountry.upper() == "USD" and tocountry.upper()=="USD":
        rates=1
    elif fromcountry.upper() == "USD" and tocountry.upper()=="INR":
        rates=86.96
    elif fromcountry.upper() == "USD" and tocountry.upper()=="EUR":
        rates=0.97
    elif fromcountry.upper() == "EUR" and tocountry.upper()=="EUR":
        rates=1
    elif fromcountry.upper() == "EUR" and tocountry.upper()=="USD":
        rates=1.03
    elif fromcountry.upper() == "EUR" and tocountry.upper()=="INR":
        rates=89.74
    else:
        print("invalid country code")
        
    totalprice = rates*amount
    print(f"{amount} {fromcountry} is {totalprice} {tocountry}")
except:
    print("invalid input")
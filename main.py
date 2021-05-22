def main():
    Digits=analyze_number()
    sum=Luhn_analyzer(Digits)
    compute_validity(sum)
    if compute_validity(sum):
        print("The credit card number is valid!")
    else:
        print("This is not a valid credit card number!")

def analyze_number():
    Number = (input("Enter a potential credit card number (no spaces): "))
    Digits = list(Number)
    if Number[0]=='4' and len(Number)==16:
        print ("This could be a VISA")
    elif Number[0]=='5' and len(Number)==16:
        print ("This could be a Mastercard")
    elif Number[0]=='6' and len(Number)==16:
        print ("This could be a Discover card")
    elif Number[0]=='3' and Number[1]=='7' and len(Number)==15:
        print("This could be an American Express card")
    elif Number[0]=='3' and (Number[1]== ('8' or '0' or '6')) and len(Number)==14:
        print("This could be a Diners Club or Carte Blanche card")
    else:
        print("This is not a valid credit card number")
    return Digits

def Luhn_analyzer(Digits):
    length=len(Digits)
    Digits = [int(i) for i in Digits]
    for i in range(len(Digits))[-2::-2]:
        digit_product = Digits[i]*2
        if digit_product > 9:
            digit_product_list = [int(x) for x in str(digit_product)]
            digit_product=digit_product_list[0] + digit_product_list[1]
        Digits[i]=digit_product
    digit_sum=0
    for i in range(len(Digits)):
        digit_sum=digit_sum+Digits[i]
    return digit_sum

def compute_validity(sum):
    if sum % 10 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
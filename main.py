import random

def main():
    while True:
        print ("Welcome to Rhain's credit card number validation tool!")
        selection=input("To validate a credit card number, enter 1. To generate a valid Mastercard number, enter 2. To exit, hit Enter ")
        if selection == "1":
            Digits=analyze_number()
            Luhn_analyzer(Digits)
        elif selection == "2":
            generate_mastercard()
        elif selection == "":
            print ("Exiting. Thank you!")
            break
        else:
            print ("Enter only 1 or 2. Hit Enter to exit.")

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def generate_mastercard():
    digit_sum = 11111111111
    while (digit_sum % 10) != 0:
        generated_numbers = random.randint((10 ** (13)), ((10 ** 14) - 1))
        potential_number = "55" + str(generated_numbers)
        length = len(potential_number)
        potential_number_test = [int(i) for i in potential_number]
        for i in range(len(potential_number_test))[-2::-2]:
            digit_product = potential_number_test[i] * 2
            if digit_product > 9:
                digit_product_list = [int(x) for x in str(digit_product)]
                digit_product = digit_product_list[0] + digit_product_list[1]
            potential_number_test[i] = digit_product
        digit_sum = 0
        for i in range(len(potential_number_test)):
            digit_sum = digit_sum + potential_number_test[i]
    print ("This is a valid Mastercard number:", potential_number)
    print ("")

def analyze_number():
    Number = (input("Enter a potential credit card number (no spaces): "))
    Digits = list(Number)
    card_type=""
    if Number[0]=='4' and len(Number)==16:
    #    print ("This could be a VISA")
        card_type="VISA"
    elif Number[0]=='5' and len(Number)==16:
    #    print ("This could be a Mastercard")
        card_type = "Mastercard"
    elif Number[0]=='6' and len(Number)==16:
    #    print ("This could be a Discover card")
        card_type = "Discover"
    elif Number[0]=='3' and Number[1]=='7' and len(Number)==15:
    #    print("This could be an American Express card")
        card_type = "American Express"
    elif Number[0]=='3' and (Number[1]== ('8' or '0' or '6')) and len(Number)==14:
    #    print("This could be a Diners Club or Carte Blanche card")
        card_type = "Diner's Club or Carte Blanche"

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
    if digit_sum % 10 == 0:
        print("The credit card number is valid!")
        print ("")
    else:
        print("This is not a valid credit card number!")
        print ("")


if __name__ == '__main__':
    main()

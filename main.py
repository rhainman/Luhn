import random

def main():
    while True:
        print ("Welcome to Rhain's credit card number validation tool!")
        selection=input("To validate a credit card number, enter 1. To generate a valid credit card number, enter 2. To exit, hit Enter ")
        print("")
        if selection == "1":
            Digits=analyze_number()
            Luhn_analyzer(Digits)
        elif selection == "2":
            type = input("To generate a Mastercard number, enter 1. To generate a VISA number, enter 2. To generate an AMEX number, enter 3. To exit, hit Enter ")
            print("")
            if type=="1":
                generate_mastercard()
            elif type=="2":
                generate_visa()
            elif type=="3":
                generate_amex()
            elif selection == "":
                print("Exiting. Thank you!")
                break
            else:
                print("Enter only 1, 2 or 3. Hit Enter to exit.")
        elif selection == "":
            print ("Exiting. Thank you!")
            break
        else:
            print ("Enter only 1 or 2. Hit Enter to exit.")

def generate_mastercard():
    digit_sum = 1
    while (digit_sum % 10) != 0:
        generated_numbers = random.randint((10 ** 13), (10 ** 14 - 1))
        potential_number = "55" + str(generated_numbers)
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
    print ("Here is a valid Mastercard number: ",potential_number[0:4], potential_number[4:8], potential_number[8:12], potential_number[12:16] )
    print ("")

def generate_visa():
    digit_sum = 1
    while (digit_sum % 10) != 0:
        generated_numbers = random.randint((10 ** 14), (10 ** 15 - 1))
        potential_number = "4" + str(generated_numbers)
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
    print ("Here is a valid VISA number: ",potential_number[0:4], potential_number[4:8], potential_number[8:12], potential_number[12:16] )
    print ("")

def generate_amex():
    digit_sum = 1
    while (digit_sum % 10) != 0:
        generated_numbers = random.randint((10 ** 12), (10 ** 13 - 1))
        potential_number = "37" + str(generated_numbers)
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
    print ("Here is a valid AMEX number: ",potential_number[0:4], potential_number[4:10], potential_number[10:15])
    print ("")

def analyze_number():
    Number = (input("Enter a potential credit card number (no spaces): "))
    Digits = list(Number)
    # Following code is not being used for now, but it allows determination of potential card type
    # card_type=""
    # if Number[0]=='4' and len(Number)==16:
    #     print ("This could be a VISA")
    #     card_type="VISA"
    # elif Number[0]=='5' and len(Number)==16:
    #     print ("This could be a Mastercard")
    #     card_type = "Mastercard"
    # elif Number[0]=='6' and len(Number)==16:
    #     print ("This could be a Discover card")
    #     card_type = "Discover"
    # elif Number[0]=='3' and Number[1]=='7' and len(Number)==15:
    #     print("This could be an American Express card")
    #     card_type = "American Express"
    # elif Number[0]=='3' and (Number[1]== ('8' or '0' or '6')) and len(Number)==14:
    #     print("This could be a Diners Club or Carte Blanche card")
    #     card_type = "Diner's Club or Carte Blanche"
    return Digits

def Luhn_analyzer(Digits):
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

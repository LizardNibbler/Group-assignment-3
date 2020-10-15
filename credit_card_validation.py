# just copy and paste valid card number 4002997440555586,
def credit_veficiaction(number):
    card_number = number
    check_digit = card_number.pop()


    card_number.reverse()

    processed_digits = []
    digit=0
    check_diget=0

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2

        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9

        processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(digit))


    total = int(check_digit) + sum(processed_digits)

    if total % 10 == 0:
        return "Valid credit card number"
    else:
        return "Invalid credit card number"

#card_number = list(input("Please enter a card number without whitespace: ").strip())
#check =credit_veficiaction(card_number)
#print(check)

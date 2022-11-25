import re

def convert(number):
    # Convert to string to remove spaces
    number = str(number)
    number = number.replace(" ", "")

    # remove non-numeric chars
    number = re.sub(r'[^0-9]', '', number)

    # Convert to int to perform number validations
    number = int(number)

    if number < 0:
        return {
            "status": "error",
            "data": "The number needs to be greater than zero."
        }

    unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    ]

    tens = {
        30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 
        70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    hundred  = {"num": 100, "name": "hundred"}
    thousand = {"num": 1000, "name": "thousand"}
    million  = {"num": thousand['num'] * 1000, "name": "million"}
    billion  = {"num": million['num']  * 1000, "name": "billion"}
    trillion = {"num": billion['num']  * 1000, "name": "trillion"}

    if number <= 20:
        text_result = unique_numbers[number]

    elif number > 20 and number < 30:
        text_result = 'twenty ' + convert(number % 10)['data']

    elif number >= 30 and number < hundred['num']:
        if number % 10 == 0:
            text_result = tens[number]
        else:
            text_result = tens[(number - number % 10)] + '-' + convert(number % 10)['data']

    elif number >= hundred['num'] and number < thousand['num']:
        if number % hundred['num'] == 0:
            text_result = unique_numbers[int(number / hundred['num'])] + f" {hundred['name']}"
        else:
            text_result = convert(int(number / hundred['num']))['data'] + f" {hundred['name']} and " + \
                convert(number % hundred['num'])['data']

    elif number >= thousand['num'] and number < million['num']:
        if number % thousand['num'] == 0:
            text_result = convert(int(number / thousand['num']))['data'] + f" {thousand['name']}"
        else:
            text_result = convert(int(number / thousand['num']))['data'] + f" {thousand['name']} " + \
                convert(number % thousand['num'])['data']
                
    elif number >= million['num'] and number < billion['num']:
        if number % million['num'] == 0:
            text_result = convert(int(number / million['num']))['data'] + f" {million['name']}"
        else:
            text_result = convert(int(number / million['num']))['data'] + f" {million['name']} " + \
                convert(number % million['num'])['data']
                
    elif number >= billion['num'] and number < trillion['num']:
        if number % billion['num'] == 0:
            text_result = convert(int(number / billion['num']))['data'] + f" {billion['name']}"
        else:
            text_result = convert(int(number / billion['num']))['data'] + f" {billion['name']} " + \
                convert(number % billion['num'])['data']
                
    elif number == trillion['num']:
        text_result = f"one {trillion['name']}"

    elif number > trillion['num']:
        return {
            "status": "error",
            "data": "The number is too high. This lib is limited to 1 trillion."
        }

    return {
        "status": "ok",
        "data": text_result
    }
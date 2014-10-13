def what_is_my_sign(day, month):
    Months = {
        '1': 21,
        '2': 20,
        '3': 21,
        '4': 21,
        '5': 22,
        '6': 22,
        '7': 23,
        '8': 23,
        '9': 24,
        '10': 23,
        '11': 23,
        '12': 22
    }

    Zodiac = {
        '1': ["Capricorn", "Aquarius"],
        '2': ["Aquarius", "Pisces"],
        '3': ["Pisces", "Aires"],
        '4': ["Aires", "Taurus"],
        '5': ["Taurus", "Gemini"],
        '6': ["Gemini", "Cancer"],
        '7': ["Cancer", "Leo"],
        '8': ["Leo", "Virgo"],
        '9': ["Virgo", "Libra"],
        '10': ["Libra", "Scorpio"],
        '11': ["Scorpio", "Sagittarius"],
        '12': ["Sagittarius", "Capricorn"]
    }
    if day
     >= Months[str(month)]:
        return Zodiac[str(month)][1]
    else:
        return Zodiac[str(month)][0]


def main():
    print(what_is_my_sign(5, 8))
    print(what_is_my_sign(29, 1))
    print(what_is_my_sign(30, 6))
    print(what_is_my_sign(31, 5))
    print(what_is_my_sign(2, 2))

if __name__ == '__main__':
    main()

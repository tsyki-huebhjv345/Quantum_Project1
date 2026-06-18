    while True:
        try:
            number = input("Wpisz tlumaczenie slowek w jezyku polskim: tynkarz, ratownik, pielegniarka, geograf, spawacz, stolarz, hydraulik: ")
            valid_answer = ['plasterer', 'Plasterer', 'lifeguard', 'Lifeguard', 'nurse', 'Nurse', 'geographer', 'Geographer', 'welder', 'Welder', 'carpenter', 'Carpenter', 'plumber', 'Plumber', ]
            if number not in valid_answer:
                raise ValueError("Tylko 1 lub 2")
            else:
                return number
        except ValueError as err:
            print(err)
typed = testinput()
print("Wpisano poprawnie: " + typed)
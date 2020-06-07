tal = 2

def test_function():
    try:
        # Division med 0 giver en fejlbesked
        resultat = 10 / tal
    except ZeroDivisionError:
        print("Division med 0!!")
    else:
        print(resultat)
        pass
    finally:
        print("Så er vi færdige")

test_function()



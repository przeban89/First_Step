
def choice_to_number(x):

    """if x == 'Usain':
        return 1
    elif x == 'Me':
        return 2
    else:
        return 3"""

    return {'Usain': 1, 'Me': 2, 'Qazi': 3}[x]
def number_to_choice(x):
    return {1: 'Usain', 2: 'Me', 3: 'Qazi'}[x]
    """if x == 1:
        return 'Usain'
    elif x == 2:
        return 'Me'
    else:
        return 'Qazi'"""



def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Qazi') == 3
    print("Good Job")

def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Qazi'
    print("Good Job")

"""def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()

    except AssertionError:

        import wrong

    else:
        import success
"""
# test your code by un-commenting the line(s) below
#test_all()
test_choice_to_number()
test_number_to_choice()
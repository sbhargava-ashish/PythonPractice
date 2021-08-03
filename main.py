# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    ashish: str = "ashish"
    print("Hi {}".format(name))
    print(f'Hi, this is {name} and another name {ashish}')


# Press the green button in the gutter to run the script.
def calculate(number1: int, number2: int) -> int:
    return number1 + number2


def list_practice():
    names = ['Ashish', 'Bhargava', "Ashu"]
    names.sort()
    print(names)


def dic_practice():
    dictionary = {'key': 'new', "key1": "value1"}
    value = dictionary.get("key")
    print(value)


def practice_loops():
    items = [1,2,3,4,5]
    for item in items:
        print(item)


def practice_while():
    x = 0
    while x < 5:
        print(f'In while loop value of of x is {x}')
        x = x+1
        if x == 3:
            break
    else:
        print(f'Value of x is now {x}')

def statement_practice():
    bank = "CBA"
    if bank == 'CBAD':
        print('bank is CBAD')
    elif bank == 'CBA':
        print('bank is CBA')
    else:
        print('Neither')


if __name__ == '__main__':
    print_hi("PyCharm")
    list_practice()
    dic_practice()
    statement_practice()
    practice_loops()
    practice_while()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

print('Number of arguments:', len(sys.argv))
print('Argument list:', str(sys.argv))


def area(width, height):
    """
    Calculate the area
    """
    return width * height


def print_welcome(name):
    print('Welcome', name)


print_welcome('Robort')
w = 1920
h = 1080
a = area(w, h)
print(f'{w} x {h} = {a}')


def ask_ok(prompt, retries=4, reminder='Please try again !'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end='')
    print("if you put", voltage, "voltage through it .")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1000000, action='VOOOOOM')
# parrot(action='VOOOOOM', voltage=1000000)
# parrot('a million', 'bereft of life', 'jump')
# parrot('a thousand', state='pushing up the daisies')


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    # / 左边的参数使用时按位置传递参数
    # * 右边的参数按关键字传递参数
    # /和* 中间的参数按位置或者关键字传递参数
    print(pos_only, standard, kwd_only)


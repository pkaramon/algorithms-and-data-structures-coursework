# zad6testy.py

from testy import *
from zad6test_spec import ALLOWED_TIME, gentest


def copyarg(arg):
    return deepcopy(arg)


def printarg(*arg):
    print(f'n: {len(arg[0])}')
    print(f'M: {limit(arg[0])}')


def printhint(hint):
    print("Poprawny wynik  : ", limit(hint))


def printsol(sol):
    print("Otrzymany wynik : ", limit(sol))


def check(hint, sol):
    return hint == sol


def generate_tests(num_tests=None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests(f, all_tests=True):
    internal_runtests(copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME)

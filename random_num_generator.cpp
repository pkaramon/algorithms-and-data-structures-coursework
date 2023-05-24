#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

string lowcase = "abcdefghijklmnopqrstuvwxyz";
string upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string digits = "0123456789";
string spec = " ~!@#$%^&*()-=+[{]}\\;:'\"/?.>,<";
string all = lowcase + upcase + digits + spec;

string vowels = "aeiouyAEIOUY";
string consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ";

bool is_vowel(char c)
{
    for (auto v : vowels) {
        if (c == v) return true;
    }
    return false;
}

bool is_consonant(char c)
{
    for (auto v : consonants) {
        if (c == v) return true;
    }
    return false;
}

int main()
{
    srand(time(0));
    int n;
    cout << "Podaj dlugosc hasla (wieksza niz 2)" << endl;
    cin >> n;
    char *haslo = new char[n];
    haslo[0] = spec[rand() % spec.length()];
    haslo[1] = digits[rand() % digits.length()];
    haslo[2] = upcase[rand() % upcase.length()];

    for (int i = 3; i < n; i++) {
        haslo[i] = all[rand() % all.length()];
    }

    for (int i = 0; i < n - 1; i++) {
        int j = (rand() % (n - i)) + i;
        char temp = haslo[i];
        haslo[i] = haslo[j];
        haslo[j] = temp;
    }

    for (int i = 0; i < n; i++) {
        cout << haslo[i];
    }
    cout << endl << endl;

    for (int i = 1; i < n; i++) {
        if (is_vowel(haslo[i - 1]) && is_vowel(haslo[i])) {
            haslo[i] = consonants[rand() % consonants.length()];
        }
        else if (is_consonant(haslo[i - 1]) && is_consonant(haslo[i])) {
            haslo[i] = vowels[rand() % vowels.length()];
        }
    }

    for (int i = 0; i < n; i++) {
        cout << haslo[i];
    }

    delete[] haslo;
    return 0;
}
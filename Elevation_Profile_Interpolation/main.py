from utils.dane import wczytaj_dane, wezly_czebyszewa, wezly_rownomierne
from utils.wykresy import rysuj_profil_trasy, rysuj_wykres
from interpolacje.lagrange import lagrange
from interpolacje.splajny import splajny

def main():
    dane2 = wczytaj_dane("2018_paths/Unsyncable_ride.csv")
    #rysuj_profil_trasy(dane2)

    dane = wczytaj_dane("2018_paths/GlebiaChallengera.csv")
    #rysuj_profil_trasy(dane)
    i=4
    while i<=32:
        wezly = wezly_rownomierne(dane2, i)
        interpolacja = splajny(wezly)
        rysuj_wykres(dane2, wezly, interpolacja, tytul="Interpolacja splajnami")
        i = i*2

if __name__ == "__main__":
    main()
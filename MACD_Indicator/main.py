import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(data, index, liczba_okresow):
    alfa = 2/(liczba_okresow+1)
    licznik = 0.0
    mianownik = 0.0
    counter = 0
    for i in range(index, index-(liczba_okresow+1), -1):
        licznik += data[i] * (1-alfa)**counter
        mianownik += (1-alfa)**counter
        counter+=1
    return licznik/mianownik


def calculate_macd(data, index):
    return calculate_ema(data, index, 12) - calculate_ema(data, index, 26)


def calculate_signal(data, index):
    return calculate_ema(data, index, 9)


def starting_value(data, stocks):
    return stocks*data.iloc[0,1]


def buy_and_keep_strategy(data, stocks):
    return stocks*data.iloc[len(data)-1,1] - stocks*data.iloc[0,1]


def simulate(data, stocks):
    starting_value = stocks*data.iloc[0,1]
    money = 0
    portfolio_value = []
    profit_trades = 0
    loss_trades = 0
    last_buy_price = data.iloc[0,1]
    last_buy_date = data.iloc[0,0]
    buy_points = []
    sell_points = []
    transactions = []

    for index, row in data.iterrows():
        if row['Action'] == 'Buy':
            if money>0:
                stocks = money//row['Ostatnio']
                money -= stocks*row['Ostatnio']
                last_buy_date = row['Data']
                last_buy_price = row['Ostatnio']
                buy_points.append((row['Data'], money + stocks*row['Ostatnio']))
        elif row['Action']  == 'Sell':
            if stocks>0:
                sell_price = row['Ostatnio']
                sell_date = row['Data']
                profit = round((sell_price - last_buy_price) * stocks,2)
                profit_pct = round(((sell_price - last_buy_price) / last_buy_price) * 100,2)

                # Zapisywanie transakcji
                transactions.append({
                    "Data zakupu": last_buy_date,
                    "Cena zakupu": last_buy_price,
                    "Data sprzedaży": sell_date,
                    "Cena sprzedaży": sell_price,
                    "Zysk": profit,
                    "Zysk %": profit_pct
                })

                if profit > 0:
                    profit_trades += 1
                else:
                    loss_trades += 1
                money += stocks*row['Ostatnio']
                stocks=0
                sell_points.append((row['Data'], money + stocks * row['Ostatnio']))
        portfolio_value.append(money+stocks*row['Ostatnio'])
    balance = money + stocks*data.iloc[len(data)-1, 1] - starting_value
    return balance, portfolio_value, profit_trades, loss_trades, buy_points, sell_points, transactions


# Wczytanie danych
#df = pd.read_csv("PKN.csv")[['Data', 'Ostatnio']]
df = pd.read_csv("zloto.csv")[['Data', 'Ostatnio']]



# Zamiana przecinków na kropki i konwersja kolumny 'Ostatnio' na float
def convert_to_float(value):
    value = float(value.replace('.', '').replace(',', '.'))  # Zmieniamy format liczby
    return value

# Przekształcenie kolumny "Ostatnio"
df['Ostatnio'] = df['Ostatnio'].apply(convert_to_float)

# Konwersja kolumny 'Data' na format datetime
df["Data"] = pd.to_datetime(df["Data"], format="%d.%m.%Y")

df = df.sort_values(by="Data").reset_index(drop=True)

# Tworzenie wykresu
plt.figure(figsize=(15, 6))
plt.plot(df["Data"], df["Ostatnio"], label="Cena zamknięcia")
plt.xlabel("Data")
plt.ylabel("Cena [PLN]")
plt.title("Zmiana ceny akcji w czasie")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

df["MACD"] = None
df["Signal"] = None
df["Action"] = "Hold"

for i in range(len(df)):
    if i<26:
        continue
    df.at[i, "MACD"] = calculate_macd(df["Ostatnio"], i)
    if i<35:
        continue
    df.at[i, "Signal"] = calculate_signal(df["MACD"], i)


for i in range(1, len(df)):
    if df.at[i-1, "Signal"] is not None:
        if df.at[i-1, "MACD"]<df.at[i-1, "Signal"] and df.at[i, "MACD"]>df.at[i, "Signal"]:
            df.at[i, "Action"] = "Buy"
        elif df.at[i-1, "MACD"]>df.at[i-1, "Signal"] and df.at[i, "MACD"]<df.at[i, "Signal"]:
            df.at[i, "Action"] = "Sell"


start_date = "2024-04-15"
end_date = "2024-06-20"


#df = df[(df["Data"] >= start_date) & (df["Data"] <= end_date)].reset_index(drop=True)

# Tworzenie wykresu
plt.figure(figsize=(15, 6))
buy_data = df[df["Action"] == "Buy"]
sell_data = df[df["Action"] == "Sell"]
plt.scatter(buy_data["Data"], buy_data["Ostatnio"], label="Kupno", marker='^', color='green', s=50, zorder=2)
plt.scatter(sell_data["Data"], sell_data["Ostatnio"], label="Sprzedaż", marker='v', color='red', s=50, zorder=2)
'''for date, price in zip(buy_data["Data"], buy_data["Ostatnio"]):
    plt.text(date, price + 0.25, f"{price:.2f}", fontsize=10, verticalalignment='bottom', color='green')
for date, price in zip(sell_data["Data"], sell_data["Ostatnio"]):
    plt.text(date, price - 0.25, f"{price:.2f}", fontsize=10, verticalalignment='top', color='red')'''
plt.plot(df["Data"], df["Ostatnio"], label="Cena zamknięcia", zorder=1)
plt.xlabel("Data")
plt.ylabel("Cena [PLN]")
plt.title("Przykład opóźnienia wskaźnika MACD przy gwałtowych wahaniach kursu złota")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()



# Tworzenie wykresu
plt.figure(figsize=(15, 6))
plt.plot(df["Data"], df["MACD"], label="MACD", zorder=1)
plt.plot(df["Data"], df["Signal"], label="Signal", zorder=1)
plt.scatter(df[df["Action"] == "Buy"]["Data"], df[df["Action"] == "Buy"]["MACD"], label="Kupno", marker='^', color='green', s=50, zorder=2)
plt.scatter(df[df["Action"] == "Sell"]["Data"], df[df["Action"] == "Sell"]["MACD"], label="Sprzedaż", marker='v', color='red', s=50, zorder=2)
plt.xlabel("Data")
plt.ylabel("Wartość")
plt.title("MACD i Signal")
plt.xticks(rotation=45)
plt.legend(['MACD', 'Signal'])
plt.grid()
plt.show()

print(df)


#Symulacja
simulation_balance, portfolio_values, profit_trades, loss_trades, buy_points, sell_points, transactions= simulate(df, 1000)

transactions_df = pd.DataFrame(transactions)
print(transactions_df)

transactions_df.to_csv("transactions_gold.csv", index=False)

plt.figure(figsize=(15, 6))
plt.plot(df["Data"], portfolio_values, label="Wartość portfela - sygnały MACD", color='blue', zorder=1)
plt.plot(df["Data"], df["Ostatnio"]*1000, label="Wartość portfela - strategia kup i trzymaj", color='purple',zorder=1, alpha=0.7)

if buy_points:
    buy_dates, buy_values = zip(*buy_points)
    plt.scatter(buy_dates, buy_values, color='green', marker='^', label='Kupno', zorder=2)
if sell_points:
    sell_dates, sell_values = zip(*sell_points)
    plt.scatter(sell_dates, sell_values, color='red', marker='v', label='Sprzedaż', zorder=2)

plt.xlabel("Data")
plt.ylabel("Wartość portfela [PLN]")
plt.title("Zmiana wartości portfela inwestycyjnego w czasie")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

balance_keep_strat = buy_and_keep_strategy(df,1000)

print(f"Zyskowne transakcje: {profit_trades}, Stratne transakcje: {loss_trades}")
print(f"Balans uzyskany metodą MACD: {simulation_balance}, balans przy strategii kup i trzymaj {balance_keep_strat}")
print(starting_value(df,1000))

#TODO tabela z danymi o transakcjach w symulacji

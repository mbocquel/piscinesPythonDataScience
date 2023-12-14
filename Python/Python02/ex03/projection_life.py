from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert(s):
    if isinstance(s, str):
        if (s[-1] == 'k'):
            return (float(s[:-1]) * 1000)
        elif (s[-1] == 'M'):
            return (float(s[:-1]) * 1000000)
        elif (s[-1] == 'B'):
            return (float(s[:-1]) * 1000000000)
        else:
            return (float(s[:-1]))
    else:
        return (s)


def kilo(x, pos):
    """
    Change the format to put it in Kilo
    """
    return '%1.0fk' % (x * 1e-3)


def main():
    """
    Program that open the population file and display two graph
    """
    try:
        df_life = load('life_expectancy_years.csv')
        df_income = load(
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        df_income = df_income.map(convert)
        df_income1900 = df_income.loc[:, '1900']
        df_life1900 = df_life.loc[:, '1900']
        formatter = FuncFormatter(kilo)
        fig, ax = plt.subplots()
        plt.xscale("log")
        ax.xaxis.set_major_formatter(formatter)
        plt.plot(df_income1900, df_life1900, 'o')
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.show()
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()

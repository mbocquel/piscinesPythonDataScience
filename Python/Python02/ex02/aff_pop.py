from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def millions(x, pos):
    """Change the format to put it in Million"""
    return '%1.1fM' % (x * 1e-6)


def convert(str: str):
    if (str[-1] == 'k'):
        return (float(str[:-1]) * 1000)
    elif (str[-1] == 'M'):
        return (float(str[:-1]) * 1000000)
    elif (str[-1] == 'B'):
        return (float(str[:-1]) * 1000000000)
    else:
        return (float(str[:-1]))


def main():
    """
    Program that open the population file and display two graph
    """
    try:
        df = load("population_total.csv")
        df = df.map(convert)
        df = df.loc[:, '1800':'2050']
        france = df.loc['France']
        belgium = df.loc['Belgium']
        years = df.columns
        formatter = FuncFormatter(millions)
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.plot(years, france, 'r', label="France")
        plt.plot(years, belgium, 'b', label="Belgium")
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title("Population Projection")
        plt.xticks(years[::50])
        plt.legend()
        plt.show()
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()

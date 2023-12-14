from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program that open the lifeexpectancy
    file and display france
    """
    try:
        df = load("life_expectancy_years.csv")
        france = df.loc['France']
        years = df.columns
        plt.plot(years, france, 'r', label="France")
        plt.xlabel("Years")
        plt.ylabel("Life Expectancy")
        plt.xticks(years[::50])
        plt.yticks(range(30, 101, 20))
        plt.title("Life Expectancy Over the Years")
        plt.legend()
        plt.show()
    except Exception as err:
        print("Error: ", err)


if __name__ == "__main__":
    main()

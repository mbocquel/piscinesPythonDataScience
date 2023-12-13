from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program that open the life 
    """
    try:
        dataFrame = load("life_expectancy_years.csv")
        print(dataFrame)
        # dataFrame.plot()

        franceDataSet = dataFrame.query('country == "France"')
        print(franceDataSet)
        franceDataSet.plot()
        plt.show() 
        # print(franceDataSet)
    except AssertionError:
        print("AssertionError: error with the file")


if __name__ == "__main__":
    main()

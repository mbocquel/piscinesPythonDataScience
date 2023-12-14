import pandas as pd


def load(path: str)-> pd.DataFrame | None:
    """
    Function that load data from a csv file and return the panda dataFrame
    Return None if there was a problem
    """
    try: 
        df = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", df.shape)
        return (df)
    except Exception as e:
        print(e)
        return None

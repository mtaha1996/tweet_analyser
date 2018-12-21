import pandas as pd
import os


class Preprocess:
    def __init__(self, path, header=None):

        try:
            print("Reading %s file" % path)
            self.df = pd.read_csv(path, header=header)
        except FileNotFoundError:
            print("File does not exist!")

    def add_column_header(self, header):

        # if there is no headers for your columns you can add a list of headers

        # header = ["Tweet_ID", "Tweet", "Screen_Name", "Description", "User_Location", "Time", "Geo_Enabled",
        # "Place", "Lat", "Long"]

        self.df.columns = header

    # print first n lines of the data
    def show_n_first(self, number_of_lines):
        print(self.df.head(number_of_lines))

    # this will return the data types of each column
    def check_data_type(self):
        return self.df.dtypes

    # return the statistical summary of data such as : count, mean, standard deviation, min, max and ...
    def describe(self, include=None):
        return self.df.describe(include=include)

    # show the top 30 rows and bottom 30 row of you data
    def info(self):
        return self.df.info()

    def get_columns(self, list_rows):
        print("row:",list_rows)
        return self.df.loc[:, list_rows]

    def set_index(self, col_label, drop=False):
        return self.df.set_index(col_label, drop)

    # save the data as csv
    def save_as_csv(self, path, file_name):
        des = os.path.join(path, file_name)
        self.df.to_csv(des)

    # save the data as json
    def save_as_json(self, path, file_name):
        des = os.path.join(path, file_name)
        self.df.to_json(des)

    def __str__(self):
        return str(self.df)

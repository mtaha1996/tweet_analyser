from pandas import DataFrame


class Activity:
    def __init__(self, data: DataFrame):
        self.data = data
        self.username = data.get("Screen_Name")[0]
        # print(self.username)

    # Get time with this format {username: [{'date': '2018-12-04', 'clock': '04:04:46'}, ...}]}
    def export_times(self):

        time = {self.username: []}

        for i in range(len(self.data.get("Time"))):
            dic_time = {}

            raw_time = self.data.get("Time")[i].split(" ")

            dic_time["date"] = raw_time[0]
            dic_time["clock"] = raw_time[1]

            time[self.username].append(dic_time)

        return time


# This is unusable for now...!
class Time:
    def __init__(self, time_date=None, time_clock=None):

        self.date = time_date
        self.clock = time_clock

    def get_date(self):
        dic_date = {"Year": None, "Month": None, "Day": None}

        date_temp = self.date.split("-")

        dic_date["Year"] = date_temp[0]
        dic_date["Month"] = date_temp[1]
        dic_date["Day"] = date_temp[2]

        return dic_date

    def get_clock(self):
        dic_clock = {"Hour": None, "Minute": None, "Second": None}

        clock_temp = self.clock.split(":")

        dic_clock["Hour"] = clock_temp[0]
        dic_clock["Minute"] = clock_temp[1]
        dic_clock["Second"] = clock_temp[2]

        return dic_clock

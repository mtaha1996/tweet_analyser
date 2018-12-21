# You should config this file and set you own thresholds!
from activity import Time
import datetime


class Threshold:
    def __init__(self, dic_user_time):
        # dic_user_time format => {username: [{'date': '2018-12-04', 'clock': '04:04:46'}, ...}]}
        self.pack = dic_user_time

    def apply_clock_threshold(self, start_time="00:00:00", stop_time="06:00:00"):
        self.start_time = start_time
        self.stop_time = stop_time
        tweets_in_threshold = 0

        start_time = Time(time_clock=start_time).get_clock()
        stop_time = Time(time_clock=stop_time).get_clock()

        start_time_in_sec = int(start_time["Hour"]) * 3600 + int(start_time["Minute"]) * 60 + int(start_time["Second"])
        stop_time_in_sec = int(stop_time["Hour"]) * 3600 + int(stop_time["Minute"]) * 60 + int(stop_time["Second"])

        for key in list(self.pack.keys()):
            for time in self.pack[key]:
                clock = Time(time_clock=time["clock"]).get_clock()

                clock_in_sec = int(clock["Hour"]) * 3600 + int(clock["Minute"]) * 60 + int(clock["Second"])

                if (clock_in_sec < stop_time_in_sec) and (clock_in_sec > start_time_in_sec):
                    tweets_in_threshold += 1
        return tweets_in_threshold

    def ckeck_day_tweets(self):

        all_days = []

        day_dic = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}

        for key in list(self.pack.keys()):
            for time in self.pack[key]:
                day_act = [0, 0, 0, 0, 0, 0, 0]

                date = time["date"]

                day = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')

                pos = day_dic[day]

                day_act[pos] = 1

                all_days.append(day_act)

        return all_days

    def apply_quantitative_thresholds(self):

        all_days = []

        for key in list(self.pack.keys()):
            for time in self.pack[key]:

                clock = Time(time_clock=time["clock"]).get_clock()

                clock_in_sec = int(clock["Hour"]) * 3600 + int(clock["Minute"]) * 60 + int(clock["Second"])

                if clock_in_sec >= 0:
                    if clock_in_sec < 6 * 3600:
                        all_days.append([1, 0, 0, 0])
                    elif clock_in_sec < 12 * 3600:
                        all_days.append([0, 1, 0, 0])
                    elif clock_in_sec < 17 * 3600:
                        all_days.append([0, 0, 1, 0])
                    elif clock_in_sec < 24 * 3600:
                        all_days.append([0, 0, 0, 1])
                    else:
                        return "err in claculating act!"

        return all_days

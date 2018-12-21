from preprocessing import Preprocess
from activity import Activity
from threshold import Threshold
import pandas as pd
import os


def calc_act(name_time_cols):
    act = Activity(name_time_cols)
    name = act.username
    dic_act = act.export_times()
    myThresh = Threshold(dic_act)
    act_hours = myThresh.apply_quantitative_thresholds()
    week = myThresh.ckeck_day_tweets()

    all_act = []

    for i in range(len(week)):
        all_act.append(week[i] + act_hours[i])
        all_act[i].append(name)

    return all_act
#
#
# # Read raw data from file
# raw_data_frame = Preprocess("raw_data/girlbosskaty_tweets.csv", header=0)
#
# # Select the Time and username column from raw data
#  data_time_uid = raw_data_frame.get_columns(["Screen_Name", "Time"])
#
# # print(data_time_uid)
#
# # Calculate Activity
# act = Activity(data_time_uid)
# dic_act = act.export_times()
#
# print(dic_act)
#
# myThresh = Threshold(dic_act)
#
# act = myThresh.apply_quantitative_thresholds()
#
# # print(act)
# # print(myThresh.apply_clock_threshold(start_time="01:00:00", stop_time="05:00:00"),
# #       "tweets between %s and %s" % (myThresh.start_time, myThresh.stop_time))
# # print(myThresh.ckeck_day_tweets())
#
# WeekDay_counter = myThresh.ckeck_day_tweets()
# night_tweet_counter = myThresh.apply_clock_threshold(start_time="01:00:00", stop_time="05:00:00")
#
# # print(WeekDay_counter)
#
#
# head = ['Username', 'Night_tweets'] + [ key for key in list(WeekDay_counter.keys())]
# row = [list(dic_act.keys())[0], night_tweet_counter] + [ value for value in list(WeekDay_counter.values())]
#
# res_df = pd.DataFrame([row], index=None, columns=head)
# res_df.to_csv(os.path.join("results", "result.csv"))
# # res_df.to_json(os.path.join("results", "result.json"))
#

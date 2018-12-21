import csv, os, sys
import pandas as pd
from liwc import word_category_counter as wc
from preprocessing import Preprocess
from activity import Activity
from threshold import Threshold
from calc_activity import calc_act


def read_file(f):
    inlines = pd.read_csv(f)
    print("num of lines = ", inlines.shape[0])
    return inlines['text'].values


def write_csv(filename, rows, header_fields=None):
    with open(filename, 'w', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        if header_fields:
            writer.writerow(header_fields)
        for row in rows:
            writer.writerow(row)


def get_liwc_scores(wc, tweets, name_time):
    categories = set()
    all_scores = []
    count = 0
    # print(len(rows))

    # This loop finds the categories
    for sent in tweets:
        count += 1
        liwc_scores = wc.score_text(sent)
        categories |= set(liwc_scores.keys())

    # print("counted",count)
    category_list = sorted(list(categories))

    count2 = 0
    for sent in tweets:
        liwc_scores = wc.score_text(sent)
        # print(liwc_scores)
        # all_scores += [[row[col_name]] + [liwc_scores.get(category, 0.0) for category in category_list]]
        all_scores += [[liwc_scores.get(category, 0.0) for category in category_list]]

        # print(all_scores)
        count2 += 1

    # This part is for adding new features to categories
    new_feat = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                '0_6', '6_12', '12_17', '17_24', 'Username']
    category_list += new_feat
    name_act = calc_act(name_time)
    # todo here !

    print('category_list:', category_list)
    print('name_act:', name_act)

    for i in range(len(all_scores)):
        all_scores[i] = all_scores[i] + name_act[i]

    print('all_scores', all_scores)

    # print(all_scores)
    return all_scores, category_list


def get_tweet_body(input_file):
    tweet_col = pd.read_csv(input_file)['Tweet']
    return tweet_col.values


def get_tweet_name_time(input_file):
    print(input_file)
    name_time = Preprocess(input_file, header=0).get_columns(["Screen_Name", "Time"])
    return name_time


def main(infname, outfname):
    ip_filename = infname
    # col_name = colname
    op_filename = outfname
    wc.load_dictionary(wc.default_dictionary_filename())
    # ip_rows = read_file(ip_filename)
    ip_tweet_body = get_tweet_body(input_all)
    tweet_name_time = get_tweet_name_time(input_all)

    ip_scores, category_list = get_liwc_scores(wc, ip_tweet_body, tweet_name_time)
    write_csv(op_filename, ip_scores, category_list)


input_file = '../raw_data/merged.csv'
input_all = '../raw_data/girlbosskaty_tweets.csv'
output_file = '../results/dataset_features_test.csv'
main(input_file, output_file)

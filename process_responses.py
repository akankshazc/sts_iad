import pandas as pd
from collections import defaultdict

# The Original Responses had very inconvinient column names and id tags that contained initials
# of the study participants.

# So we will pre process the file as follows.

# The original file isn't uploaded for participant privacy reasons.
df = pd.read_csv('Coded_responses.csv')

df = df.drop(columns=df.columns[-3])

new_column_names = ["id", "gender", "gender_coded", "batch", "batch_coded", "avg_internet_usage",
                    "avg_internet_usage_coded", "usage_type", "usage_type_coded", "iat_1", "iat_2",
                    "iat_3", "iat_4", "iat_5", "iat_6", "iat_7", "iat_8", "iat_9", "iat_10", "iat_11",
                    "iat_12", "iat_13", "iat_14", "iat_15", "iat_16", "iat_17", "iat_18", "iat_19",
                    "iat_20", "iat_score", "iat_score_range", "iat_range_coded", "salience_score",
                    "salience_round", "salience_domain", "excessive_use_score", "excessive_use_round",
                    "excessive_use_domain", "neglect_work_score", "neglect_work_round",
                    "neglect_work_domain", "anticipation_score", "anticipation_round", "anticipation_domain",
                    "lack_of_control_score", "lack_of_control_round", "lack_of_control_domain",
                    "neglect_social_life_score", "neglect_social_life_round", "neglect_social_life_domain",
                    "qol_1", "qol_2", "qol_3", "qol_3_rev", "qol_4", "qol_4_rev", "qol_5", "qol_6",
                    "qol_7", "qol_8", "qol_9", "qol_10", "qol_11", "qol_12", "qol_13", "qol_14",
                    "qol_15", "qol_16", "qol_17", "qol_18", "qol_19", "qol_20", "qol_21", "qol_22",
                    "qol_23", "qol_24", "qol_25", "qol_26", "qol_26_rev", "qol_score", "qol_score_range",
                    "qol_range_coded", "physical_score_raw", "physical_score", "physical_domain_round",
                    "physical_domain_range", "psychological_score_raw", "psychological_score",
                    "psychological_domain_round", "psychological_domain_range",
                    "social_score_raw", "social_score", "social_domain_round", "social_domain_range",
                    "environment_score_raw", "environment_score", "environment_domain_round",
                    "environment_domain_range", "avg_pre_covid_use", "avg_pre_covid_use_coded",
                    "avg_post_covid_use", "avg_post_covid_use_coded", "change_in_usage", "change_in_usage_coded"]

column_dict = defaultdict(lambda: "")

for i in range(104):
    column_dict[df.columns[i]] = new_column_names[i]

df.rename(columns=column_dict, inplace=True)

df['id'] = df['id'].str.split(
    '/', expand=True)[0] + '/' + df['id'].str.split('/', expand=True)[1]

# Already run
# df.to_csv('coded_responses.csv')

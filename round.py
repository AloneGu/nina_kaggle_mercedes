import pandas as pd
dir_name = 'result/'
file_name = 'cv_blend_3_round_res.csv'
res_file_name = 'cv_blend_3_round_res3.csv'

df = pd.read_csv(dir_name+file_name)
df['y'] = df['y'].round(5)
df.to_csv(dir_name+res_file_name, index=False)

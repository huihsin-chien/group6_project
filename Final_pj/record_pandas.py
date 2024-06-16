import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

with open('leaderboard.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

average_values = df.mean()
print("-----------------平均值-----------------")
print(average_values)
max_hour = df['hour'].max()
print("最高存活時數:", max_hour)


plt.figure(figsize=(10, 6))
sns.histplot(df['hour'], bins=10, kde=True)
plt.title('Distribution of Hours')
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.show()

df.to_csv('game_data.csv', index=False)

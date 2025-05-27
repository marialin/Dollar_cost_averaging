# Dollar_Cost_Averaging

This repository aims to determine the best dollar-cost averaging (DCA) investment frequency—daily, weekly, or monthly—when investing a fixed amount into QQQ within a year, in order to maximize total returns.

To explore this, we analyze the performance of investing a fixed amount (e.g., USD 10,000) into QQQ over the course of a year—for example, from January 2016 to December 2016—using different DCA frequencies: daily, weekly, and monthly.

The advantage of dollar-cost averaging is that when QQQ’s price is high, the same dollar amount buys fewer shares, and when the price is low, it buys more shares. This approach helps mitigate the risks of market timing.

But what if the starting year is not ideal? To address this concern, the study is repeated across different starting years to observe the impact on returns.

What if the buying price is the worst? In this study, we assume that the buying price is the worst possible—i.e., the highest price of the day.

Can you guess:
  1. Which dollar-cost averaging frequency performs best?
  2. Which starting year delivers the best average annual or total return? 😄😬🤫

Here is the final answer. Why don't I use annualized return? Because annualized return doesn't reflect the idea that *time in the market* is more important than *timing the market*.

If your answer differs slightly from mine, that's okay—as long as you're not downloading the data from Nasdaq.com or your final value date isn't 23 May 2025.

=== SUMMARY TABLE ===
 Start Year Frequency  Shares  Initial Value  Today's Value  Total Gain ($)  Avg Annual Gain (%)
       2016     daily   89.55          10000      45,835.51       35,835.51                38.16
       2016   monthly   88.90          10000      45,503.22       35,503.22                37.81
       2016    weekly   89.59          10000      45,857.82       35,857.82                38.18
       2017     daily   71.34          10000      36,516.99       26,516.99                31.61
       2017   monthly   71.44          10000      36,567.82       26,567.82                31.67
       2017    weekly   71.42          10000      36,554.60       26,554.60                31.65
       2018     daily   58.42          10000      29,900.48       19,900.48                26.93
       2018   monthly   58.80          10000      30,098.65       20,098.65                27.20
       2018    weekly   58.53          10000      29,955.54       19,955.54                27.01
       2019     daily   53.70          10000      27,486.68       17,486.68                27.37
       2019   monthly   53.87          10000      27,573.76       17,573.76                27.50
       2019    weekly   53.73          10000      27,499.14       17,499.14                27.38
       2020     daily   40.37          10000      20,661.10       10,661.10                19.78
       2020   monthly   40.45          10000      20,705.90       10,705.90                19.86
       2020    weekly   40.54          10000      20,750.81       10,750.81                19.94
       2021     daily   28.31          10000      14,489.69        4,489.69                10.23
       2021   monthly   28.34          10000      14,503.42        4,503.42                10.26
       2021    weekly   28.36          10000      14,517.27        4,517.27                10.29
       2022     daily   32.17          10000      16,466.10        6,466.10                19.08
       2022   monthly   31.89          10000      16,320.63        6,320.63                18.65
       2022    weekly   32.27          10000      16,515.19        6,515.19                19.22
       2023     daily   29.06          10000      14,874.24        4,874.24                20.39
       2023   monthly   29.19          10000      14,940.39        4,940.39                20.67
       2023    weekly   29.11          10000      14,901.37        4,901.37                20.51
       2024     daily   21.48          10000      10,993.29          993.29                 7.14
       2024   monthly   21.59          10000      11,052.28        1,052.28                 7.57
       2024    weekly   21.46          10000      10,986.31          986.31                 7.09

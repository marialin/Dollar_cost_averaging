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
| Start Year | Frequency | Shares | Initial Value | Today's Value | Total Gain ($) | Avg Annual Gain (%) |
|------------|-----------|--------|----------------|----------------|------------------|-----------------------|
| 2016       | daily     | 89.55  | 10,000         | 45,835.51      | 35,835.51        | 38.16                |
| 2016       | monthly   | 88.90  | 10,000         | 45,503.22      | 35,503.22        | 37.81                |
| 2016       | weekly    | 89.59  | 10,000         | 45,857.82      | 35,857.82        | 38.18                |
| 2017       | daily     | 71.34  | 10,000         | 36,516.99      | 26,516.99        | 31.61                |
| 2017       | monthly   | 71.44  | 10,000         | 36,567.82      | 26,567.82        | 31.67                |
| 2017       | weekly    | 71.42  | 10,000         | 36,554.60      | 26,554.60        | 31.65                |
| 2018       | daily     | 58.42  | 10,000         | 29,900.48      | 19,900.48        | 26.93                |
| 2018       | monthly   | 58.80  | 10,000         | 30,098.65      | 20,098.65        | 27.20                |
| 2018       | weekly    | 58.53  | 10,000         | 29,955.54      | 19,955.54        | 27.01                |
| 2019       | daily     | 53.70  | 10,000         | 27,486.68      | 17,486.68        | 27.37                |
| 2019       | monthly   | 53.87  | 10,000         | 27,573.76      | 17,573.76        | 27.50                |
| 2019       | weekly    | 53.73  | 10,000         | 27,499.14      | 17,499.14        | 27.38                |
| 2020       | daily     | 40.37  | 10,000         | 20,661.10      | 10,661.10        | 19.78                |
| 2020       | monthly   | 40.45  | 10,000         | 20,705.90      | 10,705.90        | 19.86                |
| 2020       | weekly    | 40.54  | 10,000         | 20,750.81      | 10,750.81        | 19.94                |
| 2021       | daily     | 28.31  | 10,000         | 14,489.69      | 4,489.69         | 10.23                |
| 2021       | monthly   | 28.34  | 10,000         | 14,503.42      | 4,503.42         | 10.26                |
| 2021       | weekly    | 28.36  | 10,000         | 14,517.27      | 4,517.27         | 10.29                |
| 2022       | daily     | 32.17  | 10,000         | 16,466.10      | 6,466.10         | 19.08                |
| 2022       | monthly   | 31.89  | 10,000         | 16,320.63      | 6,320.63         | 18.65                |
| 2022       | weekly    | 32.27  | 10,000         | 16,515.19      | 6,515.19         | 19.22                |
| 2023       | daily     | 29.06  | 10,000         | 14,874.24      | 4,874.24         | 20.39                |
| 2023       | monthly   | 29.19  | 10,000         | 14,940.39      | 4,940.39         | 20.67                |
| 2023       | weekly    | 29.11  | 10,000         | 14,901.37      | 4,901.37         | 20.51                |
| 2024       | daily     | 21.48  | 10,000         | 10,993.29      | 993.29           | 7.14                 |
| 2024       | monthly   | 21.59  | 10,000         | 11,052.28      | 1,052.28         | 7.57                 |
| 2024       | weekly    | 21.46  | 10,000         | 10,986.31      | 986.31           | 7.09                 |


---

Well, I was challenged with the following question:
**How if one invests into QQQ in year 2000, would one make money by end of year 2010?**

This is a good question as QQQ price was high in year 2000 and low in year 2010.
Below is the result when investing USD 2 million within 1 year into QQQ ETF. 

Note: The following results were generated by running the Python script DollarCostAveraging_QQQ_2000_2010.py using QQQ historical prices from the QQQ_2000_2025.csv file.

Users can obtain QQQ historical data as follows:

For data from May 26, 2015 to May 23, 2025, download from nasdaq.com.

For data from January 1, 2000 to May 22, 2015, download year by year from marketwatch.com.

Combine the datasets into a single .csv file with consistent column names for proper analysis.

### === FINAL SUMMARY TABLE ===

| Start Year | Frequency | Shares    | Initial Value | Today's Value | Total Gain (\$) |
| ---------- | --------- | --------- | ------------- | ------------- | --------------- |
| 2000       | daily     | 22,236.80 | 2,000,000     | 1,214,574.19  | -785,425.81     |
| 2000       | monthly   | 21,770.63 | 2,000,000     | 1,189,111.98  | -810,888.02     |
| 2000       | weekly    | 22,322.52 | 2,000,000     | 1,219,256.14  | -780,743.86     |
| 2001       | daily     | 46,469.00 | 2,000,000     | 2,538,136.59  | 538,136.59      |
| 2001       | monthly   | 46,529.93 | 2,000,000     | 2,541,464.74  | 541,464.74      |
| 2001       | weekly    | 46,931.52 | 2,000,000     | 2,563,399.68  | 563,399.68      |
| 2002       | daily     | 70,226.72 | 2,000,000     | 3,835,783.48  | 1,835,783.48    |
| 2002       | monthly   | 68,753.40 | 2,000,000     | 3,755,310.74  | 1,755,310.74    |
| 2002       | weekly    | 70,267.27 | 2,000,000     | 3,837,998.32  | 1,837,998.32    |
| 2003       | daily     | 66,311.98 | 2,000,000     | 3,621,960.20  | 1,621,960.20    |
| 2003       | monthly   | 67,699.01 | 2,000,000     | 3,697,719.89  | 1,697,719.89    |
| 2003       | weekly    | 66,288.05 | 2,000,000     | 3,620,653.33  | 1,620,653.33    |
| 2004       | daily     | 54,605.72 | 2,000,000     | 2,982,564.24  | 982,564.24      |
| 2004       | monthly   | 54,606.71 | 2,000,000     | 2,982,618.58  | 982,618.58      |
| 2004       | weekly    | 54,682.06 | 2,000,000     | 2,986,733.98  | 986,733.98      |
| 2005       | daily     | 51,915.94 | 2,000,000     | 2,835,648.41  | 835,648.41      |
| 2005       | monthly   | 51,913.99 | 2,000,000     | 2,835,542.33  | 835,542.33      |
| 2005       | weekly    | 51,912.37 | 2,000,000     | 2,835,453.46  | 835,453.46      |
| 2006       | daily     | 48,923.39 | 2,000,000     | 2,672,195.54  | 672,195.54      |
| 2006       | monthly   | 48,829.94 | 2,000,000     | 2,667,091.33  | 667,091.33      |
| 2006       | weekly    | 48,914.04 | 2,000,000     | 2,671,685.11  | 671,685.11      |
| 2007       | daily     | 41,753.19 | 2,000,000     | 2,280,559.50  | 280,559.50      |
| 2007       | monthly   | 42,026.08 | 2,000,000     | 2,295,464.63  | 295,464.63      |
| 2007       | weekly    | 41,764.58 | 2,000,000     | 2,281,181.23  | 281,181.23      |
| 2008       | daily     | 48,715.52 | 2,000,000     | 2,660,841.89  | 660,841.89      |
| 2008       | monthly   | 47,123.93 | 2,000,000     | 2,573,909.12  | 573,909.12      |
| 2008       | weekly    | 48,842.79 | 2,000,000     | 2,667,793.39  | 667,793.39      |
| 2009       | daily     | 55,146.44 | 2,000,000     | 3,012,098.57  | 1,012,098.57    |
| 2009       | monthly   | 56,347.93 | 2,000,000     | 3,077,723.83  | 1,077,723.83    |
| 2009       | weekly    | 55,330.91 | 2,000,000     | 3,022,174.22  | 1,022,174.22    |

---



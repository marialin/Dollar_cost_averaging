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

Note: The following results were generated by running the Python script DollarCostAveraging_QQQ_2000_2010.py using QQQ historical prices from the QQQ_2000_2025.csv file. Users can obtain QQQ historical data as follows:
1. For data from May 26, 2015 to May 23, 2025, download from nasdaq.com.
2. For data from January 1, 2000 to May 22, 2015, download year by year from marketwatch.com.
3. Combine the datasets into a single .csv file with consistent column names for proper analysis.

It can be observed from the table below that if USD 2 million was invested in the year 2000, the value on 31 December 2010 would have dropped to approximately USD 1.214574 million, resulting in a loss of USD 785,426. This is clearly not the outcome an investor would expect after holding the investment for 10 years.

It is also evident that the investment return does not significantly depend on the frequency of the dollar cost averaging (DCA), whether done daily, weekly, or monthly.



### === FINAL SUMMARY TABLE ===

| Start Year | Frequency | Shares    | Initial Value | Value on 31 Dec 2010 | Total Gain (\$) |
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

To address the issue of potential losses due to unfortunate entry timing—such as investing during a market peak—we can consider extending the DCA investment window to 2, 3, or even 4 years. A longer DCA window may provide a better smoothing effect, reducing the risk associated with short-term market volatility.

To evaluate this approach, we conducted a study comparing the total return of investing USD 2 million into QQQ using monthly DCA over different window periods: 12, 24, 36, and 48 months. For each window length, we analyzed various starting years (from 2000 to 2010 minus the window length) and calculated the investment value as of 31 December 2010. This analysis helps identify the optimal DCA window that balances market timing risk with the goal of fully investing the allocated capital.

A Python program titled DollarCostAveraging_2000_2010_Window_12m_to_48m.py has been added to this repository for this study.

The results are shown in the table below. We can observe that for investment windows of 36 months and 48 months, there are no negative returns, indicating that longer DCA periods may help mitigate the risk of poor market timing.

```markdown
| Start Year | Frequency      | Shares        | Initial Value | Value on 31 Dec 2010 | Total Gain     |
|------------|----------------|---------------|----------------|------------------------|----------------|
| 2000       | monthly (12m)  | 21770.633022  | 2,000,000      | 1,189,112              | -810,888       |
| 2001       | monthly (12m)  | 46529.929347  | 2,000,000      | 2,541,465              | 541,465        |
| 2002       | monthly (12m)  | 68753.400557  | 2,000,000      | 3,755,311              | 1,755,311      |
| 2003       | monthly (12m)  | 67699.009288  | 2,000,000      | 3,697,720              | 1,697,720      |
| 2004       | monthly (12m)  | 54606.711492  | 2,000,000      | 2,982,619              | 982,619        |
| 2005       | monthly (12m)  | 51913.993619  | 2,000,000      | 2,835,542              | 835,542        |
| 2006       | monthly (12m)  | 48829.940173  | 2,000,000      | 2,667,091              | 667,091        |
| 2007       | monthly (12m)  | 42026.082597  | 2,000,000      | 2,295,465              | 295,465        |
| 2008       | monthly (12m)  | 47123.931172  | 2,000,000      | 2,573,909              | 573,909        |
| 2009       | monthly (12m)  | 56347.928008  | 2,000,000      | 3,077,724              | 1,077,724      |
|------------|----------------|---------------|----------------|------------------------|----------------|
| 2000       | monthly (24m)  | 34150.281184  | 2,000,000      | 1,865,288              | -134,712       |
| 2001       | monthly (24m)  | 57641.664952  | 2,000,000      | 3,148,388              | 1,148,388      |
| 2002       | monthly (24m)  | 68226.204922  | 2,000,000      | 3,726,515              | 1,726,515      |
| 2003       | monthly (24m)  | 61152.860390  | 2,000,000      | 3,340,169              | 1,340,169      |
| 2004       | monthly (24m)  | 53260.352556  | 2,000,000      | 2,909,080              | 909,080        |
| 2005       | monthly (24m)  | 50371.966896  | 2,000,000      | 2,751,317              | 751,317        |
| 2006       | monthly (24m)  | 45428.011385  | 2,000,000      | 2,481,278              | 481,278        |
| 2007       | monthly (24m)  | 44575.006884  | 2,000,000      | 2,434,687              | 434,687        |
| 2008       | monthly (24m)  | 51735.929590  | 2,000,000      | 2,825,816              | 825,816        |
|------------|----------------|---------------|----------------|------------------------|----------------|
| 2000       | monthly (36m)  | 45684.654309  | 2,000,000      | 2,495,296              | 495,296        |
| 2001       | monthly (36m)  | 60994.113064  | 2,000,000      | 3,331,498              | 1,331,498      |
| 2002       | monthly (36m)  | 63686.373779  | 2,000,000      | 3,478,550              | 1,478,550      |
| 2003       | monthly (36m)  | 58073.238133  | 2,000,000      | 3,171,960              | 1,171,960      |
| 2004       | monthly (36m)  | 51783.548428  | 2,000,000      | 2,828,417              | 828,417        |
| 2005       | monthly (36m)  | 47590.005463  | 2,000,000      | 2,599,366              | 599,366        |
| 2006       | monthly (36m)  | 45993.317980  | 2,000,000      | 2,512,155              | 512,155        |
| 2007       | monthly (36m)  | 48499.313925  | 2,000,000      | 2,649,033              | 649,033        |
|------------|----------------|---------------|----------------|------------------------|----------------|
| 2000       | monthly (48m)  | 51188.243053  | 2,000,000      | 2,795,902              | 795,902        |
| 2001       | monthly (48m)  | 59397.262671  | 2,000,000      | 3,244,278              | 1,244,278      |
| 2002       | monthly (48m)  | 60743.278739  | 2,000,000      | 3,317,798              | 1,317,798      |
| 2003       | monthly (48m)  | 55762.413643  | 2,000,000      | 3,045,743              | 1,045,743      |
| 2004       | monthly (48m)  | 49344.181970  | 2,000,000      | 2,695,179              | 695,179        |
| 2005       | monthly (48m)  | 47473.486890  | 2,000,000      | 2,593,002              | 593,002        |
| 2006       | monthly (48m)  | 48581.970487  | 2,000,000      | 2,653,547              | 653,547        |
```





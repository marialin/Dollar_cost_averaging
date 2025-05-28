# Well, I was challenged with the following question:
#   How if one invests into QQQ in year 2000, would one make money by end of year 2010?
# 
#   This is a good question as QQQ price was high in year 2000 and low in year 2010.
#   This program aims to produce the result when investing USD 2 million within 1 year into QQQ ETF.
# 
# DollarCostAveraging_QQQ_2000_2010.py using QQQ historical prices from the QQQ_2000_2025.csv file.
# Users can obtain QQQ historical data as follows:
#     For data from May 26, 2015 to May 23, 2025, download from nasdaq.com.
#     For data from January 1, 2000 to May 22, 2015, download year by year from marketwatch.com.
#     Combine the datasets into a single .csv file with consistent column names for proper analysis.


import pandas as pd

if __name__ == '__main__':

    # Load CSV with mixed-format dates and dirty numeric columns
    file_path = "data/QQQ_1999_2025.csv"
    df = pd.read_csv(file_path, skiprows=1)

    # Parse dates with mixed formats
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=['Date'])

    # Strip commas/quotes and convert columns to numeric
    for col in ['Open', 'High', 'Low', 'Close/Last', 'Volume']:
        df[col] = df[col].astype(str).str.replace(',', '').str.replace('"', '')
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows with any remaining NaNs in essential columns
    df = df.dropna(subset=['High'])

    # Sort by date ascending
    df = df.sort_values('Date')
    df.reset_index(drop=True, inplace=True)

    print(df.head())
    print(df.tail())

    # Global investment settings
    X = 2_000_000  # Total investment
    months = 12
    frequencies = {'daily': 'D', 'weekly': 'W', 'monthly': 'MS'}

    # Get final price as of 31 Dec 2010
    final_date = pd.to_datetime('2010-12-31')
    final_price_row = df[df['Date'] <= final_date].iloc[-1]
    final_price = final_price_row['High']
    print(f"\nFinal Date: {final_price_row['Date'].date()} | Final Price (High): ${final_price:.2f}")

    def align_to_trading_days(dates, trading_days):
        trading_days = set(trading_days)
        aligned = []
        for date in dates:
            while date not in trading_days:
                date += pd.Timedelta(days=1)
                if date > df['Date'].iloc[-1]:  # safeguard
                    break
            if date in trading_days:
                aligned.append(date)
        return aligned

    all_results = {}

    for start_year in range(2000, 2010):  # 2000 to 2009 inclusive
        print(f"\n=== Starting Year: {start_year} ===")
        year_results = {}

        start_date = pd.to_datetime(f"{start_year}-01-01")
        end_date = pd.to_datetime(f"{start_year}-12-31")

        for freq_label, freq_code in frequencies.items():
            print(f"\n--- Frequency: {freq_label.upper()} ---")

            raw_dca_dates = pd.date_range(start=start_date, end=end_date, freq=freq_code)
            aligned_dates = align_to_trading_days(raw_dca_dates, df['Date'])

            dca_df = df[df['Date'].isin(aligned_dates)]

            if dca_df.empty:
                print("No valid investment dates after alignment. Skipping...\n")
                continue

            amount_per_period = X / len(dca_df)
            total_shares = 0

            for _, row in dca_df.iterrows():
                shares = amount_per_period / row['High']  # Worst case: buy at daily high
                total_shares += shares

            final_value = total_shares * final_price
            total_gain = final_value - X

            year_results[freq_label] = {
                'total_shares': total_shares,
                'initial_value': X,
                'final_value': final_value,
                'total_gain': total_gain
            }

            print(f"Shares: {total_shares:.4f} | Value on 31 Dec 2010: ${final_value:,.2f} | Total Gain: ${total_gain:,.2f}")

        all_results[start_year] = year_results

    # Final Summary
    print("\n=== FINAL SUMMARY TABLE ===")
    summary = []
    for year, freqs in all_results.items():
        for freq, res in freqs.items():
            summary.append({
                'Start Year': year,
                'Frequency': freq,
                'Shares': res['total_shares'],
                'Initial Value': res['initial_value'],
                "Value on 31 Dec 2010": res['final_value'],
                'Total Gain ($)': res['total_gain']
            })

    summary_df = pd.DataFrame(summary)
    summary_df = summary_df.sort_values(['Start Year', 'Frequency'])

    pd.set_option("display.float_format", "{:,.2f}".format)
    print(summary_df.to_string(index=False))

    summary_df.to_csv("data/DCA_2000_2009_Summary_by_2010.csv", index=False)

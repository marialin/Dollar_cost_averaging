# This python program answers the question on to 
# invest X dollar amount into QQQ ETF within as year
# when using dollar cost averaging,
# 1. What is the best investment frequecy: daily, weekly or monthly.
# 2. What is the best investment year
# to maximise the total return and the average annual return
# Note that the data file "data/HistoricalData_QQQ_2015_2025.csv" is dummy 
#                         which only includes the header and column names. 
# User needs to download the QQQ ETF historical daily price from nasdaq.com 
#                         or Yahoo Finance. 

import pandas as pd

if __name__ == '__main__':



    # Load and sort QQQ data
    file_path = "data/HistoricalData_QQQ_2015_2025.csv"
    df = pd.read_csv(file_path, skiprows=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df = df[['Date', 'High']]
    df.reset_index(drop=True, inplace=True)

    # Set global parameters
    X = 10000
    months = 12
    frequencies = {'daily': 'D', 'weekly': 'W', 'monthly': 'MS'}
    final_date = df.iloc[-1]['Date']
    final_price = df.iloc[-1]['High']

    # Helper to align non-trading DCA dates to next available trading day
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

    # Master dictionary to store all results
    all_results = {}

    for start_year in range(2016, 2025):  # 2016 to 2024 inclusive
        print(f"\n=== Starting Year: {start_year} ===")
        year_results = {}

        start_date = pd.to_datetime(f"{start_year}-01-01")
        end_date = start_date + pd.DateOffset(months=months)

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
                shares = amount_per_period / row['High']
                total_shares += shares

            final_value = total_shares * final_price
            duration_years = (final_date - start_date).days / 365.25
            avg_annual_gain = 100 * ((final_value - X) / (X * duration_years))

            year_results[freq_label] = {
                'total_shares': total_shares,
                'final_value': final_value,
                'avg_annual_gain': avg_annual_gain
            }

            print(f"Shares: {total_shares:.4f} | Final Value: ${final_value:,.2f} | Avg Annual Gain: {avg_annual_gain:.2f}%")

        all_results[start_year] = year_results

    # Summary Table
    print("\n=== SUMMARY TABLE ===")
    summary = []
    for year, freqs in all_results.items():
        for freq, res in freqs.items():
            summary.append({
                'Start Year': year,
                'Frequency': freq,
                'Shares': res['total_shares'],
                'Final Value': res['final_value'],
                'Avg Annual Gain (%)': res['avg_annual_gain']
            })

    summary_df = pd.DataFrame(summary)
    print(summary_df.sort_values(['Start Year', 'Frequency']).to_string(index=False))

    # Summary Table with Total Gain
    print("\n=== SUMMARY TABLE ===")
    summary = []
    for year, freqs in all_results.items():
        for freq, res in freqs.items():
            summary.append({
                'Start Year': year,
                'Frequency': freq,
                'Shares': res['total_shares'],
                'Initial Value': X,
                'Final Value': res['final_value'],
                'Total Gain ($)': res['final_value'] - X,
                'Avg Annual Gain (%)': res['avg_annual_gain']
            })

    summary_df = pd.DataFrame(summary)
    summary_df = summary_df.sort_values(['Start Year', 'Frequency'])

    # Display neatly
    pd.set_option("display.float_format", "{:,.2f}".format)
    print(summary_df.to_string(index=False))

    # Optionally save to file
    summary_df.to_csv("data/DCA_Summary_2016_2024.csv", index=False)

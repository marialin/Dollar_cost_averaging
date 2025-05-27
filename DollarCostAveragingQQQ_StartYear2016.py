import pandas as pd

if __name__ == '__main__':
    # Load and sort QQQ data (latest first, reverse to oldest first)
    file_path = "data/HistoricalData_QQQ_2015_2025.csv"
    df = pd.read_csv(file_path, skiprows=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df = df[['Date', 'High']]
    df.reset_index(drop=True, inplace=True)

    # Set parameters
    X = 100000
    start_year = 2016
    months = 12
    frequencies = {'daily': 'D', 'weekly': 'W', 'monthly': 'MS'}
    start_date = pd.to_datetime(f"{start_year}-01-01")
    end_date = start_date + pd.DateOffset(months=months)

    # Final valuation
    final_date = df.iloc[-1]['Date']
    final_price = df.iloc[-1]['High']

    # Helper: find next available trading day
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

    # Store results
    results = {}

    for freq_label, freq_code in frequencies.items():
        print(f"=== Frequency: {freq_label.upper()} ===")

        raw_dca_dates = pd.date_range(start=start_date, end=end_date, freq=freq_code)
        aligned_dates = align_to_trading_days(raw_dca_dates, df['Date'])

        print(f"Generated {len(aligned_dates)} aligned investment dates:")
        print([d.strftime('%Y-%m-%d') for d in aligned_dates], "\n")

        dca_df = df[df['Date'].isin(aligned_dates)]

        if dca_df.empty:
            print("No matching dates found after alignment. Skipping...\n")
            continue

        amount_per_period = X / len(dca_df)
        print(f"Amount invested per period: {amount_per_period:.2f}\n")

        total_shares = 0
        for i, row in dca_df.iterrows():
            date = row['Date']
            price = row['High']
            shares = amount_per_period / price
            total_shares += shares
            print(f"{date.strftime('%Y-%m-%d')} | Price (High): {price:.2f} | Shares bought: {shares:.4f}")

        final_value = total_shares * final_price
        duration_years = (final_date - start_date).days / 365.25
        avg_annual_gain = 100 * ((final_value - X) / (X * duration_years))

        print(f"\nTotal shares accumulated: {total_shares:.4f}")
        print(f"Final value as of {final_date.strftime('%Y-%m-%d')}: ${final_value:,.2f}")
        print(f"Duration: {duration_years:.2f} years")
        print(f"Average Annual Gain: {avg_annual_gain:.2f}%\n")

        results[freq_label] = {
            'total_shares': total_shares,
            'final_value': final_value,
            'avg_annual_gain': avg_annual_gain
        }

    # Summary
    print("\n==== SUMMARY OF RESULTS ====\n")
    for freq, data in results.items():
        print(f"{freq.capitalize():<10} | Shares: {data['total_shares']:.4f} | Final Value: ${data['final_value']:,.2f} | Avg Annual Gain: {data['avg_annual_gain']:.2f}%")

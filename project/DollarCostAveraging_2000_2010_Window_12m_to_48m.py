# To address the issue of potential losses due to unfortunate 
# entry timing—such as investing during a market peak—we can 
# consider extending the DCA investment window to 2, 3, or 
# even 4 years. A longer DCA window may provide a better 
# smoothing effect, reducing the risk associated with 
# short-term market volatility.
#
# To evaluate this approach, we conducted a study comparing 
# the total return of investing USD 2 million into QQQ using
# monthly DCA over different window periods: 12, 24, 36, and 
# 48 months. For each window length, we analyzed various 
# starting years (from 2000 to 2010 minus the window length) 
# and calculated the investment value as of 31 December 2010. 
# This analysis helps identify the optimal DCA window 
# that balances market timing risk with the goal of fully 
# investing the allocated capital.
#
# What this program does:
# 1. Loads and cleans QQQ data.
# 2. Runs DCA for 12, 24, 36, and 48 months.
# 3. Calculates the total shares bought and value on 2010-12-31.
# 4. Sorts results by window duration first, then by start year.
# 5. Outputs the results to screen and saves them to CSV.

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

    # Global investment settings
    X = 2_000_000  # Total investment
    final_date = pd.to_datetime('2010-12-31')
    final_price_row = df[df['Date'] <= final_date].iloc[-1]
    final_price = final_price_row['High']

    # Align to trading days
    def align_to_trading_days(dates, trading_days):
        trading_days = set(trading_days)
        aligned = []
        for date in dates:
            while date not in trading_days:
                date += pd.Timedelta(days=1)
                if date > df['Date'].iloc[-1]:
                    break
            if date in trading_days:
                aligned.append(date)
        return aligned

    # Study monthly DCA for windows 12, 24, 36, 48 months
    windows = [12, 24, 36, 48]
    results = []

    for window in windows:
        for start_year in range(2000, 2011 - (window // 12)):
            start_date = pd.to_datetime(f"{start_year}-01-01")
            end_date = pd.to_datetime(f"{start_year + (window // 12) - 1}-12-31")

            raw_dca_dates = pd.date_range(start=start_date, end=end_date, freq='MS')
            aligned_dates = align_to_trading_days(raw_dca_dates, df['Date'])

            dca_df = df[df['Date'].isin(aligned_dates)]
            if dca_df.empty:
                continue

            amount_per_period = X / len(dca_df)
            total_shares = sum(amount_per_period / row['High'] for _, row in dca_df.iterrows())

            final_value = total_shares * final_price
            total_gain = final_value - X

            results.append({
                'Start Year': start_year,
                'Frequency': f'monthly ({window}m)',
                'Shares': total_shares,
                'Initial Value': X,
                'Value on 31 Dec 2010': final_value,
                'Total Gain': total_gain
            })

    # Convert to DataFrame and sort by window first, then start year
    summary_df = pd.DataFrame(results)
    summary_df['Window'] = summary_df['Frequency'].str.extract(r'(\d+)').astype(int)
    summary_df = summary_df.sort_values(['Window', 'Start Year'])
    summary_df.drop(columns='Window', inplace=True)

    summary_df.reset_index(drop=True, inplace=True)
    print(summary_df.to_string(index=False))

    # Save to CSV
    summary_df.to_csv("data/DCA_Monthly_12_24_36_48_Summary.csv", index=False)

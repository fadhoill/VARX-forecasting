import os
import yfinance as yf

# 1. Tentukan nama folder
output_folder = 'data'

# 2. Buat folder jika belum ada
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

# 3. Tentukan kode saham (ticker) dan rentang waktu
tickers = ['NVDA', '000660.KS', '^VIX']  # NVDA untuk NVIDIA, 000660.KS untuk SK hynix
data = yf.download(tickers, start='2022-11-01', end='2026-11-01')

vix_data = yf.download('^VIX', start='2022-11-01', end='2026-11-01')

# 4. Simpan ke file CSV di dalam folder 'data'
file_path = os.path.join(output_folder, f'raw_data_daily.csv')
data.to_csv(file_path)

print(f'Data berhasil disimpan di: {file_path}')
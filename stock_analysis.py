import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FinancialAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Stock Analysis Tool (SSAT)")
        self.create_widgets()
        self.data = None

    def create_widgets(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')  # Modern theme

        # Load Button
        self.load_button = ttk.Button(self.root, text="Load CSV File", command=self.load_file)
        self.load_button.pack(pady=10)

        # Results Textbox
        self.result_text = tk.Text(self.root, height=10, width=80, state=tk.DISABLED, font=("Helvetica", 12))
        self.result_text.pack(pady=10)

        # Matplotlib Figure
        self.figure = plt.Figure(figsize=(14, 12))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            messagebox.showinfo("File Loaded", "CSV file loaded successfully!")
            self.analyze_data()
        else:
            messagebox.showwarning("No File", "No file selected. Please select a CSV file.")

    def calculate_indicators(self):
        # Convert the Date column to datetime
        self.data['Date'] = pd.to_datetime(self.data['Date'])

        # Calculate the moving averages
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data['SMA_200'] = self.data['Close'].rolling(window=200).mean()

        # Calculate the Relative Strength Index (RSI)
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

        # Calculate the MACD
        self.data['EMA_12'] = self.data['Close'].ewm(span=12, adjust=False).mean()
        self.data['EMA_26'] = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = self.data['EMA_12'] - self.data['EMA_26']
        self.data['Signal_Line'] = self.data['MACD'].ewm(span=9, adjust=False).mean()

    def plot_data(self):
        self.figure.clear()

        # Filter the data to include only the period where the indicators are calculated
        filtered_data = self.data.dropna(subset=['SMA_50', 'SMA_200', 'RSI', 'MACD', 'Signal_Line'])

        # Plot the technical indicators
        ax1, ax2, ax3 = self.figure.subplots(3, 1, sharex=True)

        # Price and moving averages
        ax1.plot(filtered_data['Date'], filtered_data['Close'], label='Close Price')
        ax1.plot(filtered_data['Date'], filtered_data['SMA_50'], label='50-day SMA', linestyle='--')
        ax1.plot(filtered_data['Date'], filtered_data['SMA_200'], label='200-day SMA', linestyle='--')
        ax1.set_title('Price and Moving Averages')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(True)

        # RSI
        ax2.plot(filtered_data['Date'], filtered_data['RSI'], label='RSI')
        ax2.axhline(70, color='red', linestyle='--')
        ax2.axhline(30, color='green', linestyle='--')
        ax2.set_title('Relative Strength Index (RSI)')
        ax2.set_ylabel('RSI')
        ax2.legend()
        ax2.grid(True)

        # MACD
        ax3.plot(filtered_data['Date'], filtered_data['MACD'], label='MACD')
        ax3.plot(filtered_data['Date'], filtered_data['Signal_Line'], label='Signal Line', linestyle='--')
        ax3.set_title('MACD and Signal Line')
        ax3.set_ylabel('MACD')
        ax3.legend()
        ax3.grid(True)

        self.canvas.draw()

    def analyze_data(self):
        self.calculate_indicators()
        latest_data = self.data.dropna(subset=['SMA_50', 'SMA_200', 'RSI', 'MACD', 'Signal_Line']).iloc[-1]

        # Extract the latest values for the indicators
        latest_close = latest_data['Close']
        latest_sma_50 = latest_data['SMA_50']
        latest_sma_200 = latest_data['SMA_200']
        latest_rsi = latest_data['RSI']
        latest_macd = latest_data['MACD']
        latest_signal_line = latest_data['Signal_Line']

        recommendation = "Hold"
        recommendation_color = "yellow"

        # Decision criteria for recommendation
        if latest_close > latest_sma_50 > latest_sma_200 and latest_rsi < 70 and latest_macd > latest_signal_line:
            recommendation = "Buy"
            recommendation_color = "green"
        elif latest_close < latest_sma_50 < latest_sma_200 or latest_rsi > 70 or latest_macd < latest_signal_line:
            recommendation = "Sell"
            recommendation_color = "red"

        result_text = (
            f"Latest Close: {latest_close:.2f}\n"
            f"50-day SMA: {latest_sma_50:.2f}\n"
            f"200-day SMA: {latest_sma_200:.2f}\n"
            f"RSI: {latest_rsi:.2f}\n"
            f"MACD: {latest_macd:.2f}\n"
            f"Signal Line: {latest_signal_line:.2f}\n"
            f"Recommendation: {recommendation}"
        )
        
        self.result_text.config(state=tk.NORMAL, fg=recommendation_color)
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result_text)
        self.result_text.config(state=tk.DISABLED)

        self.plot_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialAnalyzerApp(root)
    root.mainloop()

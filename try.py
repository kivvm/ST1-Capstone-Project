import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



class NetflixStockPredictor:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Netflix Stock Price Predictor")
        self.data = pd.read_csv("NFLX.csv")
        self.sliders = []

        self.data = self.data.drop('Date', axis='columns')
        self.data = self.data.drop('Open', axis='columns')
        self.data = self.data.drop('Adj Close', axis='columns')
        self.data = self.data.drop('Volume', axis='columns')
        self.X = self.data.drop('Close', axis=1).values
        self.y = self.data['Close'].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

        self.createWidgets()

    def createWidgets(self):
        self.high_label = tk.Label(self.master, text ='High')
        self.high_label.config(font=('comic sans MS', 10))
        self.high_label.grid(row=1, column=2)
        self.high_entry = tk.Entry(self.master)
        self.high_entry.grid(row=1, column=3)
        self.low_label = tk.Label(self.master, text ='Low')
        self.low_label.config(font=('comic sans MS', 10))
        self.low_label.grid(row=2, column=2)
        self.low_entry = tk.Entry(self.master)
        self.low_entry.grid(row=2, column=3)
        self.predict_button = tk.Button(self.master, text='Predict Price', command=self.predict_price)
        self.predict_button.config(font=('comic sans MS', 10))
        # self.predict_button.grid(row=len(self.data.columns[:-1]), columnspan=2)
        self.predict_button.grid(row=3, column= 3)

        
    def predict_price(self):
        inputs = [float(self.high_entry.get()), float(self.low_entry.get())]
        price = self.model.predict([inputs])
        messagebox.showinfo('Predicted Price', f'The predicted netflix stock price is ${price[0]:.2f}')

    



if __name__ == '__main__':
    root = tk.Tk()
    app = NetflixStockPredictor(root)
    root.mainloop()
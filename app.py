import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_percentage_error

# Import custom modules
from config import stock_symbols
from utils.data_fetcher import get_stock_data
from utils.metrics_calculator import calculate_stock_metrics
from utils.arima_forecaster import ARIMAForecaster
from utils.ui_components import create_header, create_footer, create_sidebar

# Note: LSTM is not imported here to avoid TensorFlow initialization delays
LSTM_AVAILABLE = False

# Page Configuration
st.set_page_config(page_title="Stock Price Prediction", page_icon="📊", layout="wide")

# Custom header and footer
create_header()
create_footer()

# Header Section
st.markdown(
    '<div class="header animated-heading"><h1>Stock Data Analyzer</h1></div>',
    unsafe_allow_html=True,)

# Sidebar inputs
selected_stock, start_date, end_date = create_sidebar(stock_symbols)

if st.sidebar.button("Fetch Data"):
    if start_date >= end_date:
        st.error("Start date must be before end date.")
    else:
        stock_info = stock_symbols[selected_stock]
        st.markdown(f"""
            <h1 style="font-size: 36px;text-align:center;">{stock_info['name']}</h1>
            <p style="font-size: 22px;"><b>Founder:</b> {stock_info['founder']}</p>
            <p style="font-size: 22px;"><b>History:</b> {stock_info['history']}</p>
            <p style="font-size: 22px;"><b>Present Condition:</b> {stock_info['present_condition']}</p>
        """, unsafe_allow_html=True)

        # Add space between text and graph
        st.markdown("<br><br>", unsafe_allow_html=True)

        # Fetch stock data
        data = get_stock_data(selected_stock, start_date, end_date)
        
        if data is not None and 'Close' in data.columns:
            # Calculate stock metrics
            metrics = calculate_stock_metrics(data)

            # Extract scalar values from pandas Series
            highest_price = metrics['Highest Price'].iloc[0] if isinstance(metrics['Highest Price'], pd.Series) else metrics['Highest Price']
            lowest_price = metrics['Lowest Price'].iloc[0] if isinstance(metrics['Lowest Price'], pd.Series) else metrics['Lowest Price']
            average_price = metrics['Average Price'].iloc[0] if isinstance(metrics['Average Price'], pd.Series) else metrics['Average Price']

            # Use st.markdown with custom CSS for styling the text
            st.markdown(
                f"""
                <h3 style="font-size: 22px;">Highest Price: ₹{highest_price:.2f}</h3>
                <h3 style="font-size: 22px;">Lowest Price: ₹{lowest_price:.2f}</h3>
                 <h3 style="font-size: 22px;">Average Price: ₹{average_price:.2f}</h3>
                <h3 style="font-size: 22px;">Best Time to Sell: {metrics['Best Time to Sell']}</h3>
                <h3 style="font-size: 22px;">Best Time to Buy: {metrics['Best Time to Buy']}</h3>
                """, unsafe_allow_html=True
            )

        # Display stock data table
        st.markdown(
        f"<h2 style='text-align: center;'>Stock Data for {stock_symbols[selected_stock]['name']}</h2>",
        unsafe_allow_html=True
        )
        st.write(data)

        # Plot Closing Price
        st.markdown("<h3 style='text-align: center; font-size: 36px;'>Stock Closing Price</h3>", unsafe_allow_html=True)
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label="Closing Price", color='blue')
        plt.title(f"{stock_symbols[selected_stock]['name']} Stock Closing Price")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        st.pyplot(plt)

        # Add space between ARIMA Table and Plot Closing Price
        st.markdown("<br><br>", unsafe_allow_html=True)

        # ARIMA Forecasting
        st.markdown(
        "<h3 style='text-align: center; font-size: 36px;'>ARIMA Model Forecast</h3>",
        unsafe_allow_html=True
        )

        arima_forecaster = ARIMAForecaster()
        arima_forecast, arima_accuracy = arima_forecaster.forecast(data['Close'])
        
        st.markdown(f"<h3>ARIMA Model Accuracy: {arima_accuracy:.2f}%</h3>", unsafe_allow_html=True)

        # Plot ARIMA Forecast
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label="Actual Close Price", color='blue')
        plt.plot(pd.date_range(data.index[-1], periods=31, freq='B')[1:], arima_forecast, label="Forecasted", color='red')
        plt.title(f"ARIMA Forecast for {stock_symbols[selected_stock]['name']}")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        st.pyplot(plt)

        # ARIMA Forecast Table
        arima_forecast_dates = pd.date_range(data.index[-1], periods=31, freq='B')[1:]
        arima_forecast_df = pd.DataFrame({'Date': arima_forecast_dates, 'Forecasted Price': arima_forecast})
        arima_forecast_df['Date'] = pd.to_datetime(arima_forecast_df['Date'])
        arima_forecast_df['Forecasted Price'] = arima_forecast_df['Forecasted Price'].round(2)
        
        st.markdown(
        "<br><br><h2 style='text-align: center;'>ARIMA Forecast Table</h2><br>",
        unsafe_allow_html=True)
        st.dataframe(arima_forecast_df)

        # Add space between ARIMA Table and LSTM Section
        st.markdown("<br><br>", unsafe_allow_html=True)

        # LSTM Forecasting (only if available)
        if LSTM_AVAILABLE:
            st.markdown("<br><br><h3 style='text-align: center; font-size: 36px;'>LSTM Model Forecast</h3><br><br>", unsafe_allow_html=True)
            
            lstm_forecaster = LSTMForecaster()
            lstm_predictions, lstm_accuracy = lstm_forecaster.forecast(data['Close'])
            
            st.markdown(f"<h3>LSTM Model Accuracy: {lstm_accuracy:.2f}%</h3>", unsafe_allow_html=True)

            # Plot LSTM Predictions
            plt.figure(figsize=(12, 6))
            plt.plot(data['Close'], label="Actual Close Price", color='blue')
            plt.plot(data.index[-len(lstm_predictions):], lstm_predictions, label="LSTM Prediction", color='orange')
            plt.title(f"LSTM Model Prediction for {stock_symbols[selected_stock]['name']}")
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            st.pyplot(plt)

            # LSTM Prediction Table with rounded values
            st.markdown("<br><br><h2 style='text-align: center;'>LSTM Model Prediction Table</h2><br>", unsafe_allow_html=True)
            lstm_dates = data.index[-len(lstm_predictions):]
            lstm_df = pd.DataFrame({'Date': lstm_dates, 'Predicted Price': lstm_predictions.flatten()})
            lstm_df['Date'] = pd.to_datetime(lstm_df['Date'])
            lstm_df['Predicted Price'] = lstm_df['Predicted Price'].round(2)  # Round to 2 decimal places
            st.dataframe(lstm_df) 
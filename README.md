# 📊 Stock Data Analyzer

A comprehensive stock analysis and forecasting web application built with Streamlit, featuring advanced machine learning models for stock price prediction.

## 🌟 Features

### 📈 **Stock Analysis**
- **20+ Indian Stocks**: Comprehensive coverage of major Indian companies
- **Real-time Data**: Live stock data from Yahoo Finance API
- **Historical Analysis**: Data from 2000 to present
- **Company Information**: Founder details, history, and current status

### 🤖 **Machine Learning Models**
- **ARIMA Forecasting**: Statistical time series analysis
- **LSTM Neural Networks**: Deep learning for price prediction
- **Accuracy Metrics**: Model performance evaluation
- **30-day Forecasts**: Future price predictions

### 📊 **Advanced Analytics**
- **Technical Indicators**: RSI, MACD, Moving Averages
- **Risk Metrics**: Sharpe Ratio, VaR, Max Drawdown
- **Performance Metrics**: Total returns, volatility analysis
- **Volume Analysis**: Trading volume insights

### 🎨 **User Interface**
- **Modern Web App**: Built with Streamlit
- **Responsive Design**: Works on desktop and mobile
- **Interactive Charts**: Matplotlib visualizations
- **Professional Styling**: Custom CSS and themes

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PRANAV0494/Stock_Project.git
   cd Stock_Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
Stock_Project/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and stock data
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── utils/               # Utility modules
    ├── __init__.py
    ├── data_fetcher.py      # Stock data fetching
    ├── metrics_calculator.py # Financial metrics calculation
    ├── arima_forecaster.py  # ARIMA model implementation
    ├── lstm_forecaster.py   # LSTM neural network
    └── ui_components.py     # UI components and styling
```

## 🔧 Configuration

### Stock Symbols
The application includes 20 major Indian stocks:
- **IT Sector**: TCS, Infosys, Wipro, HCL Tech
- **Banking**: HDFC Bank, ICICI Bank, SBI
- **Energy**: Reliance, Coal India, Adani Green
- **Manufacturing**: Maruti, Bajaj Auto, Asian Paints
- **Others**: ITC, Titan, UltraTech Cement, Sun Pharma

### Model Parameters
- **ARIMA**: Order (5,1,0) with 30-day forecast
- **LSTM**: 60 time steps, 50 units, 10 epochs

## 📊 Usage Guide

### 1. **Select Stock**
   - Choose from the dropdown menu in the sidebar
   - View company information and history

### 2. **Set Date Range**
   - Select start and end dates for analysis
   - Data available from 2000 to present

### 3. **Fetch Data**
   - Click "Fetch Data" button
   - View stock metrics and performance

### 4. **Analyze Results**
   - **Basic Metrics**: Highest/lowest prices, best buy/sell times
   - **ARIMA Forecast**: Statistical price predictions
   - **LSTM Predictions**: AI-powered price forecasting
   - **Visualizations**: Interactive charts and graphs

## 🛠️ Technical Details

### **Technologies Used**
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **Statistics**: StatsModels
- **Data Source**: Yahoo Finance API
- **Visualization**: Matplotlib

### **Architecture**
- **Modular Design**: Separated concerns into utility modules
- **Error Handling**: Comprehensive error handling and logging
- **Type Hints**: Full Python type annotations
- **Documentation**: Detailed docstrings and comments

### **Performance Features**
- **Efficient Data Processing**: Optimized pandas operations
- **Model Caching**: Prevents unnecessary retraining
- **Memory Management**: Efficient data handling
- **Scalable Architecture**: Easy to extend and modify

## 📈 Model Performance

### **ARIMA Model**
- **Accuracy**: Typically 80-90%
- **Best For**: Short-term trends and seasonal patterns
- **Use Case**: Conservative forecasting

### **LSTM Model**
- **Accuracy**: Typically 80-90%
- **Best For**: Complex patterns and long-term trends
- **Use Case**: Advanced AI-powered predictions

## 🔍 API Reference

### **Data Fetcher**
```python
from utils.data_fetcher import get_stock_data

data = get_stock_data("TCS.NS", start_date, end_date)
```

### **Metrics Calculator**
```python
from utils.metrics_calculator import calculate_stock_metrics

metrics = calculate_stock_metrics(stock_data)
```

### **ARIMA Forecaster**
```python
from utils.arima_forecaster import ARIMAForecaster

forecaster = ARIMAForecaster()
forecast, accuracy = forecaster.forecast(data)
```

### **LSTM Forecaster**
```python
from utils.lstm_forecaster import LSTMForecaster

forecaster = LSTMForecaster()
predictions, accuracy = forecaster.forecast(data)
```

## 🚧 Future Enhancements

### **Planned Features**
- [ ] **Portfolio Analysis**: Multi-stock comparison
- [ ] **Real-time Updates**: Live data streaming
- [ ] **Export Functionality**: PDF/Excel reports
- [ ] **More Models**: XGBoost, Random Forest
- [ ] **Technical Indicators**: Advanced charting
- [ ] **Backtesting**: Historical strategy testing

### **Technical Improvements**
- [ ] **Model Persistence**: Save trained models
- [ ] **API Rate Limiting**: Better data source management
- [ ] **Performance Optimization**: Faster model training
- [ ] **Mobile App**: React Native version

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes**
4. **Add tests** (if applicable)
5. **Commit your changes**: `git commit -m 'Add feature'`
6. **Push to the branch**: `git push origin feature-name`
7. **Submit a pull request**

### **Development Setup**
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest

# Code formatting
black .

# Linting
flake8
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Pranav Maheshwari**
- **GitHub**: [@PRANAV0494](https://github.com/PRANAV0494)
- **LinkedIn**: [Pranav Maheshwari](https://www.linkedin.com/in/pranav-maheshwari-b76894187/)
- **Email**: pranavm494@gmail.com

## 🙏 Acknowledgments

- **Yahoo Finance**: For providing stock data
- **Streamlit**: For the amazing web framework
- **Open Source Community**: For the ML libraries
- **College Project**: Academic project for learning purposes

## 📞 Support

If you have any questions or need help:

1. **Check the documentation** above
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed description
4. **Contact the author** directly

## ⚠️ Disclaimer

**This application is for educational and research purposes only.**
- Stock predictions are not financial advice
- Always consult with financial professionals
- Past performance doesn't guarantee future results
- Use at your own risk

---

**⭐ Star this repository if you find it helpful!**

**🔄 Keep updated with the latest features and improvements.** 

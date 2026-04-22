"""
Metrics Calculator Module
Calculates various stock performance metrics
"""

import pandas as pd
from typing import Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_stock_metrics(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate comprehensive stock metrics from historical data
    
    Args:
        data (pd.DataFrame): Stock data with OHLCV columns
    
    Returns:
        Dict[str, Any]: Dictionary containing calculated metrics
    """
    try:
        logger.info("Calculating stock metrics")
        
        # Basic price metrics
        highest_price = data['Close'].max()
        lowest_price = data['Close'].min()
        average_price = data['Close'].mean()
        
        # Get the index (timestamp) of the highest and lowest price
        best_time_to_sell = data['Close'].idxmax()
        best_time_to_buy = data['Close'].idxmin()
        
        # Ensure we are working with a Timestamp, not a Series
        if isinstance(best_time_to_sell, pd.Series):
            best_time_to_sell = best_time_to_sell.iloc[0]
        if isinstance(best_time_to_buy, pd.Series):
            best_time_to_buy = best_time_to_buy.iloc[0]
        
        # Convert to string format
        best_time_to_sell_str = best_time_to_sell.strftime('%Y-%m-%d')
        best_time_to_buy_str = best_time_to_buy.strftime('%Y-%m-%d')
        
        # Calculate additional metrics
        total_return = ((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
        volatility = data['Close'].pct_change().std() * 100
        
        # Volume metrics
        avg_volume = data['Volume'].mean()
        max_volume = data['Volume'].max()
        
        metrics = {
            "Highest Price": highest_price,
            "Lowest Price": lowest_price,
            "Best Time to Sell": best_time_to_sell_str,
            "Best Time to Buy": best_time_to_buy_str,
            "Average Price": average_price,
            "Total Return (%)": total_return,
            "Volatility (%)": volatility,
            "Average Volume": avg_volume,
            "Max Volume": max_volume
        }
        
        logger.info("Successfully calculated stock metrics")
        return metrics
        
    except Exception as e:
        logger.error(f"Error calculating metrics: {str(e)}")
        return {}

def calculate_technical_indicators(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate technical indicators for the stock
    
    Args:
        data (pd.DataFrame): Stock data with OHLCV columns
    
    Returns:
        Dict[str, Any]: Dictionary containing technical indicators
    """
    try:
        logger.info("Calculating technical indicators")
        
        # Moving averages
        data['MA_20'] = data['Close'].rolling(window=20).mean()
        data['MA_50'] = data['Close'].rolling(window=50).mean()
        
        # RSI calculation
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD calculation
        exp1 = data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = exp1 - exp2
        data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
        
        indicators = {
            "MA_20": data['MA_20'].iloc[-1],
            "MA_50": data['MA_50'].iloc[-1],
            "RSI": data['RSI'].iloc[-1],
            "MACD": data['MACD'].iloc[-1],
            "Signal_Line": data['Signal_Line'].iloc[-1]
        }
        
        logger.info("Successfully calculated technical indicators")
        return indicators
        
    except Exception as e:
        logger.error(f"Error calculating technical indicators: {str(e)}")
        return {}

def calculate_risk_metrics(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate risk metrics for the stock
    
    Args:
        data (pd.DataFrame): Stock data with OHLCV columns
    
    Returns:
        Dict[str, Any]: Dictionary containing risk metrics
    """
    try:
        logger.info("Calculating risk metrics")
        
        # Calculate daily returns
        returns = data['Close'].pct_change().dropna()
        
        # Risk metrics
        sharpe_ratio = returns.mean() / returns.std() * (252 ** 0.5)  # Annualized
        max_drawdown = (data['Close'] / data['Close'].expanding().max() - 1).min()
        var_95 = returns.quantile(0.05)  # 95% VaR
        
        risk_metrics = {
            "Sharpe Ratio": sharpe_ratio,
            "Max Drawdown": max_drawdown,
            "Value at Risk (95%)": var_95,
            "Standard Deviation": returns.std(),
            "Skewness": returns.skew(),
            "Kurtosis": returns.kurtosis()
        }
        
        logger.info("Successfully calculated risk metrics")
        return risk_metrics
        
    except Exception as e:
        logger.error(f"Error calculating risk metrics: {str(e)}")
        return {} 
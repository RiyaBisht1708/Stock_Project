"""
Data Fetcher Module
Handles fetching stock data from Yahoo Finance API
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
from typing import Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_stock_data(stock_symbol: str, start_date: Union[str, datetime], end_date: Union[str, datetime]) -> Optional[pd.DataFrame]:
    """
    Fetch stock data from Yahoo Finance API
    
    Args:
        stock_symbol (str): Stock symbol (e.g., 'TCS.NS')
        start_date (Union[str, datetime]): Start date for data
        end_date (Union[str, datetime]): End date for data
    
    Returns:
        Optional[pd.DataFrame]: Stock data or None if failed
    """
    try:
        logger.info(f"Fetching data for {stock_symbol} from {start_date} to {end_date}")
        
        # Download stock data
        data = yf.download(stock_symbol, start=start_date, end=end_date)
        
        if data.empty:
            logger.warning(f"No data found for {stock_symbol}")
            return None
            
        logger.info(f"Successfully fetched {len(data)} records for {stock_symbol}")
        return data
        
    except Exception as e:
        logger.error(f"Error fetching data for {stock_symbol}: {str(e)}")
        return None

def validate_stock_symbol(stock_symbol: str) -> bool:
    """
    Validate if stock symbol exists
    
    Args:
        stock_symbol (str): Stock symbol to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        ticker = yf.Ticker(stock_symbol)
        info = ticker.info
        return info is not None and len(info) > 0
    except:
        return False

def get_stock_info(stock_symbol: str) -> Optional[dict]:
    """
    Get basic stock information
    
    Args:
        stock_symbol (str): Stock symbol
    
    Returns:
        Optional[dict]: Stock information or None
    """
    try:
        ticker = yf.Ticker(stock_symbol)
        info = ticker.info
        return info
    except Exception as e:
        logger.error(f"Error getting info for {stock_symbol}: {str(e)}")
        return None 
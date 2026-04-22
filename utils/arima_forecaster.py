"""
ARIMA Forecaster Module
Handles ARIMA model forecasting for stock prices
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_percentage_error
from typing import Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ARIMAForecaster:
    """
    ARIMA Model Forecaster for stock price prediction
    """
    
    def __init__(self, order: Tuple[int, int, int] = (5, 1, 0), forecast_steps: int = 30):
        """
        Initialize ARIMA Forecaster
        
        Args:
            order (Tuple[int, int, int]): ARIMA order (p, d, q)
            forecast_steps (int): Number of steps to forecast
        """
        self.order = order
        self.forecast_steps = forecast_steps
        self.model = None
        self.model_fit = None
        logger.info(f"ARIMA Forecaster initialized with order {order}")
    
    def fit(self, data: pd.Series) -> bool:
        """
        Fit ARIMA model to the data
        
        Args:
            data (pd.Series): Time series data to fit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info("Fitting ARIMA model")
            
            # Create and fit ARIMA model
            self.model = ARIMA(data, order=self.order)
            self.model_fit = self.model.fit()
            
            logger.info("ARIMA model fitted successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error fitting ARIMA model: {str(e)}")
            return False
    
    def forecast(self, data: pd.Series) -> Tuple[np.ndarray, float]:
        """
        Generate forecast using ARIMA model
        
        Args:
            data (pd.Series): Time series data
            
        Returns:
            Tuple[np.ndarray, float]: Forecast values and accuracy
        """
        try:
            logger.info("Generating ARIMA forecast")
            
            # Fit the model first
            if not self.fit(data):
                raise Exception("Failed to fit ARIMA model")
            
            # Generate forecast
            forecast = self.model_fit.forecast(steps=self.forecast_steps)
            
            # Calculate accuracy
            accuracy = self._calculate_accuracy(data, forecast)
            
            logger.info(f"ARIMA forecast generated successfully with {accuracy:.2f}% accuracy")
            return forecast, accuracy
            
        except Exception as e:
            logger.error(f"Error generating ARIMA forecast: {str(e)}")
            # Return default values
            return np.zeros(self.forecast_steps), 0.0
    
    def _calculate_accuracy(self, data: pd.Series, forecast: np.ndarray) -> float:
        """
        Calculate forecast accuracy using MAPE
        
        Args:
            data (pd.Series): Actual data
            forecast (np.ndarray): Forecasted values
            
        Returns:
            float: Accuracy percentage
        """
        try:
            # Use last 30 actual values for accuracy calculation
            actual_values = data[-30:].values
            
            # Ensure forecast has enough values
            if len(forecast) < len(actual_values):
                forecast_subset = forecast[:len(actual_values)]
            else:
                forecast_subset = forecast[:len(actual_values)]
            
            # Calculate MAPE
            mape = mean_absolute_percentage_error(actual_values, forecast_subset)
            
            # Convert to accuracy percentage
            accuracy = 100 - (mape * 100)
            
            return max(0, accuracy)  # Ensure non-negative
            
        except Exception as e:
            logger.error(f"Error calculating accuracy: {str(e)}")
            return 0.0
    
    def get_model_summary(self) -> str:
        """
        Get ARIMA model summary
        
        Returns:
            str: Model summary
        """
        if self.model_fit is not None:
            return str(self.model_fit.summary())
        else:
            return "Model not fitted yet"
    
    def get_forecast_confidence(self, data: pd.Series, confidence_level: float = 0.95) -> Tuple[np.ndarray, np.ndarray]:
        """
        Get forecast confidence intervals
        
        Args:
            data (pd.Series): Time series data
            confidence_level (float): Confidence level (0.95 for 95%)
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: Lower and upper confidence bounds
        """
        try:
            if not self.fit(data):
                raise Exception("Failed to fit ARIMA model")
            
            # Get forecast with confidence intervals
            forecast_result = self.model_fit.forecast(steps=self.forecast_steps)
            
            # For simplicity, return basic confidence intervals
            # In a production environment, you might want to use get_forecast() method
            std_dev = data.std()
            z_score = 1.96  # 95% confidence interval
            
            lower_bound = forecast_result - (z_score * std_dev)
            upper_bound = forecast_result + (z_score * std_dev)
            
            return lower_bound, upper_bound
            
        except Exception as e:
            logger.error(f"Error getting confidence intervals: {str(e)}")
            return np.zeros(self.forecast_steps), np.zeros(self.forecast_steps) 
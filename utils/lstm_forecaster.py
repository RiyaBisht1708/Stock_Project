"""
LSTM Forecaster Module
Handles LSTM neural network forecasting for stock prices
"""

import os
import warnings

# Suppress TensorFlow warnings and optimize initialization
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_percentage_error
from typing import Tuple
import logging

# Import TensorFlow with optimizations
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LSTMForecaster:
    """
    LSTM Neural Network Forecaster for stock price prediction
    """
    
    def __init__(self, time_steps: int = 60, units: int = 50, epochs: int = 10, batch_size: int = 32):
        """
        Initialize LSTM Forecaster
        
        Args:
            time_steps (int): Number of time steps for LSTM input
            units (int): Number of LSTM units
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
        """
        self.time_steps = time_steps
        self.units = units
        self.epochs = epochs
        self.batch_size = batch_size
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None
        logger.info(f"LSTM Forecaster initialized with {units} units, {time_steps} time steps")
    
    def _create_lstm_dataset(self, data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Create LSTM dataset with time steps
        
        Args:
            data (np.ndarray): Scaled data array
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: X and y data for LSTM
        """
        x_data, y_data = [], []
        for i in range(self.time_steps, len(data)):
            x_data.append(data[i-self.time_steps:i, 0])
            y_data.append(data[i, 0])
        return np.array(x_data), np.array(y_data)
    
    def _build_model(self, input_shape: Tuple[int, int]) -> Sequential:
        """
        Build LSTM model architecture
        
        Args:
            input_shape (Tuple[int, int]): Input shape for LSTM
            
        Returns:
            Sequential: Compiled LSTM model
        """
        model = Sequential()
        model.add(LSTM(units=self.units, return_sequences=True, input_shape=input_shape))
        model.add(LSTM(units=self.units))
        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    def fit(self, data: pd.Series) -> bool:
        """
        Fit LSTM model to the data
        
        Args:
            data (pd.Series): Time series data to fit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            logger.info("Fitting LSTM model")
            
            # Scale the data
            scaled_data = self.scaler.fit_transform(data.values.reshape(-1, 1))
            
            # Create LSTM dataset
            x_data, y_data = self._create_lstm_dataset(scaled_data)
            
            # Reshape for LSTM
            x_data = x_data.reshape((x_data.shape[0], x_data.shape[1], 1))
            y_data = y_data.reshape(-1, 1)
            
            # Build and train model
            self.model = self._build_model((x_data.shape[1], 1))
            self.model.fit(x_data, y_data, epochs=self.epochs, batch_size=self.batch_size, verbose=0)
            
            logger.info("LSTM model fitted successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error fitting LSTM model: {str(e)}")
            return False
    
    def forecast(self, data: pd.Series) -> Tuple[np.ndarray, float]:
        """
        Generate forecast using LSTM model
        
        Args:
            data (pd.Series): Time series data
            
        Returns:
            Tuple[np.ndarray, float]: Forecast values and accuracy
        """
        try:
            logger.info("Generating LSTM forecast")
            
            # Fit the model first
            if not self.fit(data):
                raise Exception("Failed to fit LSTM model")
            
            # Scale the data
            scaled_data = self.scaler.fit_transform(data.values.reshape(-1, 1))
            
            # Create LSTM dataset for predictions
            x_data, y_data = self._create_lstm_dataset(scaled_data)
            
            # Reshape for LSTM
            x_data = x_data.reshape((x_data.shape[0], x_data.shape[1], 1))
            
            # Generate predictions
            lstm_predictions = self.model.predict(x_data)
            
            # Inverse transform predictions
            lstm_predictions = self.scaler.inverse_transform(lstm_predictions.reshape(-1, 1))
            
            # Calculate accuracy
            accuracy = self._calculate_accuracy(data, lstm_predictions)
            
            logger.info(f"LSTM forecast generated successfully with {accuracy:.2f}% accuracy")
            return lstm_predictions, accuracy
            
        except Exception as e:
            logger.error(f"Error generating LSTM forecast: {str(e)}")
            # Return default values
            return np.zeros(len(data) - self.time_steps), 0.0
    
    def _calculate_accuracy(self, data: pd.Series, predictions: np.ndarray) -> float:
        """
        Calculate forecast accuracy using MAPE
        
        Args:
            data (pd.Series): Actual data
            predictions (np.ndarray): Predicted values
            
        Returns:
            float: Accuracy percentage
        """
        try:
            # Get actual values corresponding to predictions
            actual_values = data[-len(predictions):].values
            
            # Calculate MAPE
            mape = mean_absolute_percentage_error(actual_values, predictions.flatten())
            
            # Convert to accuracy percentage
            accuracy = 100 - (mape * 100)
            
            return max(0, accuracy)  # Ensure non-negative
            
        except Exception as e:
            logger.error(f"Error calculating accuracy: {str(e)}")
            return 0.0
    
    def predict_future(self, data: pd.Series, future_steps: int = 30) -> np.ndarray:
        """
        Predict future values beyond the training data
        
        Args:
            data (pd.Series): Historical data
            future_steps (int): Number of future steps to predict
            
        Returns:
            np.ndarray: Future predictions
        """
        try:
            logger.info(f"Predicting {future_steps} future steps")
            
            if not self.fit(data):
                raise Exception("Failed to fit LSTM model")
            
            # Get the last time_steps values
            last_sequence = data[-self.time_steps:].values.reshape(-1, 1)
            last_sequence_scaled = self.scaler.transform(last_sequence)
            
            future_predictions = []
            current_sequence = last_sequence_scaled.copy()
            
            for _ in range(future_steps):
                # Reshape for prediction
                x_input = current_sequence.reshape((1, self.time_steps, 1))
                
                # Predict next value
                next_pred = self.model.predict(x_input, verbose=0)
                
                # Add to predictions
                future_predictions.append(next_pred[0, 0])
                
                # Update sequence for next prediction
                current_sequence = np.roll(current_sequence, -1)
                current_sequence[-1] = next_pred[0, 0]
            
            # Inverse transform predictions
            future_predictions = np.array(future_predictions).reshape(-1, 1)
            future_predictions = self.scaler.inverse_transform(future_predictions)
            
            logger.info("Future predictions generated successfully")
            return future_predictions.flatten()
            
        except Exception as e:
            logger.error(f"Error predicting future values: {str(e)}")
            return np.zeros(future_steps)
    
    def get_model_summary(self) -> str:
        """
        Get LSTM model summary
        
        Returns:
            str: Model summary
        """
        if self.model is not None:
            # Create a string representation of the model
            summary = []
            summary.append("LSTM Model Summary:")
            summary.append(f"Time Steps: {self.time_steps}")
            summary.append(f"LSTM Units: {self.units}")
            summary.append(f"Training Epochs: {self.epochs}")
            summary.append(f"Batch Size: {self.batch_size}")
            summary.append(f"Total Parameters: {self.model.count_params()}")
            return "\n".join(summary)
        else:
            return "Model not fitted yet" 
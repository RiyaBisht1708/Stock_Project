"""
UI Components Module
Handles Streamlit UI components and styling
"""

import streamlit as st
from datetime import datetime
from typing import Tuple, Dict, Any

def create_header():
    """Create custom header with styling"""
    st.markdown("""
        <div style="background-color:#4CAF50;padding:15px;border-radius:10px;">
            <h1 style="color:white;text-align:center;">Stock Data Analyzer</h1>
        </div>
    """, unsafe_allow_html=True)

def create_footer():
    """Create custom footer with credits"""
    st.markdown("""
        <style>
            footer {visibility: hidden;} /* Hide default Streamlit footer */
            .custom-footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: black;
                color: white;
                text-align: center;
                padding: 10px 0;
                font-size: 18px;
                z-index: 9999;
            }
        </style>
        <div class="custom-footer">
            Developed by Riya Bisht | Stock Data Project
        </div>
    """, unsafe_allow_html=True)

def create_sidebar(stock_symbols: Dict[str, Any]) -> Tuple[str, datetime, datetime]:
    """
    Create sidebar with stock selection and date inputs
    
    Args:
        stock_symbols (Dict[str, Any]): Dictionary of stock symbols and metadata
        
    Returns:
        Tuple[str, datetime, datetime]: Selected stock, start date, end date
    """
    st.sidebar.header("Enter Stock Details")
    
    # Convert stock symbols dictionary to list of display names
    stock_options = [f"{symbol} - {details['name']}" for symbol, details in stock_symbols.items()]
    selected_stock_option = st.sidebar.selectbox("Select Stock Symbol", stock_options)
    
    # Extract the stock symbol from the selected option
    selected_stock = selected_stock_option.split(" - ")[0]
    
    # Calendar date range from 2000 to today
    min_date = datetime(2000, 1, 1)
    max_date = datetime.today()
    
    start_date = st.sidebar.date_input(
        "Start Date", 
        datetime(2020, 1, 1), 
        min_value=min_date, 
        max_value=max_date
    )
    
    end_date = st.sidebar.date_input(
        "End Date", 
        datetime(2025, 1, 1), 
        min_value=min_date, 
        max_value=max_date
    )
    
    return selected_stock, start_date, end_date

def create_stock_info_display(stock_info: Dict[str, Any]) -> None:
    """
    Display stock information in a formatted way
    
    Args:
        stock_info (Dict[str, Any]): Stock information dictionary
    """
    st.markdown(f"""
        <h1 style="font-size: 36px;text-align:center;">{stock_info['name']}</h1>
        <p style="font-size: 22px;"><b>Founder:</b> {stock_info['founder']}</p>
        <p style="font-size: 22px;"><b>History:</b> {stock_info['history']}</p>
        <p style="font-size: 22px;"><b>Present Condition:</b> {stock_info['present_condition']}</p>
    """, unsafe_allow_html=True)

def create_metrics_display(metrics: Dict[str, Any]) -> None:
    """
    Display stock metrics in a formatted way
    
    Args:
        metrics (Dict[str, Any]): Stock metrics dictionary
    """
    # Extract scalar values from pandas Series
    highest_price = metrics['Highest Price'].iloc[0] if hasattr(metrics['Highest Price'], 'iloc') else metrics['Highest Price']
    lowest_price = metrics['Lowest Price'].iloc[0] if hasattr(metrics['Lowest Price'], 'iloc') else metrics['Lowest Price']
    average_price = metrics['Average Price'].iloc[0] if hasattr(metrics['Average Price'], 'iloc') else metrics['Average Price']
    
    st.markdown(
        f"""
        <h3 style="font-size: 22px;">Highest Price: ₹{highest_price:.2f}</h3>
        <h3 style="font-size: 22px;">Lowest Price: ₹{lowest_price:.2f}</h3>
        <h3 style="font-size: 22px;">Average Price: ₹{average_price:.2f}</h3>
        <h3 style="font-size: 22px;">Best Time to Sell: {metrics['Best Time to Sell']}</h3>
        <h3 style="font-size: 22px;">Best Time to Buy: {metrics['Best Time to Buy']}</h3>
        """, unsafe_allow_html=True
    )

def create_section_header(title: str, size: int = 36) -> None:
    """
    Create a section header with consistent styling
    
    Args:
        title (str): Header title
        size (int): Font size for the header
    """
    st.markdown(f"<h3 style='text-align: center; font-size: {size}px;'>{title}</h3>", unsafe_allow_html=True)

def create_data_table(title: str, data: Any) -> None:
    """
    Create a data table with title
    
    Args:
        title (str): Table title
        data (Any): Data to display
    """
    st.markdown(f"<h2 style='text-align: center;'>{title}</h2>", unsafe_allow_html=True)
    st.write(data)

def add_spacing(lines: int = 2) -> None:
    """
    Add vertical spacing between sections
    
    Args:
        lines (int): Number of line breaks to add
    """
    st.markdown("<br>" * lines, unsafe_allow_html=True)

def create_error_message(message: str) -> None:
    """
    Create a styled error message
    
    Args:
        message (str): Error message to display
    """
    st.error(message)

def create_success_message(message: str) -> None:
    """
    Create a styled success message
    
    Args:
        message (str): Success message to display
    """
    st.success(message)

def create_info_message(message: str) -> None:
    """
    Create a styled info message
    
    Args:
        message (str): Info message to display
    """
    st.info(message)

def create_warning_message(message: str) -> None:
    """
    Create a styled warning message
    
    Args:
        message (str): Warning message to display
    """
    st.warning(message) 
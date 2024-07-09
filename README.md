# Stock Trends
#### Video Demo:  <URL HERE>
#### Description:

## Project Overview

Welcome to the Stock Trends Project! This project is designed to help track various stock trends using data from Yahoo Finance. Whether you're interested in identifying patterns like the golden cross, death cross, high and low prices, or volume changes, this project has you covered. I'll explain each part of the project, the files involved, and the choices I made along the way. The Stock Trends Project is built using Python and several key libraries including Matplotlib, yfinance, Flask, and scikit-learn. The project aims to analyze stock data, visualize trends, and use a linear regression model to predict stock prices. The main functionalities include downloading stock data, calculating exponential moving averages (EMAs), plotting high vs low prices, and predicting closing prices based on various features.

## File Descriptions

### `main.py`

The `main.py` file is the core of the project, containing the main logic for data processing, visualization, and the web interface. Here's a breakdown of its contents:

- **Imports**: The necessary libraries are imported at the beginning, including Matplotlib for plotting, yfinance for fetching stock data, Flask for creating the web interface, and scikit-learn for building and evaluating the linear regression model.
- **Flask App**: The Flask application is created and configured to handle requests.
- **Handle Request**: The main route (`/`) handles both GET and POST requests. For POST requests, it fetches the stock data for the specified stock and time period, calculates EMAs, and generates various plots (EMA, high vs low prices, predicted vs actual values, and closing price vs volume). These plots are saved as images and displayed on the web page.
- **Linear Regression**: The linear regression model is trained on features like opening price, high price, low price, volume, and EMAs to predict the closing price. The model's performance is evaluated using metrics like mean squared error, mean absolute error, and R-squared score.
- **Templates**: The results are rendered using HTML templates.

### `templates/index.html`

The `index.html` file is the main web page where users can input the stock name and the number of years to analyze. Here's a breakdown of its contents:

- **HTML5 Document Structure**: Sets up the basic structure with `<!DOCTYPE html>` and `<html>` tags.
- **Head Section**:
  - `<link>` tag to include a favicon.
  - `<title>` tag to set the page title.
- **Body Section**:
  - `style` attribute to set the background color.
  - `<script>` tag to include Bootstrap JS from a CDN.
  - `<nav>` element for a sticky-top navbar with a dark theme.
  - `<div>` element to center the main content vertically and horizontally.
  - `<p>` element for the page heading.
  - `<div>` element with a form for user input:
    - **Stock Name Input**: `<input>` element for the stock name.
    - **Years Input**: `<input>` element for the number of years.
    - **Submit Button**: `<button>` element to submit the form.

## Design Choices

1. **Technology Stack**: I chose Python for its versatility and the availability of powerful libraries like Matplotlib, yfinance, Flask, and scikit-learn. Flask was chosen for the web interface because it is lightweight and easy to set up.

2. **Data Visualization**: Matplotlib was used to create clear and informative plots. Each plot is designed to highlight a specific trend or aspect of the stock data, making it easier for users to understand the stock's performance.

3. **Machine Learning**: A linear regression model was implemented to predict closing prices. This choice was made because linear regression is simple, interpretable, and sufficient for this project's scope.

4. **User Interface**: The web interface is designed to be user-friendly, with a clean and simple layout using Bootstrap. This ensures that users can easily input the required data and view the results.

## Conclusion

The Stock Trends Project provides a comprehensive tool for analyzing stock trends and predicting stock prices using data from Yahoo Finance. By combining data visualization with machine learning, this project offers valuable insights into stock performance. I hope this README helps you understand the project's structure and functionalities. Feel free to explore!

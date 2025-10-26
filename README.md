# SEC Revenue Analysis Tool

A dynamic web application that fetches and visualizes company revenue data from the U.S. Securities and Exchange Commission (SEC) XBRL API.

## Project Overview

This project provides an interactive dashboard for analyzing company revenue trends using official SEC financial data. The application defaults to Tesla, Inc. but supports dynamic loading of any publicly traded company by CIK (Central Index Key).

## Features

- **SEC API Integration**: Fetches real-time revenue data from SEC's XBRL API
- **Statistical Analysis**: Calculates average, maximum, and minimum revenues
- **Interactive Visualization**: Dynamic Chart.js-powered revenue trend chart
- **Multi-Company Support**: Query any company using `?CIK=` parameter
- **Responsive Design**: Modern, gradient-styled interface
- **No Page Reload**: Dynamic data fetching and UI updates via JavaScript

## Setup Instructions

### Prerequisites

- Python 3.6+ (for data fetching script)
- Modern web browser with JavaScript enabled
- Internet connection (for SEC API access and Chart.js CDN)

### Installation

1. Clone or download this repository
2. No additional dependencies required for the web interface
3. For Python script: uses only standard library modules

### Running the Application

#### Option 1: View Pre-Generated Data

Simply open `index.html` in your web browser:
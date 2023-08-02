# Data Analysis Dashboard

## Overview

This project is a web-based data analysis dashboard that allows users to explore and visualize data using SQL queries. The dashboard is built using Flask, a lightweight Python web framework, and uses SQLite as the backend database for data storage and retrieval. The interactive dashboard provides users with an intuitive interface to view and analyze sample data presented in various chart types, such as bar charts, line charts, or scatter plots.

## Features

- Data visualization using Plotly.js
- SQL database integration for data storage/retrieval
- Sample data usage
- Customization

## Installation

1. Install the required dependencies:
pip install -r requirements.txt (Flask, plotly, sqlite3)

2. Run the application:
python app.py

3. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to use dashboard

## Usage

- The dashboard displays a bar chart by default, visualizing the sample data stored in the SQLite database
- You can explore the data and interact with the chart using the web interface


## Sample Data

SQLite database `data.db` can contain sample data for demonstration purposes. The data is stored in the `data` table, which has columns `id`, `name`, and `value` There is a test `data.py` made for the purpose of inputting sample data into `data.db`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- The dashboard uses [Plotly.js](https://plotly.com/javascript/) for interactive data visualization.



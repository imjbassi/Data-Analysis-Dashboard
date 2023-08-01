# Data Analysis Dashboard

## Overview

This project is a web-based data analysis dashboard that allows users to explore and visualize data using SQL queries. The dashboard is built using Flask, a lightweight Python web framework, and uses SQLite as the backend database for data storage and retrieval. The interactive dashboard provides users with an intuitive interface to view and analyze sample data presented in various chart types, such as bar charts, line charts, or scatter plots.

## Features

- Interactive data visualization with Plotly.js
- SQL database integration for data storage and retrieval
- Sample data for demonstration purposes
- Easy-to-use web interface for data exploration
- Expandable and customizable for further data analysis tasks

## Installation

1. Clone the repository:
git clone https://github.com/imjbassi/data-analysis-dashboard.git
cd sql-data-analysis-dashboard

2. Install the required dependencies:
pip install -r requirements.txt
- Flask
- plotly
- sqlite3

4. Run the application:
python app.py

5. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the dashboard.

## Usage

- The dashboard displays a bar chart by default, visualizing the sample data stored in the SQLite database.
- You can explore the data and interact with the chart using the web interface.


## Sample Data

The SQLite database `data.db` contains sample data for demonstration purposes. The data is stored in the `data` table, which has columns `id`, `name`, and `value`. The dashboard retrieves and visualizes this data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- The dashboard uses [Plotly.js](https://plotly.com/javascript/) for interactive data visualization.



# FastAPI YFinance Backend

This repository provides a backend built with FastAPI and Python 3, integrating the `yfinance` library to fetch historical stock data. The API allows users to retrieve one-year historical stock data for a given ticker symbol.

Deployment Link: [https://stock-history-api.onrender.com](https://stock-history-api.onrender.com)

## Features

- **FastAPI**: High-performance, modern web framework for building APIs.
- **CORS Middleware**: Configured to allow cross-origin requests.
- **YFinance**: Retrieve historical stock market data effortlessly.

## Project Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.9 or later
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/saijayanth59/stock-history-api
   cd stock-history-api
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Starting the Server

Run the FastAPI server using the following command:

```bash
uvicorn main:app --reload
```

The server will start and be accessible at `http://127.0.0.1:8000`.

## API Usage

### Endpoint: `GET /`

Retrieve one-year historical data for a given stock ticker symbol.

#### Query Parameters

- `q` (string): The stock ticker symbol (e.g., `AAPL` for Apple Inc.).

#### Example Request

```bash
curl -X GET "http://127.0.0.1:8000/?q=AAPL"
```

#### Example Response

```json
[
    {
        "Date": "2023-01-01",
        "Open": 145.23,
        "High": 147.30,
        "Low": 144.00,
        "Close": 146.50,
        "Volume": 98765432
    },
    ...
]
```

#### Error Response

```json
{
  "message": "Invalid ticker symbol"
}
```

## Project Structure

```
.
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## Contact

For any questions or suggestions, please open an issue or reach out me.

# Multi-Company Enhanced Stock Analysis Tool

A comprehensive Python tool for analyzing multiple stocks with advanced visualizations, CSV logging, and detailed HTML reporting.

## Features

- **Multi-company analysis** with portfolio overview
- **Advanced visualization dashboard** with 10+ chart types
- **Comprehensive CSV logging** and data export
- **Correlation analysis** across stocks
- **Performance comparison** and ranking
- **Risk-return optimization** analysis
- **HTML report generation** with interactive elements
- **Individual stock detailed charts**
- **Validation testing** for analysis accuracy

## Installation

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn yfinance pathlib warnings datetime logging itertools
```

### Required Files

The tool requires two Python files:
- `API_3y.py` (main analysis engine)
- `html_report_generator.py` (HTML report generator - not included in this file)

## Usage

### Basic Usage

```python
from API_3y import MultiStockAnalyzer

# Define your portfolio
portfolio = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Initialize analyzer
analyzer = MultiStockAnalyzer(portfolio, output_dir="my_analysis")

# Load data
analyzer.load_all_data(period="1y")

# Run analysis
analyzer.analyze_all_stocks()

# Create visualizations
analyzer.create_comprehensive_dashboard()
analyzer.create_individual_stock_charts()

# Generate HTML report
analyzer.generate_comprehensive_report()
```

### Command Line Usage

```bash
python API_3y.py
```

This will analyze a default portfolio of major tech stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX).

## Analysis Components

### 1. Simple Moving Average (SMA) Analysis
- Calculates SMA for 5, 10, 20, and 50-day periods
- Generates BUY/SELL signals based on current price vs SMA
- Tracks trend direction and momentum

### 2. Runs Analysis
- Identifies consecutive upward and downward price movements
- Calculates streak lengths and frequencies
- Provides momentum scoring

### 3. Returns Analysis
- Daily, annualized returns calculation
- Volatility and Sharpe ratio computation
- Win rate and maximum gain/loss tracking

### 4. Profit Analysis
- Buy-and-hold strategy returns
- Optimal trading strategy simulation
- Transaction analysis and profit potential

### 5. Correlation Analysis
- Cross-stock correlation matrix
- Portfolio diversification insights
- Risk assessment across holdings

## Output Files

The tool generates multiple output files in the specified directory:

### CSV Files
- `daily_stock_data.csv` - Combined daily price data
- `sma_analysis.csv` - Moving average analysis results
- `runs_analysis.csv` - Price runs and momentum data
- `returns_analysis.csv` - Return and volatility metrics
- `profit_analysis.csv` - Profit optimization results
- `correlation_matrix.csv` - Stock correlation data
- `portfolio_summary.csv` - Comprehensive portfolio overview
- `validation_results.csv` - Analysis validation test results

### Visualization Files
- `comprehensive_dashboard.png` - Multi-panel dashboard
- `{TICKER}_detailed_analysis.png` - Individual stock charts
- `analysis.log` - Detailed logging information

### Reports
- `comprehensive_report.html` - Interactive HTML report (requires html_report_generator.py)

## Dashboard Components

The comprehensive dashboard includes:

1. **Price Comparison Chart** - All stocks on one timeline
2. **SMA Trading Signals** - Buy/sell signal visualization
3. **Returns Comparison** - Performance bar chart
4. **Risk-Return Scatter Plot** - Volatility vs returns positioning
5. **Runs Analysis** - Upward vs downward momentum
6. **Profit Potential** - Buy-hold vs optimal trading
7. **Correlation Heatmap** - Inter-stock relationships
8. **Volatility Comparison** - Risk assessment
9. **Top Performers Analysis** - Best stock performance
10. **Portfolio Summary** - Key statistics and insights

## Configuration

### Time Periods
```python
# Available periods for yfinance
periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
analyzer.load_all_data(period="1y")  # Default: 1 year
```

### Custom Portfolio
```python
# Define your own stock list
my_portfolio = ['SPY', 'QQQ', 'IWM', 'VTI', 'BND']
analyzer = MultiStockAnalyzer(my_portfolio)
```

### Output Directory
```python
# Specify custom output location
analyzer = MultiStockAnalyzer(portfolio, output_dir="custom_analysis_folder")
```

## Validation and Testing

The tool includes comprehensive validation:

```python
# Run validation tests
analyzer.run_comprehensive_validation()
```

Validation includes:
- SMA calculation accuracy vs pandas
- Data integrity checks
- Analysis consistency verification
- Error handling validation

## Error Handling

- Automatic handling of failed ticker downloads
- Graceful degradation for missing data
- Comprehensive logging of all operations
- Data validation and sanitization

## Performance Metrics

The tool calculates numerous performance metrics:

- **Total Return %** - Overall portfolio performance
- **Annualized Return** - Year-over-year performance projection
- **Volatility** - Risk measurement (standard deviation)
- **Sharpe Ratio** - Risk-adjusted return metric
- **Win Rate** - Percentage of profitable days
- **Maximum Drawdown** - Largest peak-to-trough decline
- **Momentum Score** - Directional trend strength

## Limitations

- Requires active internet connection for data fetching
- Historical data analysis only (not predictive)
- Assumes perfect execution for optimal trading calculations
- Limited to stocks available through yfinance
- Does not account for transaction costs or taxes

## Troubleshooting

### Common Issues

1. **Import Error for html_report_generator**
   - Ensure `html_report_generator.py` exists in the same directory
   - Comment out HTML report generation if file unavailable

2. **yfinance Connection Issues**
   - Check internet connection
   - Verify ticker symbols are correct
   - Some tickers may be delisted or renamed

3. **Insufficient Data**
   - Some stocks may not have enough historical data
   - Tool automatically excludes failed tickers from analysis

4. **Memory Issues with Large Portfolios**
   - Reduce the number of stocks analyzed simultaneously
   - Use shorter time periods for analysis

### Debug Mode

Enable detailed logging by checking the `analysis.log` file in the output directory.

## Example Analysis Output

```
PORTFOLIO SUMMARY STATISTICS
═══════════════════════════════════════════════════════════════

📊 Portfolio Overview:
   • Total Stocks Analyzed: 8
   • Profitable Stocks: 6 (75.0%)
   • Average Return: 12.34%
   • Average Volatility: 28.45%

📈 Best Performer: NVDA (45.67%)
📉 Worst Performer: META (-8.23%)
🎯 Highest Sharpe Ratio: AAPL (1.23)
⚡ Most Volatile: TSLA (45.67%)
```

## Contributing

To extend the tool:
1. Add new analysis methods to the `MultiStockAnalyzer` class
2. Update CSV logging in `_save_analysis_to_csv()`
3. Add corresponding visualization methods
4. Update validation tests

## License

This tool is provided as-is for educational and analysis purposes. Users should verify all calculations independently before making investment decisions.

## Disclaimer

This tool is for educational and informational purposes only. It does not constitute financial advice, and users should consult with financial professionals before making investment decisions. Past performance does not guarantee future results.
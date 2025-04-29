
# 📘 NumPy Learning Path for Algo Traders & Data Scientists

Welcome! This guide is designed to help you learn **NumPy** step-by-step — from absolute basics to intermediate and trading-related applications. It’s written for developers, data scientists, and algo traders who want a structured, purposeful way to master NumPy.

---

## 🛠️ Prerequisites

Before starting, make sure you:

- Have Python installed (preferably 3.8+)
- Are comfortable running Python scripts
- Can create and use virtual environments
- Have a code editor (like VS Code)

---

## 🚀 Setup Instructions

1. **Create a project directory**  
   ```bash
   mkdir numpy_trading_intro && cd numpy_trading_intro
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the environment**
   - Windows: `.env\Scriptsctivate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install NumPy**
   ```bash
   pip install numpy
   ```

5. **Create your first file**
   ```bash
   touch btc_prices.py
   ```

---

## 📚 Learning Roadmap

> Follow these steps in order. Make sure to experiment and code as you go!

### 1. 🔢 NumPy Basics
- What is NumPy and why it's used in trading
- Creating 1D arrays (e.g., price data)
- `dtype`, `.shape`, `.ndim`, `.size`

### 2. 🧩 Array Indexing and Slicing
- Accessing specific elements
- Slicing OHLCV arrays
- Algo trading task: extract the last 3 closing prices

### 3. 🔄 Array Operations
- Vectorized operations (e.g., percentage returns)
- Arithmetic and comparison
- Broadcasting explained

### 4. 📏 Statistical Functions
- `mean()`, `std()`, `min()`, `max()`
- Use case: calculating daily volatility or average close
- Task: find which day had the highest price

### 5. 🏗️ Array Reshaping & Stacking
- `reshape()`, `flatten()`
- Stacking arrays: `hstack()`, `vstack()`
- Use case: combining price and volume arrays

### 6. 🎯 Boolean Indexing & Filtering
- Filtering arrays based on conditions
- Task: find prices above average
- Example: filter trades that meet a signal condition

### 7. 📈 Real Data Simulation (Optional)
- Creating synthetic OHLCV arrays
- Task: calculate log returns using NumPy

### 8. 🧠 Advanced Concepts
- Broadcasting rules deep dive
- `np.where()` for signal generation
- `np.diff()`, `np.cumsum()` — for indicator calculations

---

## ✅ Suggested Practice Projects

- Build a 5-day moving average using NumPy
- Identify trend reversals from price patterns
- Compare NumPy speed vs Python lists in backtesting

---

## 📌 Tips

- Don’t skip coding along
- Always relate concepts to trading logic
- Use comments to document your thought process
- Revisit topics periodically

---

Happy coding and profitable trading! 🧠📊💹

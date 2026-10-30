# SmartBuy AI

A beginner-friendly Python + Streamlit shopping comparison demo.

## Features
- Product search
- Sample price comparison across Amazon, Flipkart and Croma
- Sample 7-day price history chart
- Product pros and cons
- Basic review keyword analysis
- Rule-based shopping assistant

## Important
This project uses sample prices and sample reviews. It does not fetch live prices or real customer reviews. The assistant uses simple Python rules, not a connected AI model.

## Setup

1. Install Python 3.10 or newer.
2. Open Terminal / Command Prompt in this folder.
3. Install packages:

   `pip install -r requirements.txt`

4. Run the website:

   `streamlit run app.py`

5. A browser tab should open. If not, copy the local URL shown in the terminal (usually http://localhost:8501).

## Presentation demo
1. Search for `Samsung`.
2. Select Samsung Galaxy S24.
3. Compare store prices.
4. Show the price history chart.
5. Explain pros and cons.
6. Open customer reviews.
7. Ask the SmartBuy Assistant where the cheapest demo price is.

## How the code works
- `products` is a Python dictionary containing sample product data.
- `st.text_input()` accepts a search term.
- `st.selectbox()` lets the user choose a product.
- `min()` finds the store with the lowest price.
- `pandas` creates the comparison table.
- `st.line_chart()` displays price history.
- `any()` checks review text for positive and negative keywords.
- `st.button()` runs the assistant's recommendation code.

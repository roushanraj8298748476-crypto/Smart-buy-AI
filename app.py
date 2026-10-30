import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# SMARTBUY AI - BEGINNER PYTHON DEMO
# Prices and reviews below are SAMPLE DATA.
# ---------------------------------

st.set_page_config(
    page_title="SmartBuy AI",
    page_icon="🛍️",
    layout="wide"
)

# Sample product database
products = {
    "Samsung Galaxy S24": {
        "category": "Smartphone",
        "prices": {"Amazon": 52999, "Flipkart": 49999, "Croma": 51999},
        "history": [57999, 55999, 54999, 53999, 52999, 51999, 49999],
        "reviews": [
            "Excellent camera and display. Very smooth performance.",
            "Battery life is good and phone feels premium.",
            "Camera is amazing but battery could be better.",
            "Phone is fast, but it gets warm during gaming.",
            "Great display and compact design."
        ],
        "pros": ["Excellent camera", "Bright display", "Fast performance"],
        "cons": ["Battery could be better", "Can warm up during heavy gaming"]
    },
    "iPhone 15": {
        "category": "Smartphone",
        "prices": {"Amazon": 58999, "Flipkart": 57999, "Croma": 59999},
        "history": [69999, 67999, 65999, 63999, 61999, 59999, 57999],
        "reviews": [
            "Camera quality is excellent and video is very stable.",
            "Smooth performance and premium build.",
            "Battery is average for heavy users.",
            "Easy to use but charging speed is slow.",
            "Photos look great in daylight."
        ],
        "pros": ["Excellent video camera", "Smooth performance", "Premium build"],
        "cons": ["Charging is slow", "Battery may be average for heavy users"]
    },
    "OnePlus Nord CE4": {
        "category": "Smartphone",
        "prices": {"Amazon": 24999, "Flipkart": 23999, "Croma": 25499},
        "history": [27999, 26999, 25999, 25999, 24999, 24499, 23999],
        "reviews": [
            "Battery backup is excellent.",
            "Charging is very fast and performance is smooth.",
            "Camera is decent but not the best.",
            "Good value for money.",
            "Phone works well for everyday use."
        ],
        "pros": ["Strong battery", "Fast charging", "Good everyday performance"],
        "cons": ["Camera is average", "Not ideal for demanding photography"]
    },
    "Sony WH-1000XM5": {
        "category": "Headphones",
        "prices": {"Amazon": 24990, "Flipkart": 25990, "Croma": 23990},
        "history": [29990, 28990, 27990, 26990, 25990, 24990, 23990],
        "reviews": [
            "Noise cancellation is excellent.",
            "Very comfortable for long listening sessions.",
            "Sound quality is detailed and clear.",
            "Expensive, but features are useful.",
            "Microphone quality could be better outdoors."
        ],
        "pros": ["Excellent noise cancellation", "Comfortable", "Detailed sound"],
        "cons": ["Expensive", "Microphone can struggle outdoors"]
    },
    "HP 15s Laptop": {
        "category": "Laptop",
        "prices": {"Amazon": 42990, "Flipkart": 41990, "Croma": 43990},
        "history": [46990, 45990, 44990, 44990, 43990, 42990, 41990],
        "reviews": [
            "Good for study and office work.",
            "Keyboard is comfortable.",
            "Battery backup is average.",
            "Works well for browsing and documents.",
            "Not suitable for heavy gaming."
        ],
        "pros": ["Good for students", "Comfortable keyboard", "Useful for office work"],
        "cons": ["Average battery", "Not for heavy gaming"]
    }
}

st.title("🛍️ SmartBuy AI")
st.caption("Search products • Compare prices • Understand reviews • Make smarter choices")
st.info("Student project demo: all prices and customer reviews are sample data, not live store information.")

# Search area
st.subheader("🔎 Find a product")
search_text = st.text_input("Enter product name or category", placeholder="Example: Samsung, iPhone, Laptop")

matching_products = []
for product_name, details in products.items():
    if search_text.lower() in product_name.lower() or search_text.lower() in details["category"].lower():
        matching_products.append(product_name)

if search_text.strip() == "":
    matching_products = list(products.keys())

if matching_products:
    selected_product = st.selectbox("Choose a product", matching_products)
    details = products[selected_product]

    st.divider()
    st.subheader("📦 Product overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Product", selected_product)
    col2.metric("Category", details["category"])
    lowest_store = min(details["prices"], key=details["prices"].get)
    lowest_price = details["prices"][lowest_store]
    col3.metric("Lowest demo price", f"₹{lowest_price:,}", lowest_store)

    # Price comparison
    st.subheader("💰 Compare store prices")
    price_df = pd.DataFrame(
        list(details["prices"].items()),
        columns=["Shopping website", "Price (₹)"]
    ).sort_values("Price (₹)")

    st.dataframe(price_df, use_container_width=True, hide_index=True)
    st.success(f"Best demo deal: {lowest_store} at ₹{lowest_price:,}")

    # Price history chart
    st.subheader("📈 Sample price history")
    history_df = pd.DataFrame({
        "Day": ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"],
        "Price (₹)": details["history"]
    })
    st.line_chart(history_df.set_index("Day"))

    # Pros and cons
    st.subheader("⭐ Product pros and cons")
    pros_col, cons_col = st.columns(2)
    with pros_col:
        st.markdown("**👍 Pros**")
        for item in details["pros"]:
            st.write("•", item)
    with cons_col:
        st.markdown("**👎 Cons**")
        for item in details["cons"]:
            st.write("•", item)

    # Review analysis using simple keyword matching
    st.subheader("📝 Customer review analysis")
    positive_words = ["excellent", "good", "great", "smooth", "amazing", "comfortable", "premium", "fast", "clear", "decent"]
    negative_words = ["bad", "poor", "average", "slow", "expensive", "better", "warm", "struggle", "not"]

    positive_count = 0
    negative_count = 0

    for review in details["reviews"]:
        review_lower = review.lower()
        if any(word in review_lower for word in positive_words):
            positive_count += 1
        if any(word in review_lower for word in negative_words):
            negative_count += 1

    review_col1, review_col2 = st.columns(2)
    review_col1.metric("Positive-signal reviews", positive_count)
    review_col2.metric("Negative-signal reviews", negative_count)

    with st.expander("Read sample customer reviews"):
        for number, review in enumerate(details["reviews"], start=1):
            st.write(f"{number}. {review}")

    # Rule-based AI-style assistant
    st.subheader("🤖 SmartBuy Assistant")
    user_question = st.selectbox(
        "What do you want to know?",
        [
            "Should I buy this product?",
            "What are its main advantages?",
            "What should I be careful about?",
            "Where is the cheapest demo price?"
        ]
    )

    if st.button("Get recommendation"):
        if user_question == "Should I buy this product?":
            st.write(
                f"Based on the sample information, {selected_product} may be worth considering. "
                f"Compare its pros and cons with your needs before buying."
            )
        elif user_question == "What are its main advantages?":
            st.write("Main advantages: " + ", ".join(details["pros"]) + ".")
        elif user_question == "What should I be careful about?":
            st.write("Things to consider: " + ", ".join(details["cons"]) + ".")
        else:
            st.write(f"The lowest sample price is ₹{lowest_price:,} at {lowest_store}.")

else:
    st.warning("No matching product found. Try Samsung, iPhone, OnePlus, Sony, HP, Smartphone, Laptop or Headphones.")

st.divider()
st.caption("SmartBuy AI | Created with Python and Streamlit | Educational demonstration only")

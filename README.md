# Coupon Finder

## Description

The Coupon Finder Web App is a tool that helps users find the best coupons and deals for their online purchases. It utilizes natural language processing (NLP) techniques to search for relevant offers based on user input. This project is built using Python, Flask, and other technologies.

## Hosted Version
You can access a hosted version of the Coupon Finder Web App by visiting the following URL:

Hosted Coupon Finder:  http://pa1vasanth.pythonanywhere.com 

The hosted version allows you to use the app without needing to set it up locally. Simply click the link and start searching for coupons and deals for your online purchases.

## Features

- User-friendly web interface for entering search keywords.
- Search functionality to find coupons and deals based on user input.
- Utilizes NLP techniques for text similarity matching.
- Displays coupon results with their similarity scores.
- Responsive design for both desktop and mobile devices.
- ## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.7+)
- Flask (Python web framework)
- pandas (Data manipulation library)
- numpy (Data manipulation library)
- scikit-learn (Machine learning library)

You can install these dependencies using pip:

```
pip install Flask pandas numpy scikit-learn 
```
## Assumptions

This Coupon Finder web app operates with the following assumptions:

- **Retailer, Brand, and Category Filters**: Coupons are primarily categorized into retailers, brands, and categories. The app assumes that users will enter a keyword that is either a valid retailer, brand, or category. It will then search for coupons relevant to that specific filter.

- **Cosine Similarity Threshold**: For keywords that do not match any specific retailer, brand, or category, the app will perform a broader search. It uses a cosine similarity threshold of 0.3 to determine the relevance of the coupons. Coupons with a cosine similarity score greater than or equal to 0.3 are considered relevant and displayed.

- **Data Availability**: This app assumes that coupon data is available in the provided data sources and is structured in a way that can be processed by the app.

- **User-Friendly Interface**: The web interface is designed to be user-friendly, allowing users to easily search for coupons by entering keywords related to retailers, brands, or categories.

- **Coupon Retrieval**: Coupons are retrieved based on the entered keyword and their similarity to the keyword. The app does not make any direct transactions or interactions with external coupon providers. The displayed coupons are based on the data available in the provided datasets.

Please note that the accuracy and availability of coupons may vary depending on the provided data and the similarity algorithm used.


## Installation

1. Clone the repository:

```
git clone https://github.com/pa1vasanth/CouponFinder.git
```

2.Navigate to the project directory:
```
cd couponFinder
```

3.Run the application:
```
python app.py
```


The web app will be accessible at http://localhost:5000 in your web browser.

Usage

- Open your web browser and go to http://localhost:5000.
- Enter the products you want to buy in the input field.
- Click the "Search Coupons" button to find relevant coupons.
- View the list of coupon results with their similarity scores.

Contributors
- pa1vasanth - Project Developer

Conclusion

The Coupon Finder web app provides a convenient way for users to search for and discover coupons and deals for their online shopping needs. It simplifies the process of finding relevant coupons based on user-entered keywords related to retailers, brands, or categories.

We hope you find this tool helpful in saving money on your online purchases!

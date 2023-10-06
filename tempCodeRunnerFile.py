from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from source import mainCouponer


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/getdata",methods=["GET","POST"])
def getData():
    # print('some get data')
    if request.method == "POST":
        keyword = request.form.get("keyword")
        # print('some test')
        # print(keyword)
        if keyword:
            # Perform the coupon search based on the user's input
            coupon_results = mainCouponer(keyword)
            return render_template("index.html", coupon_results=coupon_results, keyword=keyword,isCouponEmpty=len(coupon_results['Offers'])>0)

    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)

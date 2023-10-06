import pandas as pd
import os

# Get the full path to your web app's root directory
app_root = os.path.abspath(os.path.dirname(__file__))
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Now, you can use `app_root` to construct the absolute paths to your CSV files
categories_path = os.path.join(app_root, "DS_NLP_search_data", "categories.csv")
offer_retail_path = os.path.join(app_root, "DS_NLP_search_data", "offer_retailer.csv")
brand_category_path = os.path.join(app_root, "DS_NLP_search_data", "brand_category.csv")


def preprocess_data():
    categories = pd.read_csv(categories_path)
    offer_retail = pd.read_csv(offer_retail_path)
    brand_category = pd.read_csv(brand_category_path)

    # Vectorization
    tfidf_vect = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
    vectorizer = CountVectorizer()

    vect = tfidf_vect.fit_transform(offer_retail.OFFER)
    vect_df = pd.DataFrame(vect.toarray(), columns=tfidf_vect.get_feature_names_out())

    vect_df = vect_df.drop(columns=['000', '10', '100', '110', '115', '12', '120', '130', '14', '140',
                                    '15', '150', '155', '16', '18', '185', '19', '20', '210', '22',
                                    '220', '25', '250', '270', '275', '28', '30', '300', '35', '40',
                                    '45', '50', '52', '60', '65', '75', '750ml', '80', '90'], )

    # To remove unnecessary words
    column_names_with_1s = []

    # Iterate through each row and find column names where the value is 1
    for index, row in vect_df.iterrows():
        terms_with_1s = vect_df.columns[row != 0]
        s = " ".join(map(str, terms_with_1s.tolist()))
        column_names_with_1s.append(s)

    offer_retail["cleaned"] = column_names_with_1s

    # Joining three tables
    # joining categories and brand category
    result = offer_retail.join(brand_category.set_index('BRAND'), on='BRAND', how='inner')
    result = result.reset_index(drop=True)

    return offer_retail, result, vectorizer

def calculate_similarity(df, keyword, vectorizer):
    ee = []
    rr = []

    for i in range(0, len(df)):
        X = vectorizer.fit_transform([df.cleaned[i], keyword])

        # Get the vectors for each sentence
        vector1 = X.toarray()[0]
        vector2 = X.toarray()[1]

        # Calculate the cosine similarity between the vectors
        cosine_sim = cosine_similarity([vector1], [vector2])

        if round(cosine_sim[0][0], 2) >= 0.3:
            ee.append(df.OFFER[i])
            rr.append(round(cosine_sim[0][0], 2))

    df_result = pd.DataFrame({'Offers': ee, 'Similarity': rr}).drop_duplicates().reset_index(drop=True)
    return df_result

def mainCouponer(keyword):
    offer_retail, result, vectorizer = preprocess_data()

    uniq_retailers = offer_retail.RETAILER.unique()
    uniq_brands = offer_retail.BRAND.unique()
    uniq_category = result.BRAND_BELONGS_TO_CATEGORY.unique()

    if keyword.upper() in uniq_retailers:
        print("retail")
        df_result = calculate_similarity(offer_retail, keyword, vectorizer)

    elif keyword.upper() in uniq_brands:
        print("brand")
        df_result = calculate_similarity(result, keyword, vectorizer)

    elif keyword.lower() in uniq_category:
        print("category")
        df_result = calculate_similarity(result, keyword, vectorizer)

    else:
        print("other")
        df_result = calculate_similarity(offer_retail, keyword, vectorizer)

    return df_result







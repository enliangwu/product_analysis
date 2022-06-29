import requests
from statistics import mean
'''
@author Enliang Wu

Query the following API that returns a randomized list of products in JSON format.
https://www.beautylish.com/rest/interview-product/list

1. Display a list of products including only the brand name, product name, and price. 
2. Filter out any products that are hidden or deleted.
3. Sort by lowest to the highest price. If two items have the same price, sort by name. 
4. If the same product is included twice, only display it once. 
5. Display a summary that includes: a. The total number of unique products b. The total number of unique brands c. The average price
'''


def get_products() -> list:
    # query products form url
    try:
        res = requests.get("https://www.beautylish.com/rest/interview-product/list")
    except:
        print("get products from beautylish failed")
        exit(1)

    # store filter products as key-value of id and product in order to remove duplicated product
    filtered_products = dict()
    res_json = res.json()
    # print(json.dumps(res_json["products"], indent=4))
    for product in res_json.get("products", []):
        # skip deleted product
        if product["deleted"] is True:
            continue

        # skip hidden product
        if product["hidden"] is True:
            continue

        # add product in filtered_products, the product with same id will be replaced
        filtered_products[product["id"]] = product

    # convert dict to list
    filtered_products = list(filtered_products.values())

    # sort the filtered products by price and name
    return sorted(filtered_products, key=lambda p: (float(p["price"].replace("$", "")), p["product_name"]))


def display_products(sorted_products):
    # record unique brands and prices
    brands = set()
    prices = []
    for product in sorted_products:
        brands.add(product["brand_name"])
        prices.append(float(product["price"].replace("$", "")))

    # display the brand name, product name, and price of the products
    print("\n--------LIST OF PRODUCTS--------")
    for product in sorted_products:
        print("Brand Name: {:24s}, Product Name: {:24s}, Price: {:20s}"
              .format(product["brand_name"], product["product_name"], product["price"]))

    # display a summary
    print("\n--------SUMMARY:----------")
    print(f"The total number of unique products is {len(sorted_products)}")
    print(f"The total number of unique brands is {len(brands)}")
    print(f"The average price is ${round(mean(prices), 2)}")


if __name__ == "__main__":
    # get products
    sorted_products_ = get_products()

    # display the products and the summary
    display_products(sorted_products_)

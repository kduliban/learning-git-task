lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywaniak": ["marchew", "seler", "rukola"]
}
x = 0
for shop, products in lista_zakupow.items():
    shop = shop.title ()
    products_titled = []
    for product in products:
        products_titled.append (product.title())
        x = x + 1
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products_titled}.")
print (f"W sumie kupuję {x} produktów")
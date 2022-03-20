lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywaniak": ["marchew", "seler", "rukola"]
}
for shop, products in lista_zakupow.items():
    shop = shop.title ()
    products_titled = []
    for product in products:
        products_titled.append (product.title())
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products_titled}.")
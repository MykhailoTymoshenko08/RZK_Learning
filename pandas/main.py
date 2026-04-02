import pandas as pd

r1 = pd.DataFrame({'Yes': [50, 21], 
                   'No': [131, 2]})
r2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
                   'Sue': ['Pretty good.', 'Bland.']})

print(r1)
print(r2)

r3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(r3)


wine_reviews = pd.read_csv("./read.csv")

wine_reviews.shape # size

print(wine_reviews.shape)
print(wine_reviews)
print(wine_reviews.head()) # onlu first five rows
wine_reviews = pd.read_csv("./read.csv", index_col=0)
print('='*20)
print(wine_reviews)



pd.DataFrame([[30,21]], columns = ['Apples', 'Bananas'])
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
pd.DataFrame({'Bob': ['I l', 'It.'], 'Sue': ['Pd.', 'Bld.']}, index=['Pr A', 'Pr B'])

fruit_sales = pd.DataFrame(
    {
        'Apples': [35,41],
        'Bananas': [21,34]
    },
    columns = ['Apples', 'Bananas'],
    index = ['2017 Sales', '2018 Sales']
)


quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']

ingredients = pd.Series(quantities, index=items, name='Dinner')

ingredients.to_csv("cows_and_goats.csv") # to saev to csv

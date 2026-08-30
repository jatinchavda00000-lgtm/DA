import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')

# Task 1
flipkart_df = pd.read_csv('flipkart_products.csv')
sns.jointplot(x='rating', y='price', data=flipkart_df, kind='scatter', height=7)
plt.suptitle('Flipkart Products: Rating vs Price', y=1.02)
plt.show()

# Task 2
swiggy_df = pd.read_csv('swiggy_orders.csv')
sns.jointplot(x='delivery_time', y='order_value', data=swiggy_df, kind='hex', height=7)
plt.suptitle('Swiggy Orders: Delivery Time vs Order Value', y=1.02)
plt.show()

# Task 3
instagram_df = pd.read_csv('instagram_posts.csv')
sns.jointplot(x='likes', y='comments', data=instagram_df, kind='kde', fill=True, height=7)
plt.suptitle('Instagram Posts: Likes vs Comments', y=1.02)
plt.show()

# Task 4
zomato_df = pd.read_csv('zomato_reviews.csv')
for kind in ['scatter', 'hex', 'kde']:
    kwargs = {'fill': True} if kind == 'kde' else {}
    sns.jointplot(x='rating', y='number_of_reviews', data=zomato_df, kind=kind, height=7, **kwargs)
    plt.suptitle(f'Zomato Reviews — {kind.title()}', y=1.02)
    plt.show()
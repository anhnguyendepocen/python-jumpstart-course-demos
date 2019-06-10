import pandas as pd


def main():
    print_header()
    df = load_data('SacramentoRealEstateTransactions2008.csv')
    most_extreme_home(df, extreme='max')
    most_extreme_home(df, extreme='min')
    average_house(df, beds=None)
    average_house(df, beds=2)


def print_header():
    print('------------------------')
    print('    REAL ESTATE APP')
    print('------------------------')
    print()


def load_data(csv_file):
    print('Loading real estate data...')
    df = pd.read_csv(csv_file)
    print()
    return df


def most_extreme_home(df, extreme = 'max'):
    if extreme == 'max':
        most_extreme = df['price'] == df['price'].max()
        descriptor = 'Most expensive'
    else:
        most_extreme =  df['price'] == df['price'].min()
        descriptor = 'Least expensive'

    home = df[most_extreme].reset_index()
    beds = int(home['beds'])
    baths = int(home['baths'])
    price = int(home['price'])
    city = home.loc[0, 'city'].title()
    state = home.loc[0, 'state']

    print('{} house: {}-bed, {}-bath, house for ${:,} in {}, {}'.format(descriptor, beds, baths, price, city, state))


def average_house(df, beds=None):
    cols = ['price', 'beds', 'baths']
    rows = df.index.values
    label = 'Average house'

    if beds:
        rows = df['beds'] == beds
        label = 'Average {}-bedroom house'.format(beds)

    averages = df.loc[rows, cols].agg('mean')
    print('{}: ${:,}, {}-bed, {}-bath'.format(
        label,
        averages['price'].round(0).astype('int'),
        averages['beds'].round(1),
        averages['baths'].round(1)))


if __name__ == '__main__':
    main()
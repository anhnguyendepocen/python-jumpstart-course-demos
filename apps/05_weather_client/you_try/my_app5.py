import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    header()
    zipcode = get_zipcode_from_user()
    html = get_html_from_web(zipcode)
    components = get_weather_from_html(html)
    display_forcast(components)


def header():
    print('----------------------------')
    print('        WEATHER APP')
    print('----------------------------')
    print()


def get_zipcode_from_user():
    user_zip = input('What zipcode do you want the weather for? ')
    user_zip = user_zip.lower().strip()
    return user_zip


def get_html_from_web(user_zip):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(user_zip)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, features="html.parser")
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-value wu-value-to').get_text()
    scale = soup.find(class_='wu-label').get_text()

    loc = clean_up_text(loc)
    condition = clean_up_text(condition).lower()
    temp = clean_up_text(temp)
    scale = clean_up_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def clean_up_text(text: str):
    return text.strip()


def display_forcast(components):
    print("The temperature for {} is {}°{} and {}.".format(
        components.loc,
        components.temp,
        components.scale,
        components.cond
    ))


if __name__ == '__main__':
    main()

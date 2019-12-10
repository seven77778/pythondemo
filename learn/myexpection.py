import requests
from requests import ReadTimeout, ConnectTimeout


def get_page(url):
    try:
        response = requests.get(url, timeout=(0.1,0.1))
        if response.status_code == 200:
            return response.text
        else:
            print('Get Page Failed', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        print('ConnectTimeout', url)
        return None
    finally:
        print("this is finally")
        # return "ok!!"


def main():
    url = 'https://www.google.com'
    print(get_page(url))


if __name__ == '__main__':
    main()
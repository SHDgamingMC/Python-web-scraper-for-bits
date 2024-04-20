import requests
from bs4 import BeautifulSoup

def get_hotel_data(city, budget, sort_by):
    url = f'https://example.com/hotels/{city}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    hotels = []
    for hotel in soup.find_all('div', class_='hotel'):
        name = hotel.find('h2').text.strip()
        price = int(hotel.find('span', class_='price').text.strip().replace('$', '').replace(',', ''))
        rating = float(hotel.find('span', class_='rating').text.strip())
        hotels.append({'name': name, 'price': price, 'rating': rating})
    
    # Filter hotels by budget
    filtered_hotels = [hotel for hotel in hotels if hotel['price'] <= budget]
    
    # Sort hotels
    if sort_by == 'price':
        filtered_hotels.sort(key=lambda x: x['price'])
    elif sort_by == 'rating':
        filtered_hotels.sort(key=lambda x: x['rating'], reverse=True)
    
    return filtered_hotels[:5]

def main():
    city = input("Enter the city you want to visit: ")
    budget = int(input("Enter your budget per night (in USD): "))
    sort_by = input("Sort by price or rating (type 'price' or 'rating'): ").lower()
    
    while sort_by not in ['price', 'rating']:
        print("Invalid input! Please enter 'price' or 'rating'.")
        sort_by = input("Sort by price or rating (type 'price' or 'rating'): ").lower()
    
    hotels = get_hotel_data(city, budget, sort_by)
    
    if hotels:
        print(f"\nHere are 5 hotels in {city} within your budget, sorted by {sort_by}:")
        for idx, hotel in enumerate(hotels, start=1):
            print(f"{idx}. {hotel['name']} - Price: ${hotel['price']}, Rating: {hotel['rating']}")
    else:
        print("Sorry, no hotels found within your budget in this city.")

if __name__ == "__main__":
    main()

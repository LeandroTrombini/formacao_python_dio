import phonenumbers 
from phonenumbers import geocoder

phone = input('enter the phone in the format +553298587457: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
import phonenumbers
from phonenumbers import geocoder 
phone_number1= phonenumbers.parase("+917294536271")
phone_number2= phonenumbers.parase("+918878586271")
phone_number3= phonenumbers.parase("+12136574429")
phone_number4= phonenumbers.parase("+201234567898")

print("\nphone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))

import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
response = requests.get(url)
data = response.json()

znach = {item["cc"]: item["rate"] for item in data}
print(znach)

while True:
    
    suma = float(input("Введіть суму: "))
    val= input("Введіть валюту для конвертації : ").upper()

    if val not in znach:
        print("Валюту не знайдено")
    else: 
        pereved = suma * znach[val]
        print(f"{suma} {val} = {pereved} UAH")
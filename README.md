# Moneyfarm to Financedrip Portfolio Export
Export Moneyfarm Portfolio to Financedrip standard format

If you like this project you can support me with :coffee: or simply put a :star: to this repository :blush:
[![buy me a coffee](https://img.shields.io/badge/support-buymeacoffee-222222.svg?style=flat-square)](https://www.buymeacoffee.com/lorenzodeluca)

## Installation

Clone this repository and install dependency
```python
pip install -r requirements.txt 
```
## Usage

### Export Data from Moneyfarm
1. Login on your Moneyfarm account
2. Go into **Documents** 
3. Download latest **Rendiconto Gestione Patrimoniale** 
![Download MF](images/download-rendiconto.png)
4. Copy downloaded file into project folder
5. Run **main.py**, automatically takes the first pdf file in the folder, if you want to specify it put it after main.py
  ```python
python main.py Rendiconto+Gestione+Patrimoniale+3+trimestre+2023.pdf
```
6. If there were no errors, you should find the csv file with the name 'export_for_financedrip.csv'
![Exporting MF](images/exporting.png)

### Import data to Financedrip
1. Login on your Financedrip account
2. Create a Portfolio if you haven't yet
3. Click on **Importa** 
![Import Financedrip](images/financedrip-Importa.png)

4. Select CSV File 'export_for_financedrip.csv' with **Personalizzato** Broker
5. Wait a few seconds and you should have all transactions imported :blush:
![Imported Financedrip](images/imported.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
GNU AGPLv3 © [Lorenzo De Luca][https://lorenzodeluca.dev]
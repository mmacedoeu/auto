from board_setup_extractor import BoardSetupExtractor
import csv

with open('board.csv', newline='', encoding='utf-8') as csvFile:
    reader = csv.DictReader(csvFile, delimiter = ';', dialect="excel")
    for row in reader:
        try:
            BoardSetupExtractor().extract(row['IP'], 'pi', row['Senha'])
        except Exception as ex:
            print(f'[Device {row["IP"]}] - Error while extracting device configuration: {ex}')
        
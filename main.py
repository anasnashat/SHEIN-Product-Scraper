import save_data
import scrap_data

FILE_NAME = input('Enter the file name you need to save data in :  ')

if __name__ == '__main__':
    product = scrap_data.fetch_data()
    save_data.save(FILE_NAME, product)

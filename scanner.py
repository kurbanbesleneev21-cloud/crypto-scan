import ccxt
import json
import time

def fetch_crypto_data():
    # Инициализируем биржи
    # Мы используем публичные методы, поэтому ключи API пока не нужны
    exchanges = {
        'binance': ccxt.binance(),
        'bybit': ccxt.bybit()
    }
    
    symbol = 'BTC/USDT'
    data_to_save = {}

    print(f"Начинаю сбор данных для {symbol}...")

    for name, exchange in exchanges.items():
        try:
            # Запрашиваем цену
            ticker = exchange.fetch_ticker(symbol)
            data_to_save[name] = ticker['last']
            print(f"Цена на {name}: {ticker['last']}")
        except Exception as e:
            print(f"Ошибка при работе с {name}: {e}")
            # Если биржа не ответила, поставим 0, чтобы сайт не сломался
            data_to_save[name] = 0

    # Сохраняем результат в файл data.json
    with open('data.json', 'w') as f:
        json.dump(data_to_save, f)
    
    print("Данные успешно сохранены в data.json")

if __name__ == "__main__":
    fetch_crypto_data()

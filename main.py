import openai
import json
from base64 import b64decode

# запрос у пользователя ввести текстом ожидаемое изображение
prompt = input("The pompt: ")

# Подключить ключ API
openai.api_key = "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"

# Генерация изображения ИИ с передачей данный в кодировке base64_json
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256',
    response_format='b64_json'
)

# записить данных сгенерированых ИИ в файл json
with open('data_json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)
    
# декодируем данные сгенерируемые ИИ в b64_json
image_data = b64decode(response['data'][0]['b64_json'])

#  создаем имя файла = запросу пользователя с разделителем "_"
file_name = '_'.join(prompt.split(' '))

#сохраняем сгененрированные данные как изображение
with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)




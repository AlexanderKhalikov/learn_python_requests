import requests
import os

# Create images directory

directory_name = 'images'
os.mkdir(directory_name)

print(f"Directory {directory_name} created")

response = requests.get('https://www.adobe.com/express/feature/image/convert/jpg-to-png/media_1b0ad89a4a5ad233f5708e21b5998d6638cb07929.png?width=2000&format=webply&optimize=medium')

with open(f'{directory_name}/image.png', 'wb') as f:
    f.write(response.content)

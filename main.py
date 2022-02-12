#!/usr/bin/env python3
import requests

# token = '5230930889:AAGEc5mBMx217ZVU9Ig7ckeEWBt0KVV8FNY'
# chat_ident = '@clase_clase_exito'
# texto = 'Hola mundo cruel!'

# requests.post('https://api.telegram.org/bot'+'token'+'/sendMessage',
#               data={'chat_id': chat_ident, 'text': texto})

#!/usr/bin/env python3
import requests

texto = 'Meto un ciclo for para enviar varios mensajes a la vez'

requests.post('https://api.telegram.org/bot5230930889:AAGEc5mBMx217ZVU9Ig7ckeEWBt0KVV8FNY/sendMessage',
              data={'chat_id': '@clase_clase_exito', 'text': texto})



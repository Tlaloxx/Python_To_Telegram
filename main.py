#!/usr/bin/env python3
import requests

# token = '************************************************'
# chat_ident = '@clase_clase_exito'
# texto = 'Hola mundo cruel!'

# requests.post('https://api.telegram.org/bot'+'token'+'/sendMessage' , data={'chat_id': chat_ident, 'text': texto})


import requests

texto = 'Meto un ciclo for para enviar varios mensajes a la vez'

requests.post('https://api.telegram.org/bot************************************************/sendMessage',
              data={'chat_id': '@clase_clase_exito', 'text': texto})



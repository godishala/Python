#!/usr/bin/env python3

import openai,sys

query = sys.argv[1]

openai.api_key ="<Api-Key-Here>"

response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Open AI chatbot"},
            {"role": "user", "content": query },
            ]
)

result= ''
for choice in response.choices:
    result += choice.message.content

print(result)

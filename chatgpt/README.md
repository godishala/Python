Python script to query Chatgpt


Installing required packages:
```bash
$ mkdir -p openai/chatgpt
$ virtualenv openai/chatgpt
$ source openai/chatgpt/bin/activate
$ pip3 install -U pip
$ pip3 install openai
$ cd openai/chatgpt
$ wget https://raw.githubusercontent.com/godishala/Python/master/chatgpt/chatbot.py
```

Usage:
```bash
python3 chatbot.py "<query-here>"
eg: python3 chatbot.py "write socket program in python" 
```


POC:
![chatbotone](https://github.com/godishala/Python/blob/master/chatgpt/Images/chatgptone.png)
![chatbottwo](https://github.com/godishala/Python/blob/master/chatgpt/Images/chatgpttwo.png)

Note: Don't forgot to add the `api-key` in script.

import openai
from dotenv import dotenv_values

config = dotenv_values('.env')
openai.api_key = config["OPENAI_API_KEY"]


messages = [] # holds all messages for persistent chat
while True:
    try:
        user_input = input("You: ") # get user input
        # append user input to messages list
        messages.append({"role": "user", "content": user_input})

        # generate response to user's input message
        # ChatCompletion requires model and messages
        res = openai.ChatCompletion.create(
            model = 'gpt-4',
            messages = messages
        )
        # append ai response to messages list
        messages.append(res['choices'][0]['message'].to_dict())
        # display ai response
        print("ASSISTANT: ", res['choices'][0]['message']['content'])

    except KeyboardInterrupt:
        print('Exiting...')
        break
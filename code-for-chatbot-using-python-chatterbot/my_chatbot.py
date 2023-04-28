# Importing necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating a chatbot instance
chatbot = ChatBot('MyChatBot')

# Creating a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Training the chatbot which is based on the english corpus
trainer.train('chatterbot.corpus.english')

# Starting the chatbot
print('Type "quit" to exit')
while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        break
    else:
        bot_response = chatbot.get_response(user_input)
        print('Bot:', bot_response)

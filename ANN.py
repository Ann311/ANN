#import Packages
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot=ChatBot('ANN')
#import Chatbot to train
bot.set_trainer(ChatterBotCorpusTrainer)
#training the data
bot.train('chatterbot.corpus.english')
#creating interaction of Chatbot
while(True):
    mes=input('You:')
    if(mes=='Bye' or mes=='bye'):
        print('{}:Bye,see you soon'.format(bot.name))
        break
    if(mes!='Bye' or mes!='bye'):
        print('{}:{}'.format(bot.name,bot.get_response(mes)))
        
    
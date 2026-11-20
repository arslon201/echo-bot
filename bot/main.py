from bot.settings import settings
from bot.updater import Updater
from bot.handlers import TextHandler, PhotoHandler, ContactHandler, LocatioinHandler, DocumentHandler, VoiceHandler, VideoHandler


def reply_text(update: dict):
    print("text keldi")


def reply_photo(update: dict):
    print("photo keldi")


def reply_contact(update: dict):
    print("contact keldi")


def reply_location(update: dict):
    print("lcoation keldi")
    
    
def reply_document(update: dict):
    print("document keldi")
    
    

def reply_voice(update: dict):
    print("voice keldi")
    
    
def reply_video(update: dict):
    print("video keldi")



def main() -> None:
    updater = Updater(settings.token)

    updater.dispatcher.add_handler(TextHandler(reply_text))
    updater.dispatcher.add_handler(PhotoHandler(reply_photo))
    updater.dispatcher.add_handler(ContactHandler(reply_contact))
    updater.dispatcher.add_handler(LocatioinHandler(reply_location))
    updater.dispatcher.add_handler(DocumentHandler(reply_document))
    updater.dispatcher.add_handler(VoiceHandler(reply_voice))
    updater.dispatcher.add_handler(VideoHandler(reply_video))
    updater.start_polling() 

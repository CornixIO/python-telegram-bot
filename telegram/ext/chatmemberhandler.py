from telegram.ext import Handler


# Define a custom handler for my_chat_member updates
class MyChatMemberHandler(Handler):
    def __init__(self, callback):
        # Call the parent constructor and pass the callback function
        super().__init__(callback)

    # Check if the update is a my_chat_member update
    def check_update(self, update):
        return update.my_chat_member is not None

    # Handle the my_chat_member update if it matches
    def handle_update(self, update, dispatcher):
        return self.callback(dispatcher.bot, update)
        # return self.callback(update, dispatcher) # Delete if the above line is working

from telegram.ext import Handler


# Custom handler class that overrides the check_update method
class MyChatMemberHandler(Handler):
    def check_update(self, update):
        # We are only interested in my_chat_member updates
        return update.my_chat_member is not None

    def handle_update(self, update, dispatcher):
        my_chat_member = update.my_chat_member

        # Check if the bot's membership status has changed
        if my_chat_member.new_chat_member.user.id == dispatcher.bot.id:
            # If the bot has become an administrator in a channel
            if my_chat_member.new_chat_member.status == "administrator":
                chat_id = my_chat_member.chat.id
                chat_title = my_chat_member.chat.title
                print(f"Bot added to channel: {chat_title} (ID: {chat_id})")

                # Optionally send a message to the channel
                dispatcher.bot.send_message(chat_id, "Hello! I've been added to this channel.")

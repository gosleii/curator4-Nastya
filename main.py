import telebot

bot = telebot.TeleBot("6793066097:AAHpIVFgHT58WRCBbgUQTuddhkcKT9ZTg4E")


@bot.message_handler(comands=["start"])
def main(messange):
    bot.send_messange(messange.chat.id, "выбери команду")


@bot.message_handler(comands=["information about Pushkin"])
def main(messange):
    bot.send_messange(messange.chat.id,
                      "_прочитай информацию про  А.С.Пушкина_/nАлександр Сергеевич Пушкин (1799-1837 гг.) –         великий  русский поэт, прозаик, драматург. Автор бессмертных произведений в стихах и прозе: романов *Евгений Онегин*,           *Дубровский*,  известных поэм *Руслан и Людмила*, *Кавказский пленник*, повести *Пиковая дама* и многих других, а               также  сказок для детей.")


@bot.message_handler(comands=["information about Gogol"])
def main(messange):
    bot.send_messange(messange.chat.id,
                      "_прочитай информацию о Н.В.Гоголе_/nНиколай Васильевич Гоголь (1809 – 1852) – классик           русской литературы, писатель, драматург, публицист, критик. Самыми известными произведениями Гоголя можно назвать               сборник *Вечера на хуторе близ Диканьки*, посвященный обычаям и традициям украинского народа, а также величайшую поэму         *Мертвые    души*")


@bot.message_handler(comands=["information about Dostoevsky "])
def main(messange):
    bot.send_messange(messange.chat.id,
                      "_прочитай информацию о Ф.М.Достоевском_/nФёдор Михайлович Достоевский (1821–1881 гг.) –    величайший писатель, классик русской литературы, мыслитель. Автор таких бессмертных произведений, как *Идиот*, *Преступление    и наказание*, *Униженные и оскорблённые*, *Братья Карамазовы* и многих других.")


bot.infinity_polling()


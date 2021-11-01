import logging
import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.conversationhandler import ConversationHandler
from telegram.ext.updater import Updater
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup

from sender import collection_1, send_collection_all, comment_save, coment_show  


# Configuracion del loogin
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Estados de la conversacion
GETOPTION, GETCOMMENTS, GETSUBMENU = range(3)

# Teclado Principal
reply_keyboard = [
    ['💎Nuestras Colecciones💎'],
    ['Redes 💻📱📸', 'Quiénes somos❓'],
    ['Por qué #pendientes_a_lo_cubano❓🤔'],
    ['Comentar ✍️✍️'],
    ['Quiero un BOT así😍']
]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

# Respuestas a los botones
btn_1 = '^💎Nuestras Colecciones💎$'
btn_2 = '^Redes 💻📱📸$'
btn_3 = '^Quiénes somos❓$'
btn_4 = '^Por qué #pendientes_a_lo_cubano❓🤔$'
btn_5 = '^Comentar ✍️✍️$'
btn_6 = '^Quiero un BOT así😍$'

# Teclado de Colecciones
colection_keyboard = [
    ['Raíces Hispanas💃🏻♥️💛'],
    ['Raíces Africanas👸🥁🌈'],
    ['Paisajes Insulares🌊🏔🏛🏕'],
    ['Ajiaco🌽🐷🥘🥣'],
    ['Volver al menú↩️']
]
markup_colection = ReplyKeyboardMarkup(colection_keyboard, resize_keyboard=True)

# Funciones para los manejadores
def start(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} ha iniciado en el bot.')
    
    update.message.reply_text(
        text=f'Hola {update.effective_user.first_name} bienvenid@ a Ínsula \nPendientes a lo cubano \nEs un placer atenderte. \nInteractúa con nuestro bot para que conozcas mas detalles de nuestros productos y servicios. \nGracias por preferirnos 😉',
        reply_markup=markup
    )
    return GETOPTION

def colection(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} esta en el Submenu de Coleccioes.')
    
    update.message.reply_text(
        text='💎Nuestras Colecciones💎',
        reply_markup=markup_colection
    )
    return GETSUBMENU

def redes(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} esta viendo info de redes Insula.')
    
    update.message.reply_text(
                text="""La mejor modelo de 💎Ínsula eres tú.
Escoge👇🏻, encarga🛍 y luce🤩 tus #pendientes_a_lo_cubano
https://wa.me/c/5358037785

Síguenos y apoya nuestro proyecto por acá 👇🏻
https://www.instagram.com/insula_pendientes_a_lo_cubano/

Estamos en telegram😉👇🏻
@pendientesAloCubano
https://t.me/pendientesAloCubano

Siguenos en Facebook😉👇🏻
https://www.facebook.com/Ínsula-Pendientes-a-lo-cubano-101855228956424
            """
    )
    return GETOPTION


def who_are(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} quiere conocer mas de Isula.')
    
    update.message.chat.send_photo(
        photo=open('./img/logo.jpg', 'rb'), 
        caption="💎Ínsula es un pequeño emprendimiento dedicado a la confección de aretes de cerámica fría. \n💎Todo el proceso es manufacturado y diseñado sobre la base de elementos identitarios de la cubanía❤️💙🤍. \n💎Ínsula es una apuesta por resaltar lo cubano, lo típico, lo nuestro. "
    )
    return GETOPTION

def what_pc(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} quiere conocer Pendientes a lo cubano.')
    
    update.message.reply_text(
        text='Por qué #pendientes_a_lo_cubano?🤔\nEn nuestro eslogan hay un pequeño juego de doble sentido💡: \n✅En primer lugar nos referimos a los aretes con un sello nacional💎: "pendientes a lo cubano".\n✅Al mismo tiempo estamos "atentos" (pendientes) a lo singular, a lo típico, a lo cubano🇨🇺.'
    )
    return GETOPTION

def to_comment(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} comenta.')
    
    update.message.reply_text(
        text='Por favor, deje su comentario sobre nuestro emprendimiento. Es muy importante para nosotros saber que piensas. 😉😉😉👇🏻👇🏻👇🏻'
    )
    return GETCOMMENTS 

def save_comment(update: Update, context: CallbackContext):
    user_name = update.effective_user.full_name
    date = update.message.date.date()
    comment = update.message.text
    context.bot.sendMessage(
        chat_id=1088981095,
        text=f'Comentario: \nUsuario: {user_name}\nFecha: {date} \nComentario: \n{comment}',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Mostrar Todos los Comentarios',callback_data='show')]
            ])
    )
    save_text = f'Usuario: {user_name}, Fecha: {date}, Comentario: {comment}' 
    comment_save(save_text)
    return GETOPTION

def show_all(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer('Ok')
    comments = '\n'.join(coment_show())
    
    query.edit_message_text(
        text=f"""
Todos los comentarios:
{comments}
        """
    )
    return GETOPTION

def send_collection(update: Update, context: CallbackContext):
    name_coll = update.message.text # -> Tomo el nombre de la colleccion q elije el usuario
    print(name_coll)
    send_collection_all(update, context, name_coll) 
    return GETSUBMENU

def spam(update: Update, context: CallbackContext):
    usuario = update.effective_user.full_name
    logger.info(f'Usuario: {usuario} quiere contratar tu servicio.')
    
    update.message.reply_text(
        text='Puede tener un BOT 🤖 como este para automatizar su negocio, haciéndolo mas próspero.\nPuede perzonalizarlo a su gusto, atendiendo a sus necesidades, solo tiene que contactar con el desarrollador. 👇🏻👇🏻👇🏻 ',
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Contactatenos 🤓', url='https://t.me/CarlosSalgado')]])
    )
    return GETOPTION
def fallback(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Disculpa! No puedo entenderte.'
    )
def main():
    # TOKEN
    TOKEN = os.getenv('TOKEN')
    
    # Updater
    updater = Updater(TOKEN)
    
    # Dispatcher
    dispatcher = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points= [CommandHandler('start', start)],
        states={
            GETOPTION: [
                MessageHandler(Filters.regex(btn_1), colection),
                MessageHandler(Filters.regex(btn_2), redes),
                MessageHandler(Filters.regex(btn_3), who_are),
                MessageHandler(Filters.regex(btn_4), what_pc),
                MessageHandler(Filters.regex(btn_5), to_comment),
                MessageHandler(Filters.regex(btn_6), spam)
            ],
            GETSUBMENU:[ 
                MessageHandler(Filters.regex('^Volver al menú↩️$'), start),
                MessageHandler(Filters.regex('^Raíces Hispanas💃🏻♥️💛$'), send_collection),
                MessageHandler(Filters.regex('^Raíces Africanas👸🥁🌈$'), send_collection),
                MessageHandler(Filters.regex('^Paisajes Insulares🌊🏔🏛🏕$'), send_collection),
                MessageHandler(Filters.regex('^Ajiaco🌽🐷🥘🥣$'), send_collection),
                ],
            GETCOMMENTS: [ MessageHandler(Filters.text, save_comment)]
        },
        fallbacks=[MessageHandler(Filters.all, fallback)]
    )
    # Agregar la conversacion
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CallbackQueryHandler(pattern='show', callback=show_all))
    
    # START BOT
    PORT = int(os.environ.get("PORT","8443"))
    updater.start_webhook(listen='0.0.0.0', 
                          port=PORT, 
                          url_path=TOKEN, 
                          webhook_url=f'https://insula-bot.herokuapp.com/'+TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
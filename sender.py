from telegram import Update, InlineKeyboardButton, keyboardbutton
from telegram.ext.callbackcontext import CallbackContext
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup

# Infografias de cada coleccion
collection_1 = ['La Colección Raíces Hispanas representa la herencia de nuestro "abuelo blanco"💛❤️🇪🇦Olé👏🏻! El poeta nacional Nicolás Guillén✒️🇨🇺 se refirió así a nuestros ancestros españoles en su Balada de los Dos Abuelos', 'Conoces nuestras Castañuelas??🤔🤔 Las protagonistas de los tablaos👏🏻👏🏻. Compañía por excelencia de cantaores🎤 y bailaores💃 Luce Hispanidad🇪🇸 Luces Castañuelas💛❤️', 'Conoces nuestros Abanicos🤔🤔 Códigos de romance😍 y coqueteo😏 Traen brisas de galanteo😉 y baile💃 Luce enigmática y sedutora💫 Luce Abanicos💛❤️','Conoces nuestros Colores Hispanos??🤔🤔 Binomio identitario de los peninsulares: Amarillo💛 y Rojo❤️ Marca la herencia de nuestro "abuelo blanco"👴🏻(al decir de Guillén✒️) Luce Colores Hispanos🇪🇦Olé', 'Conoces nuestras Batas Sevillanas??🤔🤔 Bailan al ritmo de las palmas 💃👏🏻👏🏻 Llenan de lunares y colores las ferias sevillanas 🎉🎉 Luce la elegancia andaluza😌 Luce Batas Sevillanas💛❤️','Conoces nuestras Batas Sevillanas??🤔🤔 Bailan al ritmo de las palmas 💃👏🏻👏🏻 Llenan de lunares y colores las ferias sevillanas 🎉🎉 Luce la elegancia andaluza😌 Luce Batas Sevillanas💛❤️']
collection_2 = ['La Colección Raíces Africanas representa la herencia de "nuestro abuelo negro". Ashé 😉','Ínsula 🏝: Conoces nuestro Mestizaje??🤔🤔 ¿Qué somos los cubanos sino una mezcla única y hermosa de muchas raíces?🌈  Somos una Isla mestiza, múltiple, diversa🏝🎨♥️ Luce Cubanía🇨🇺 Luce Mestizaje', 'Conoces nuestros Tambores??🤔🤔 A su toque baila nuestra identidad 🥁💫 Se acompañan de risas😄, de palmas👏🏻, de canto🎤🎶 La sensualidad cubana se resume en su sonido😏😉🥁🎶 Luce nuestro Folclore ♥️💙 Luce Tambores', 'Conoces nuestros Oshún??🤔🤔 La reina de la feminidad👸 y el romance♥️ Patrona nuestra💫🙇🏼♀️ Con esencia de miel🍯 y girasoles🌻 Luce sensualidad ancestral 💛💄👑 Luce Oshún', 'Conoces nuestros Yemayá??🤔🤔 La reina de las aguas 👸💙y los mares🌊🐚 Símbolo de maternidad🤰 y amor💖 Luce serenidad☺️ y paz🧘♀️ Luce Yemayá']
collection_3 = ['La Colección Paisajes Insulares recrea lugares representativos de nuestra geografía. Viaja con ella 😉','Ínsula 🏝: Conoces nuestro Viñales??🤔🤔 Paraíso natural único 💚✨ Combinación perfecta de ríos🌊 , valles 🏕, mogotes ⛰y cuevas🏔 Luce Exótica 😉🤩 Luce Viñales','Conoces nuestro Varadero??🤔🤔 La mejor playa del Caribe 🏖🥇 Baño de aguas azules 🌊 espuma blanca y arena fina💎 Luce Tropical👒⛱   Luce Varadero','Conoces nuestra Habana??🤔🤔 La ciudad de las columnas🏛  Novia de la bahía ❤🌊 Mezcla de tradición🧓 y modernidad 😎 Luce Bohemia🥰 Luce La Habana', 'Conoces nuestro Turquino??🤔🤔 El punto más elevado de nuestra geografía⛰ Ícono de cubanía🇨🇺😌 Luce aventura 🚵🏼♀️ e Identidad❤💙 Luce Turquino⛰💫']
collection_4 = ['Ajiaco Ínsula 🏝: La colección Ajiaco es la expresión de la cubanía hecha al plato','Conoces nuestro Cerdo Asado??🤔🤔 El rey de nuestras mesas🥩🐷💙♥️ Protagonista del fin de año🎊🗓⏳ Luce singular💫🤩 Luce Cerdo Asado', 'Conoces nuestra Caldosa??🤔🤔 Sabor y aroma de las fiestas cubanas😋🥘♥️💙 Mezcla perfecta de ingredientes y condimentos 🌽🌶🥔🍗🍖🥩🥓 El más cubano de los caldos 😌🥘 Luce festiva🎊 Luce Caldosa', 'Conoces nuestros Tamalitos de Olga??🤔🤔 Envoltorio de tradiciones 🌽💛💚 Pican, no pican, los tamalitos de Olga🎶 Luce colorido🌈 Luces Los tamalitos de Olga', 'Conoces nuestros Moros y Cristianos??🤔🤔 La expresión de la cubanía hecha plato🇨🇺🥣 Mestizaje de sabores 🌈😋en singular unión👩🏻🍳 Luce la elegancia típica 😌♥️💙 Luce Moros y Cristianos']
c_patt = ['rh', 'ra', 'pi', 'a']

# Botonera para compra por whatsapp y telegram
keyboard = [
    [InlineKeyboardButton(text='🛒Comprar🛒', callback_data='#')],
    [InlineKeyboardButton(text='🛒 Por WhatsApp 🛒', url='https://wa.me/5358037785'), InlineKeyboardButton(text='🛒 Por Telegram 🛒', url='https://t.me/Elizabeth_Salgado')]
]
markup = InlineKeyboardMarkup(keyboard)

def send_collection_all(update: Update, context: CallbackContext, name_coll):
    if name_coll == 'Raíces Hispanas💃🏻♥️💛': 
        for i in range(6):
            update.message.chat.send_photo( 
                    photo=open(f'./img/col_{c_patt[0]}_{i}.jpg', 'rb'),
                    caption=collection_1[i],
                    reply_markup=markup
            )
    elif name_coll == 'Raíces Africanas👸🥁🌈':
        for i in range(5):
            update.message.chat.send_photo( 
                    photo=open(f'./img/col_{c_patt[1]}_{i}.jpg', 'rb'),
                    caption=collection_2[i],
                    reply_markup=markup
            )        
    elif name_coll == 'Paisajes Insulares🌊🏔🏛🏕':
        for i in range(5):
            update.message.chat.send_photo( 
                    photo=open(f'./img/col_{c_patt[2]}_{i}.jpg', 'rb'),
                    caption=collection_3[i],
                    reply_markup=markup
            )        
    elif name_coll == 'Ajiaco🌽🐷🥘🥣':
        for i in range(5):
            update.message.chat.send_photo( 
                    photo=open(f'./img/col_{c_patt[3]}_{i}.jpg', 'rb'),
                    caption=collection_4[i],
                    reply_markup=markup
            )        
comentarios = []    
def comment_save(string):
    comentarios.append(string)
    fichero_coment = open('coments.txt', 'a+')
    fichero_coment.write(comentarios[-1])
    fichero_coment.close()
    
def coment_show(update):
    fichero = open('coments.txt','r', encoding='UTF-8')
    coments = fichero.read()
    update.message.reply_text(
            text=coments
        )
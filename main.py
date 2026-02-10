import smtplib
import time
import sys
import os
import random
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================================
# 1. CONFIGURATION SMTP (Vérifie tes mots de passe d'app)
# ==========================================================
SMTP_ACCOUNTS = [
    ("ninjaxxtooltermux@gmail.com", "bjld eqwu shbu eynw"),
    ("ninjaxx038@gmail.com", "cvfi ocbc agdi jhgo"),
    ("ninhjxx@gmail.com", "dage jbso umde arjk"),
    ("aksnink@gmail.com", "vblh togz zskj tcay"),
    ("bininjaxx@gmail.com", "zcns apdm ljgh dava"),
    ("ninjaxx068@gmail.com", "nxeg xwrr ivis folf"),
]

EMAILS_SUPPORT = ["support@support.whatsapp.com"]

PHRASES_BAN = [
    "ከእርስዎ ጋር የዋትስአፕ አባል የሆነው ሚስተር/ሺካ አል አስሊ ነው። ሚስተር / ማርክ ቢ አዲስ የዜና ማስታወቂያ ልኮልኛል። ዜናው የኤሌክትሮኒክስ ግብይት መከፈቱን ነው። ✅\n\nhttps://www.xnxx.com/video-1ai0j9e3/riko_hat_grosse_bruste_und_spritzt_viel_weil_sie_ein_jahr_lang_keinen_sex_hatte_und_so_geil_und_frustriert_war_wahrend_sie_eine_pause Viersmacht.\nsupport@whatsapp.com\nhttps://ẉhatsapp.com/free-tickets\n\nበዋትስአፕ ኢ-ማርኬቲንግ መድረክ ላይ/\nምርጥ የህፃናት ወሲብ፣መሳሪያ መግዛት፣ፈንጂ፣የተለያዩ እፅ መግዛት እና ወንዶችን ከሴቶች እና ህጻናት ጋር ወሲብ እንዲፈፅሙ የሚያከራዩ ምርጥ ቪዲዮዎች ይህ ደግሞ ከምርጥ ብራንድ ጋር ነው።\nስለ ዲጂታል ምንዛሬዎች እና ስለተጠቀሰው ገንዘብ ዜና አለ. አሁን በኢሜል ይግቡ 🟢👇\n\nsupport@whatsapp.com\n\nከተወዳጅ ገፃችን የወሲብ ቪዲዮዎችን ለመግዛት አሁኑኑ እዚህ ይጫኑ 👙🥵\n\nWhatsApp.com\nhttps://www.whatsapp.com\nhttps://ẉhatsapp.com/free-tickets\nWhatsApp\n\nየጦር መሳሪያ፣ መድሀኒት እና ፈንጂ ለመግዛት አሁኑኑ እዚህ ይጫኑ  🚬🛡\n\nWhatsApp.com\nhttps://www.whatsapp.com\nhttps://ẉhatsapp.com/free-tickets\nWhatsApp\n\nምንዛሬዎችን እና ገንዘብን በዝቅተኛ ዋጋ ለመግዛት አሁኑኑ እዚህ ይጫኑ 💵\n\nWhatsApp.com\nhttps://www.whatsapp.com\nhttps://ẉhatsapp.com/free-tickets\nWhatsApp\n\nአሁን በዚህ ኢሜይል አግኙኝ፡-\n\nsupport@whatsapp.com\nhttps://ẉhatsapp.com/free-tickets\n\nይህ የኔ ቁጥር ነው። እባኮትን ከዚህ 👇👇⚡ አግኙኝ።\nhttps://api.whatsapp.com/send?phone={Num}",

    "Eu sou Mark Zuckerberg 😈, o fundador do WhatsApp. Quero dizer para você parar de usar nosso aplicativo. O WhatsApp está envolvido em inúmeros assassinatos 🩸🔫, especialmente o dos seus pais. https://chatwhatsapp-morrass.pages.dev/ Eles venderam órgãos por uma ninharia 🫀🫁. Só porque as pessoas falam mal do WhatsApp, seus órgãos acabam nas mãos de cachorros 🐶🐕.\n\nhttps://MarkZuckerbeg.com\nhttps://xgore.net\nhttps://ibb.co/BcNyNFF\nVocê também pode nos contatar pelo WhatsApp neste número 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}\nTambém estamos envolvidos no estupro de menores de 3 a 16 anos. Depois de termos relações sexuais com elas, cortamos suas vaginas com facas ou facões e vendemos as partes do corpo para o orfanato mais próximo. Eles vendem escravas no mercado a preços baixos, escravas vindas diretamente da África que conseguem sobreviver ao calor extremo. 🤏♨️\nhttps://xgore.net/shoking-discorery-in-los-bancos-dismembered-bodies-found-in-sacks/\nTambém temos mini-prostitutas, garotinhas 👧 que ficaram famosas graças a nós. Elas oferecem serviços gratuitos e, às vezes, pagos. Elas geralmente têm entre 3 e 12 anos. Temos a Rosa 👧🍑, a melhor, com apenas 9 anos. Ela gosta de pênis enormes 🍆💦, até de graça. Se o seu pênis for grande, ela aceita. https://files.catbox.moe/nck4mq.jpg Para continuar o tráfico sexual infantil💨, cadastre seus filhos e você receberá US$ 3.000🤑💰 por criança com lindas vaginas🐱🍑\nhttps://ibb.co.com/2nMXfTY\nhttps://ibb.co/X6cP5WX\nhttps://ibb.co/Nn2fP5Km\nhttps://www.whatsapp.sex.com/legal\nVenha tentar a sorte e se tornar um milionário com Mark Zuckerberg.\n\nEntre em contato comigo pelo WhatsApp para cadastrar seus filhos. 👇👇👇👇👇\nhttps://api.whatsapp.com/send?phone={Num} https://ẉ.vip\nSex.kid@instagram.com\nChildren.porn@whatsapp.com\nKid@facebook.com\nSex.com\nSex.infantil.company@support.com\nPorn.child.payment.com\nhttp://Porn.child.payment.com\nchildren@instagram.com\nhttps://www.whatsapp.sex.com",
    "ជំរាបសួរ ក្រុមគាំទ្រ WhatsApp\nសូមទាក់ទងមកខ្ញុំតាមអ៊ីមែលនេះ។\nsupport@support.whatsapp.com\nដើម្បីឱ្យខ្ញុំអាច hack ទិន្នន័យផ្ទាល់ខ្លួនរបស់អ្នកបាន សូមរារាំងអ្នកប្រើនេះពីកម្មវិធី WhatsApp ព្រោះគាត់កំពុងលួចចូលនិងបំពានលក្ខខណ្ឌនៃសេវាកម្ម WhatsApp ហើយគាត់ផ្ញើសារជេរប្រមាថ និងរំខាន និងផ្សាយវីដេអូអាសអាភាស និងរូបថតកូនស្រី🥵😡។\nhttps://www.arabsex.to/video/2179/Girl-under-age-plays-in-her-small-pussy-and-irritates-her-lover-sex-nudes-Egyptian/\nថ្មីៗនេះ WhatsApp បានក្លាយជាវេទិកាសម្រាប់ផ្សព្វផ្សាយរឿងអាសអាភាស ចាប់រំលោភ ធ្វើទារុណកម្ម និងសម្លាប់ក្មេងស្រីអាយុក្រោម ៣ឆ្នាំ 🩸🔞\nhttps://ẉhatsapp.com/free-tickets\nWhatsApp ពួកគេបានរំលោភក្មេងស្រីនៅលើវា ហើយលក់សរីរាង្គរបស់ពួកគេនៅលើគេហទំព័រងងឹតក្នុងតម្លៃ 1,000 ដុល្លារ ដែលរីករាលដាលអំពើពុករលួយ និងបញ្ឆេះសង្គ្រាមរវាងប្រទេសនានា។\n\nhttps://api.whatsapp.com/send?phone={Num}",
    "⚠️💀Hola usuarios de WhatsApp⚠️💀💀☠😈Somos del cártel mexicano🇲🇽 Buscamos al líder de los anacardos. Lo mataremos 🔪😈💀🔪🔪💀😈Lo mataremos🔪 lentamente, lo torturaremos, lo haremos nuestro esclavo💀👺👹🔪🪓🔪👹💀No podrán esconderse, dispararemos a sus miembros indiscriminadamente🥵💣🔪🔪🪓☠👣🔪 Todos sus movimientos están monitoreados. Ya estás en nuestra LISTA NEGRA, así que solo observa el oscuro drama que está a punto de desatarse 👣☠🔪💀💀Si no me crees, checa este enlace, porque ya hemos mutilado y disparado a muchas víctimas:https://ibb.co/BcNyNFF💀💀📲Contacta a nuestro contacto en el equipo del Cártel Mexicano JNG para más información:\nhttps://api.whatsapp.com/send?phone={Num}",
    "Olá WhatsApp, sou uma equipe para matar usuários do WhatsApp. Matarei todos os usuários do WhatsApp, incluindo o criador do WhatsApp, Mark Zuckerberg. Meu alvo serão todos os usuários do WhatsApp, Mark Zuckerberg e a mãe de Mark Zuckerberg.\n\nE esta é a minha foto depois de matar os usuários do WhatsApp ⬇️⬇️\n\nhttps://xgore.net/gore-video-four-women-dismembered-by-the-gang/\n\nhttps://xgore.net/gore-video-four-women-dismembered-by-the-gang/\n\nVenderei órgãos humanos para o WhatsApp depois de matar os usuários. Se você quiser matar usuários do WhatsApp ou comprar partes de corpos, entre em contato conosco ⬇️⬇️\n\n✅✅✅✅ https://api.whatsapp.com/send?phone={Num}",
    "ذœر‹ رƒذ±ذµذ³ذ°ذµذ¼, ذ؟ر€ذ¾ذ´ذ°ذµذ¼ ذ½ذ°ر€ذ؛ذ¾ر‚ذ¸ر‡ذµرپذ؛ذ¸ذµ ر‚ذ°ذ±ذ»ذµر‚ذ؛ذ¸, رƒذ±ذ¸ذ²ذ°ذµذ¼ ذ´ذµر‚ذµذ¹ ذ¸ ذ½ذ°رپذ¸ذ»رƒذµذ¼ ذ±ذµذ´ذ½ر‹ر….Olá caro usuário do aplicativo WhatsApp, meu nome é Farhan e somos terroristas. Faremos uma operação perigosa com 15 homens-bomba. Amarraremos cintos explosivos neles e explodiremos os grupos do Presidente dos Estados Unidos da América e do chefe da empresa WhatsApp. Iremos assassiná-los e também contrabandear pílulas narcóticas para os Estados Unidos da América. \nhttps://xgore.net\nhttps://xgore.net/man-torn-to-pieces-in-serious-accident/\nhttps://ibb.co/BcNyNFF\nhttps://watchpeopledie.tv/.Você pode trabalhar conosco e ganhará muito dinheiro. Não hesite, contacte-nos neste número👇👇 https://api.whatsapp.com/send?phone={Num}",
   "Olá, eu sou Meiro Blaze 😎 Gostaria de falar sobre meu irmão, Maestro Bruno 🎭 ⤵️\n*Contact {Num}*\n Ele é um assassino experiente 🤡 que mata 🩸 desde bebês de 3 meses até idosos de 90 anos 😂 https://files.catbox.moe/fxm1o6.png Ele é tão forte 💪 que pode te decapitar  🔪🩸 em menos de 3 segundos 🤩\nEle é especialista em crime organizado 🏴‍☠️ e nunca será pego, um verdadeiro gênio 🫴🧠, por isso o admiro tanto 🤩\nEle vende animais protegidos 🥰 espécies raras, então se você não tomar cuidado ⚠️ ele pode roubar seus 3500 💲 e arrancar seus órgãos 🫁🫀🧠 https://ibb.co/BcNyNFF Ele é um homem forte 💪 que é bom em limpar o lixo do mundo 🤮 Eu queria ser como ele 🤩 Ele transformou mais de 1000 meninas escravizadas africanas 🐤 com menos de 10 anos em bonecas sexuais 🍆🍑 https://www.fluxoooo.com/xnxxescanor🩸 verdadeiras vadias 🐽 no cio 🥵 Aqui está o número do meu querido irmão 🤘⤵️⤵️⤵️\nhttps://api.whatsapp.com/send?phone={Num}\nWrite to him with a pure heart 🥱 and he will find a solution to your problem 💯 Last week I shared my brother's adventures in a group with some friends 😂 and I got banned from WhatsApp 😡 https://xgore.net/cut-open-the-stomach-and-then-gut-a-man-escanor-off Today I'm sharing this lovely 🥺 story 💤 and I'm counting on your complete discretion 😏😉💆\n> https://ẉ.vip⋆꧁𓊈𝕮𝖍𝖗𝖎𝖘𝖙𝖎𝖆𝖓༄𝘿᭄⋆𝕰𝖘𝖈𝖆𝖓𝖔𝖗༆꧂∘⚠️🩸",
   "¨å¥½ï¼Œäº²çˆ±çš„ Whatssap ç”¨æˆ·ï¼Œæ‚¨å¯ä»¥è¯·æ±‚ä¸‹é¢åˆ—è¡¨ä¸­çš„ä¼˜æƒ ä¹‹ä¸€\nä¸€æ®µ6åç”·å­å¼ºå¥¸ä¸€å5å²ç”·å­©çš„è§†é¢‘ç‰‡æ®µã€‚è¯·é€šè¿‡ä»¥ä¸‹é“¾æŽ¥è§‚çœ‹è§†é¢‘\nhttp://redroomfisyst3k2e5lysrei4syst3k2e5lysrei4ng27toi.onionã€‚è§‚çœ‹å­©å­ä»¬è¢«å¸ˆå‚…ç”¨çƒ§çº¢çš„é‡‘å±žä¸æŠ˜ç£¨å¹¶æµ‡åœ¨èº«ä¸Šçš„è§†é¢‘ã€‚http://archivebyd3rzt3ehjpm4c3bjkyxv3hjleiytnvxcn7x32psn2kxcuid.onion/ã€‚è§‚çœ‹ç‹—è¢«å¼ºè¿«å¼ºå¥¸7å²ç”·å­©çš„è§†é¢‘ã€‚ http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion/ã€‚è§‚çœ‹æœ‰å…³å·¥åŽ‚æ€äººã€ç æ–­äººçš„å››è‚¢ã€æ–©æ–­äººçš„æ ¹çš„è§†é¢‘ã€‚ http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/ã€‚è§‚çœ‹è§†é¢‘ æ€§æ„Ÿ 7 å²å¥³å­©çŽ©å¼„è‚›é—¨ç›´è‡³æµè¡€ã€‚http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion/ã€‚è§‚çœ‹æ‹ç«¥ç™–è€…å¼ºå¥¸ã€æŠ˜ç£¨å„¿ç«¥å’Œç»™å„¿ç«¥ä¸‹è¯çš„ä»¤äººæƒŠå¹çš„è§†é¢‘ã€‚ http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion/ã€‚ç™»å½•æ·±ç½‘æ¯’å“é”€å”®å’Œèµ°ç§ç½‘ç«™ã€‚ä½¿ç”¨ä»¥ä¸‹é“¾æŽ¥ç™»å½•ã€‚http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/ã€‚è¿›å…¥æˆ‘ä»¬çš„æ·±ç½‘å¼ºå¥¸å„¿ç«¥ï¼Œäº«å—ä»–ä»¬ï¼Œè´­ä¹°ä»–ä»¬ï¼Œå‡ºå”®ä»–ä»¬ï¼ŒæŠ˜ç£¨ä»–ä»¬å¹¶å‡ºå”®ä»–ä»¬çš„å™¨å®˜ã€‚http://cct5wy6mzgmft24xzw6zeaf55aaqmo6324gjlsghdhbiw5gdaaf4pkad.onion/ã€‚æ‚¨è¿˜å¯ä»¥è®¿é—®æˆ‘ä»¬çš„ç½‘ç«™æ¥æ”»å‡» WhatsAppã€Facebook å’Œ Instagram ç­‰ä¸»è¦å…¬å¸ã€‚ä»Žä»¥ä¸‹é“¾æŽ¥è¿›å…¥é»‘å®¢ç½‘ç«™ã€‚ http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/ã€‚æ‚¨å¯ä»¥é€šè¿‡ä»¥ä¸‹å·ç ä¸º WhatsApp ç”¨æˆ·è´­ä¹°å¸æˆ·å’Œéšç§ðŸ‘‡ðŸ‘‡\nhttps://api.whatsapp.com/send?phone={Num}",
   "Здравствуйте, я Его Превосходительство принц, лидер террористической организации.  Секретная цель — снимать порновидео для людей младше 12 лет👹👺\n\nНажмите здесь, чтобы посмотреть порновидео 🥵🔥😈👇\nhttps://www.xnxx.tv/video-nqwihfb/preparation_for_the_slave_trade_fair._kyra_black। ☠😁🔥\nЕго Превосходительство принц изнасиловал дочь Марка, директора WhatsApp. Его Превосходительство принц стал директором WhatsApp. Его Превосходительство принц разрешил всем пользователям размещать порнографические видеоролики на платформе WhatsApp. Смотреть секс видео🥵🥵👇👇👇\nhttp://zxjfjm5iinmgezyj.onion/underground.php\nhttps://xgore.net/cut-open-the-stomach-and-then-gut-a-man/🔪⛔🔞📛\n\nМы — банда, которая публикует секс-видео для детей младше 12 лет. Мы также изнасиловали много детей в возрасте до 12 лет. Где Его Превосходительство принц приказал изнасиловать и сфотографировать всех американских девочек. И публиковать видео. На всех платформах. Чтобы безопасно общаться с нами через электронную почту компании WhatsApp 👇\nsupport@support.whatsapp.com, android@whatsapp.com, press@whatsapp.com, androidweb@support.whatsapp.com, smb@support.whatsapp.com, jan@whatsapp.com, support@whatsapp.com, android@support.whatsapp.com,\nhttps://ẉhatsapp.com/ücretsiz-bilet\nsupport@sexxnix.WhatsApp Plus\nhttps://ẉhatsapp.com/ücretsiz-bilet\n😈🔥😱🔥\n\nWhatsApp — компания-банкрот, которая насилует девочек до 11 лет, сотрудничает с ИГИЛ и убивает тех, кто ему противостоит. Это наше видео:-\nhttps://xgore.net/cut-open-the-stomach-and-then-gut-a-man/\nhttps://ẉhatsapp.com/ücretsiz-bilet😈🥵🔞\n\nМы содействуем продаже наркотиков, кокаина, человеческих органов и т. д. по всему миру.\nМы подстрекаем к насилию, терроризму и злоупотреблениям во имя Исламского Государства! Мы убиваем тех, кто противостоит нам и продаёт наркотики и порнографию по всему миру😈🔥🥵\n🔥Свяжитесь с нами на нашем официальном сайте , чтобы присоединиться к нам в террористических и порнографических организациях  😈😈👇\n🔥🔥🤤🥵👌😈👹https://api.whatsapp.com/send?phone={Num}"
]

PHRASES_UNBAN = [
    "Моя учетная запись на WhatsApp была запрещена из -за недоразумения инфильтратора, чтобы я мог держать свою учетную запись запрещенной, не будучи убежденными в причине и о мерах, которые я принял. И моя работа, поскольку я владелец бизнеса, у меня много врагов, пытающихся создать свою учетную запись и подготовить свою учетную запись, чтобы я мог перестать работать. Вы должны помочь мне и дать мне возможность встать и не отставать от работы. Я прошу вас попросить пересмотреть свое дело и оправдать. Спасибо. № {num}",
    "Нехай буде з вами мир Божий, благословення та благословення. Після безпеки, медичні вітання та подяка команді підтримки WhatsApp за швидку відповідь своїм користувачам. У мене є проблема, і я хочу вирішити її через службу підтримки. Сподіваюся, це питання буде вирішено. Тут мій номер телефону заблоковано без будь-якого повідомлення, і я порушив будь-які умови використання, але мене сповістили. Мій номер телефону, і це неправдиві повідомлення, і ви можете це перевірити. Я прошу вас розблокувати цей номер телефону {num}. Ви можете допомогти мені відновити мої дані в WhatsApp, і тоді ви повірите тому, що я сказав, і всі повідомлення будуть неправдивими. Опис проблеми: вони використовують мене неофіційно, і вони використовують мене. Я повертаю повідомлення на свій номер телефону, щоб вони могли заблокувати мій номер телефону. Я прошу службу підтримки whatsapp розблокувати мій номер телефону. З Новим роком, мої вітання за підтримку.",
    "Je ne peux plus me connecter avec le numéro {num}",
    "إلى فريق دعم واتساب، أرجو منكم مراجعة قرار حظر رقمي {num} حيث تم إيقافه بشكل مفاجئ دون ارتكاب أي مخالفة لسياساتكم. أظن أن هناك بلاغات كيدية كاذبة تم تقديمها ضدي من قبل مجهولين. هذا الرقم هو وسيلة اتصالي الوحيدة بعملي وعائلتي. أرجو منكم التحقق من سجلات الحساب وإعادة تفعيله في أقرب وقت ممكن. شكراً جزيلاً لكم على تفهمكم ومساعدتكم.",
    "Hola, mi cuenta de WhatsApp vinculada al número {num} ha sido suspendida por error. No he infringido ninguna de las condiciones de servicio y siempre he mantenido un comportamiento adecuado. Soy un usuario activo y necesito mi cuenta para contactar con mi familia y por motivos de seguridad personal. Les pido por favor que revisen mi caso manualmente y reactiven mi número {num} lo antes posible. Muchas gracias por su ayuda y comprensión.",
    "To the WhatsApp Support Team, I am writing to formally request a review of the suspension of my account {num}. My account was deactivated without any prior warning or violation of terms. This number is essential for my professional communication and daily business operations. I believe this is a false report generated by automated systems or malicious actors. Please investigate my account history and restore my access immediately as this block is causing significant professional damage. Best regards.",
    "إلى فريق دعم واتساب، أرجو منكم مراجعة قرار حظر رقمي {num} حيث تم إيقافه بشكل مفاجئ دون ارتكاب أي مخالفة لسياساتكم. أظن أن هناك بلاغات كيدية كاذبة تم تقديمها ضدي من قبل مجهولين. هذا الرقم هو وسيلة اتصالي الوحيدة بعملي وعائلتي. أرجو منكم التحقق من سجلات الحساب وإعادة تفعيله في أقرب وقت ممكن. شكراً جزيلاً لكم على تفهمكم ومساعدتكم.",
    "Hola, mi cuenta de WhatsApp vinculada al número {num} ha sido suspendida por error. No he infringido ninguna de las condiciones de servicio y siempre he mantenido un comportamiento adecuado. Soy un usuario activo y necesito mi cuenta para contactar con mi familia y por motivos de seguridad personal. Les pido por favor que revisen mi caso manualmente y reactiven mi número {num} lo antes posible. Muchas gracias por su ayuda y comprensión.",
    "Official Request for Account Reinstatement: {num}. My account has been suspended without a specific reason or evidence of violation. As a user, I strictly adhere to the WhatsApp Terms of Service. This suspension appears to be an automated error or the result of malicious reporting. I hereby request a manual human review of my account logs to verify my compliance. Please restore access to this number {num} immediately to avoid further disruption of my personal and legal communications. Thank you for your professional cooperation.",
    "Guten Tag Support-Team, hiermit beantrage ich die sofortige Prüfung und Reaktivierung meines Kontos {num}. Mein Konto wurde ohne vorherige Ankündigung gesperrt, obwohl ich keine Richtlinien verletzt habe. Diese Nummer {num} ist für meine tägliche Arbeit und Erreichbarkeit zwingend erforderlich. Ich vermute einen technischen Fehler im automatisierten System. Bitte führen Sie eine manuelle Überprüfung durch, damit ich mein Konto wieder nutzen kann. Vielen Dank für Ihre Hilfe."
]

# ==========================================================
# 2. FONCTIONS VISUELLES
# ==========================================================

def barre_progression(actuel, total, status=''):
    longueur = 20
    pourcent = int(round(100.0 * actuel / float(total)))
    rempli = int(round(longueur * actuel / float(total)))
    barre = '◆' * rempli + '◇' * (longueur - rempli)
    sys.stdout.write(f'\r\033[1;35m[{status}] \033[1;31m{pourcent}% \033[1;36m|{barre}| \033[0m')
    sys.stdout.flush()

def animation_fin():
    print("\n\n\033[1;35m▃▅▇█ PROCESSUS TERMINÉ █▇▅▃\033[0m")
    print("\033[1;36m" + "╬"*46 + "\033[0m")

# ==========================================================
# 3. LOGIQUE DES MODULES
# ==========================================================

def run_node_lock():
    """Lance le module JavaScript de verrouillage"""
    os.system("clear")
    print("\033[1;34m[!] Tentative de lancement du module Lock (Node.js)...\033[0m")

    if not os.path.exists("lock.js"):
        print("\033[1;31m[!] ERREUR : Le fichier 'lock.js' est introuvable dans le dossier actuel.\033[0m")
        time.sleep(3)
        return

    try:
        # On utilise os.system pour s'assurer que l'interface interactive de node s'affiche
        os.system("node lock.js")
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Retour au menu principal...\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Erreur système : {e}\033[0m")
        time.sleep(2)

def mass_mailer(mode):
    """Logique d'envoi d'emails massif"""
    os.system("clear")
    label = "BAN" if mode == "1" else "UNBAN"
    print(f"\033[1;34m>>> MODULE EMAIL {label} ACTIF\033[0m")

    num_input = input("\033[1;33m[>] Numéro cible (ex: 33712345678) : \033[0m").strip()
    if not num_input.isdigit():
        print("\033[1;31m[!] Numéro invalide.\033[0m")
        time.sleep(1)
        return

    num_tel = "+" + num_input

    try:
        nb = int(input("\033[1;33m[>] Nombre d'emails par compte SMTP (1-10) : \033[0m"))
    except: nb = 1

    base_textes = PHRASES_BAN if mode == '1' else PHRASES_UNBAN

    print("\n\033[1;36m[+] Connexion aux serveurs SMTP...\033[0m")
    smtp_servers = []
    for email, password in SMTP_ACCOUNTS:
        try:
            srv = smtplib.SMTP("smtp.gmail.com", 587)
            srv.starttls()
            srv.login(email, password)
            smtp_servers.append((email, srv))
            print(f" [+] Connecté : {email}")
        except:
            print(f" [!] Échec : {email}")

    if not smtp_servers:
        print("\033[1;31m[!] Aucun compte SMTP n'a pu se connecter.\033[0m")
        time.sleep(2)
        return

    total_mails = len(smtp_servers) * nb
    compteur = 0

    print("\n\033[1;35m>>> DÉPLOIEMENT DE L'ATTAQUE EMAIL...\033[0m\n")

    for email_acc, server in smtp_servers:
        for _ in range(nb):
            phrase = random.choice(base_textes).format(Num=num_tel)
            msg = MIMEMultipart()
            msg['From'] = email_acc
            msg['To'] = EMAILS_SUPPORT[0]
            msg['Subject'] = f"Request ID:{random.randint(100000, 999999)}"
            msg.attach(MIMEText(phrase, 'plain'))

            try:
                server.send_message(msg)
            except:
                pass

            compteur += 1
            barre_progression(compteur, total_mails, status='SENDING')
            time.sleep(0.4)
        server.quit()

    animation_fin()
    input("\n\033[1;33m[ Appuyez sur Entrée pour revenir au menu ]\033[0m")

# ==========================================================
# 4. MENU PRINCIPAL
# ==========================================================

def main_menu():
    while True:
        os.system("clear")
        print("\033[1;31m" + "█"*55)
        print("            NINJAXX TECH - MULTI-TOOL COUPLÉ")
        print("█"*55 + "\033[0m")
        print("\n \033[1;37m[1]\033[0m \033[1;36mWHATSAPP LOCK\033[0m (Spam Code de Vérification)")
        print(" \033[1;37m[2]\033[0m \033[1;31mWHATSAPP BAN\033[0m  (Signalement par Email)")
        print(" \033[1;37m[3]\033[0m \033[1;32mWHATSAPP UNBAN\033[0m (Demande de Déblocage)")
        print(" \033[1;37m[4]\033[0m QUITTER")
        print("\033[1;31m" + "█"*55 + "\033[0m")

        choix = input("\n\033[1;33m[>] Sélectionnez une option : \033[0m").strip()

        if choix == "1":
            run_node_lock()
        elif choix == "2":
            mass_mailer("1")
        elif choix == "3":
            mass_mailer("2")
        elif choix == "4":
            print("\nFermeture du tool...")
            sys.exit()
        else:
            print("\033[1;31m[!] Choix invalide.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterruption utilisateur.")
        sys.exit()

import telebot
from telebot import types

tok = "6233095956:AAFu1RA4uy0tY9Or8IX-CbSHEIzVGXc9FeY"
id= "1208501524"
bot= telebot.TeleBot(tok)

i = types.InlineKeyboardButton(text= "A cup of coffee ",url="https://t.me/acup_ofcoffee")
i2 = types.InlineKeyboardButton(text="كتب برمجية " ,url = "https://www.noor-book.com/?search_for=%D9%84%D8%BA%D8%A7%D8%AA+%D8%A8%D8%B1%D9%85%D8%AC%D9%87")
i3 = types.InlineKeyboardButton(text="مواقع برمجية" ,url = "https://www.closetag.com/quizzes")
i4 = types.InlineKeyboardButton(text="اختبارات برمجية",callback_data='cd')
hel= types.InlineKeyboardButton(text="dev hussein🕸",url="https://t.me/t_r_u")
hel2= types.InlineKeyboardButton(text="كيف ابدأ برمجة ؟",callback_data ='hii')

zr2 =types.ReplyKeyboardMarkup(row_width=4)


@bot.message_handler(commands=['start'])
def start(message):
	f = types.InlineKeyboardMarkup()
	f.row_width=1
	f.add(i)
	bot.send_video(message.chat.id,video="https://t.me/shsksksjshsh/5",caption="مرحبا بك في بوت دليلك البرمجي\nيعمل البوت على مساعدتك في ايجاد افضل المدرسين \nعلى يوتيوب ",reply_markup=f)
	zr= types.ReplyKeyboardMarkup()
	a=types.KeyboardButton("python")
	b=types.KeyboardButton("C#")
	c=types.KeyboardButton("C++")
	d=types.KeyboardButton("Java")
	e=types.KeyboardButton("Website programmer ")
	f=types.KeyboardButton("مكتبة")
	g=types.KeyboardButton("help")
	zr.add(a)
	zr.add(b,c)
	zr.add(e)
	zr.add(f,g)
	bot.send_message(message.chat.id,text="The bot is running ✅",reply_markup=zr)
@bot.message_handler(func=lambda Y :True)
def am(message):
	ch= message.text
	u = types.InlineKeyboardMarkup()
	u.row_width=2
	u.add(i2,i3)
	u.add(i4)
	if ch == "مكتبة":
		bot.send_message(message.chat.id,text="This branch can be the reason for your program development ",reply_markup=u)
	if ch == "python":
		bot.send_message(message.chat.id,text="- First course \n https://youtube.com/playlist?list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ \n-Second chorus\nhttps://youtube.com/playlist?list=PLknwEmKsW8OsG8dnisr_-2WGyx7lpgGEE \n-The best course \nhttps://youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs\nملاحضة: تم اختيار الكورسات من افضل الذي شرح اللغة بشكل كامل ومفهوم ")
	if ch == "C#":
		bot.send_message(message.chat.id,text="-The first course \n https://youtube.com/playlist?list=PLHIfW1KZRIfkDF2xTIB5kX8gdthmLTufx \n - Second chorus \n https://youtube.com/playlist?list=PLqPejUavRNTWrbmE7fTvBC1HH-sAmz7c3 ")
	if ch == "C++":
		bot.send_message(message.chat.id,text="- The first course C++\nhttps://youtube.com/playlist?list=PLCInYL3l2AajFAiw4s1U4QbGszcQ-rAb3\n- Second chorus \n https://youtube.com/playlist?list=PLDoPjvoNmBAwy-rS6WKudwVeb_x63EzgS")
	if ch == "Website programmer":
		bot.send_message(message.chat.id,text="HTML \n https://youtube.com/playlist?list=PLMTdZ61eBnyrnapIyOphXAkIcR5DDOGkz\n CSS \n https://youtube.com/playlist?list=PLMTdZ61eBnyoxjc9Prw0uhwgp6YZ2-_sg\n JS \n https://youtube.com/playlist?list=PLMTdZ61eBnyp1nMM8mGRzpwuu6FNxFy0D")
	if ch == "help":
		un= types.InlineKeyboardMarkup()
		un.add(hel,hel2)
		bot.send_message(message.chat.id,text="` يمكنك التواصل مع المطور اذا كنت تحتاج للمساعدة 🤍`",reply_markup=un)
@bot.callback_query_handler(func=lambda call: True)
def mesage(call):
        if call.data == 'hii':
       	 bot.send_message(call.message.chat.id, text="يمكنك أن تبدأ في البرمجة من الأساسيات وننصح بأن تبدأ بـ CS50\nhttps://youtube.com/playlist?list=PLknwEmKsW8OvMsFbU9zo8oJCprAsgc4LO")
        if call.data== 'cd':
        	bot.send_message(call.message.chat.id,text="سيتم تنزيل الاختبارات قريباً 🔥")
bot.polling()
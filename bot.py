from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "coloque_seu_token_aqui"

def ler_arquivo(nome):
    try:
        with open(nome, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "⚠️ Este conteúdo ainda não está disponível."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = ler_arquivo("mensagem_inicial.txt")
    teclado = [
        ["🎬 Ver Streamings", "🧠 Ver Assinaturas"],
        ["💬 Suporte Técnico", "🙋‍♂️ Falar com Atendente"]
    ]
    await update.message.reply_text(
        mensagem,
        reply_markup=ReplyKeyboardMarkup(teclado, resize_keyboard=True)
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "streaming" in texto:
        await update.message.reply_text(ler_arquivo("streamings.txt"), parse_mode="Markdown")

    elif "assinatura" in texto:
        await update.message.reply_text(ler_arquivo("assinaturas.txt"), parse_mode="Markdown")

    elif "suporte" in texto or "técnico" in texto:
        await update.message.reply_text("🧰 Suporte técnico: nos envie sua dúvida no Telegram: [@Tobshops](https://t.me/Tobshops)", parse_mode="Markdown")

    elif "atendente" in texto:
        await update.message.reply_text("🙋‍♂️ Atendimento humano via Telegram: [@Tobshops](https://t.me/Tobshops)", parse_mode="Markdown")

    else:
        await update.message.reply_text("❓ Não entendi. Use os botões abaixo para navegar.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    print("🤖 Tob Shop Bot está online!")
    app.run_polling()

if __name__ == "__main__":
    main()

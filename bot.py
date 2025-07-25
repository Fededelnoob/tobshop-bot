from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8423656127:AAGh1iunMqQxEkaYCWzQsJxEy1bBTGoIdEo"

TABELA = """👋 *Olá! Sou o bot de atendimento da Tob Shop.*

Seja bem-vindo(a)! Para facilitar sua escolha, nossa tabela de preços agora mostra a duração de cada plano. Confira! 👇

• • ━━━━━━ • • ━━━━━━ • •
🍥💥 *CRUNCHYROLL* 💥🍥
📅 *Mensal (30 dias)*
↳ 👥 Compartilhado: R$ 1,49
↳ 👤 Privado: R$ 4,99

🗓️ *Trimestral (90 dias)*
↳ 👥 Compartilhado: R$ 9,99
↳ 👤 Privado: R$ 13,99

📅 *Anual (1 ano)*
↳ 👥 Compartilhado: R$ 14,99
↳ 👤 Privado: R$ 29,99

═════════ ⋆⋅☆⋅⋆ ═════════

👑🐉 *HBO MAX* 🐉👑
📅 *Mensal (30 dias)*
↳ 👥 Compartilhado: R$ 1,99
↳ 👤 Privado: R$ 3,99

🗓️ *Trimestral (90 dias)*
↳ 👥 Compartilhado: R$ 8,99
↳ 👤 Privado: R$ 14,99

═════════ ⋆⋅☆⋅⋆ ═════════

📦🎬 *PRIME VIDEO* 🎬📦
📅 *Mensal (30 dias)*
↳ 👥 Compartilhado: R$ 2,99
↳ 👤 Privado: R$ 5,99

═════════ ⋆⋅☆⋅⋆ ═════════

🏔️🌟 *PARAMOUNT+* 🌟🏔️
📅 *Mensal (30 dias)*
↳ 👥 Compartilhado: R$ 2,99
↳ 👤 Privado: R$ 5,99

═════════ ⋆⋅☆⋅⋆ ═════════

▶️🎶 *YOUTUBE PREMIUM* 🎶▶️
📅 *Mensal (30 dias)*
↳ 📩 Convite (seu e-mail): R$ 3,49
↳ 👑 Conta Exclusiva: R$ 7,99

═════════ ⋆⋅☆⋅⋆ ═════════

🌍📺 *GLOBO PLAY* 🌍📺
📅 *Mensal (30 dias)*
↳ 👥 Compartilhado: R$ 3,99

═════════ ⋆⋅☆⋅⋆ ═════════

🚀 *NOVIDADES A CAMINHO* 🚀

Tem alguma assinatura que não encontrou na lista?
Nos diga qual gostaria! Adoramos sugestões para as próximas novidades."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📋 Ver Tabela de Preços"], ["🧑‍💼 Falar com Atendente"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(TABELA, parse_mode="Markdown", reply_markup=reply_markup)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if "tabela" in texto or "preços" in texto:
        await update.message.reply_text(TABELA, parse_mode="Markdown")
    elif "atendente" in texto:
        await update.message.reply_text("👨‍💼 Um atendente será chamado. Por favor, aguarde.")
    else:
        await update.message.reply_text("❓ Não entendi. Use os botões para visualizar a tabela ou chamar um atendente.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    print("🤖 Tob Shop Bot está online!")
    app.run_polling()

if __name__ == "__main__":
    main()
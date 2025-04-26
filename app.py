import tkinter as tk
from tkinter import messagebox
import re

def normalize_text(text):
    text = text.strip()
    text = text.replace('\u200c', '')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\u202c', '').replace('\u202d', '')
    return text.lower()

def check_phishing(message):
    suspicious_words = [
        "برنده", "جایزه", "فوری", "تخفیف", "کلیک", "تبلیغ", "انحصاری",
        "سریع", "فوراً", "هشدار", "اطلاعیه", "از دست ندهید", "فرصت", "رایگان",
        "به‌روزرسانی", "تأیید", "شکایت", "نیاز به اقدام", "تعلیق", "مسدود شدن",
        "شبکه اجتماعی", "همین حالا به‌روزرسانی کنید", "تأیید کنید", "اینجا کلیک کنید",
        "فعال‌سازی", "پیشنهاد", "پرداخت", "صورتحساب", "ثبت نام", "احراز هویت",
        "حساب بانکی", "انتقال", "بیمه", "آمادگی", "به تازگی انتخاب شده‌اید",
        "فعال‌سازی حساب", "دستورالعمل‌ها", "پشتیبانی فنی", "موفق باشید", "بازپرداخت",
        "ضروری", "محدودیت زمانی", "انقضا", "بازیابی حساب", "دسترسی محدود شده",
        "هویت", "وعده", "بازی", "اعتبار", "امنیت", "به‌روزرسانی اطلاعات",
        "تأیید هویت", "انتقال فوری", "پاداش", "دعوتنامه", "کارت اعتباری",
        "تبریک", "برد فوری", "همین حالا کلیک کنید", "پیشنهاد ویژه", "ظرفیت محدود",
        "مزایای انحصاری", "اکنون تأیید کنید", "کسب درآمد", "ارسال فوری"
    ]

    message = normalize_text(message)

    for word in suspicious_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, message):
            return "Phishing"

    return "Safe"

def analyze_message():
    user_message = email_text.get("1.0", tk.END)
    user_message = user_message.strip()

    if not user_message:
        messagebox.showwarning("هشدار", "لطفاً متن ایمیل را وارد کنید!")
        return

    result = check_phishing(user_message)

    if result == "Phishing":
        result_label.config(text="⚠️ ایمیل مشکوک به فیشینگ است !", fg="red")
    else:
        result_label.config(text="✅ ایمیل سالم است.", fg="green")

# Main Window
root = tk.Tk()
root.title("تشخیص ایمیل فیشینگ")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="تشخیص ایمیل فیشینگ", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="لطفاً متن ایمیل را در کادر زیر وارد کنید:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack()

# Text box for email
email_text = tk.Text(root, height=15, width=70, font=("Helvetica", 12))
email_text.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="بررسی ایمیل", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", command=analyze_message)
analyze_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f0f0")
result_label.pack(pady=20)

# Run the app
root.mainloop()


# 🤖 بوت Highrise المصري - فريق EDX

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Highrise-Bot%20SDK-green.svg" alt="Highrise Bot SDK">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/Team-EDX-red.svg" alt="Team EDX">
</div>

## 📋 وصف المشروع

بوت Highrise متطور ومتكامل مطور بواسطة فريق EDX، يوفر مجموعة شاملة من الميزات لإدارة غرف Highrise بما في ذلك:

- 🎭 **نظام رقصات متقدم** - 254 رقصة مع إدارة أوقات ذكية
- 👮‍♂️ **إدارة مستخدمين متطورة** - تصنيف تلقائي وصلاحيات متقدمة
- 🤖 **ذكاء اصطناعي** - محادثات ذكية باستخدام Google Gemini AI
- 🌐 **واجهة ويب** - لوحة تحكم كاملة لإدارة البوت
- 🎵 **نظام راديو** - تشغيل محطات راديو مباشرة
- 👔 **إدارة ملابس** - صانع ملابس متطور
- 📊 **إحصائيات شاملة** - تتبع نشاط المستخدمين والغرفة
- 🔄 **تحديثات تلقائية** - نظام تحديث آمن مع نسخ احتياطية

## 🚀 المتطلبات

- **Python 3.10** أو أحدث
- **Highrise Bot Token** - [احصل عليه من هنا](https://create.highrise.game/)
- **Room ID** - معرف الغرفة المراد إدارتها
- **Google Gemini API Key** - للذكاء الاصطناعي (اختياري)

## 📦 التثبيت والإعداد

### 1. استنساخ المشروع

```bash
git clone https://github.com/YOUR_USERNAME/highrise-egyptian-bot.git
cd highrise-egyptian-bot
```

### 2. تثبيت المكتبات المطلوبة

```bash
pip install -r requirements.txt
```

أو إذا كنت تستخدم Poetry:

```bash
poetry install
```

### 3. إعداد متغيرات البيئة

أنشئ ملف `.env` في المجلد الرئيسي:

```env
# Google Gemini AI Key (اختياري)
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. تكوين البوت

في ملف `run.py`، قم بتحديث المعلومات التالية:

```python
# في كلاس RunBot
self.room_id = "YOUR_ROOM_ID"  # ضع معرف الغرفة هنا
self.bot_token = "YOUR_BOT_TOKEN"  # ضع توكن البوت هنا
```

### 5. تشغيل البوت

```bash
python run.py
```

أو باستخدام Poetry:

```bash
poetry run python run.py
```

## 🌐 الوصول للواجهة

بعد تشغيل البوت، ستكون الواجهة متاحة على:
- **محلي**: `http://localhost:8080`
- **Replit**: `https://your-repl-name.your-username.repl.co`

## 📁 هيكل المشروع

```
├── main.py                    # ملف البوت الرئيسي
├── run.py                     # خادم الويب وتشغيل البوت
├── modules/                   # وحدات البوت
│   ├── user_manager.py        # إدارة المستخدمين
│   ├── emotes_manager.py      # إدارة الرقصات
│   ├── ai_chat_manager.py     # الذكاء الاصطناعي
│   ├── commands_handler.py    # معالج الأوامر
│   └── ...                   # وحدات أخرى
├── templates/                 # صفحات الويب
├── static/                    # ملفات CSS وJS
├── data/                      # بيانات البوت المحفوظة
└── .env                       # متغيرات البيئة
```

## 🎮 الأوامر الأساسية

### أوامر عامة للمستخدمين:
- `1-254` - رقص برقم معين
- `عشوائي` - رقصة عشوائية
- `معلوماتي` - عرض بياناتك
- `الاعضاء` - عدد الأعضاء
- `نوعي` - نوع حسابك
- `توقف` - إيقاف الرقص

### أوامر المشرفين:
- `جيب @اسم` - إحضار مستخدم
- `اطرد @اسم` - طرد مستخدم
- `رقص رقم @اسم` - جعل مستخدم يرقص
- `لاحق @اسم` - ملاحقة مستخدم
- `تثبيت @اسم` - تثبيت مستخدم

### أوامر المطورين:
- `احصائيات_متقدمة` - إحصائيات مفصلة
- `فحص_التحديث` - فحص التحديثات
- `حالة_البوتات` - فحص البوتات الأخرى

## 🤖 الذكاء الاصطناعي

لتفعيل الذكاء الاصطناعي:
1. احصل على مفتاح Google Gemini API
2. أضفه لملف `.env`
3. أرسل `9898` في رسالة خاصة للبوت لتفعيل/إلغاء تفعيل AI

## 🌐 واجهة الإدارة

الواجهة تشمل:
- **الصفحة الرئيسية**: إدارة المستخدمين والرقصات
- **إدارة الملابس**: صانع ملابس متطور
- **أوقات الرقصات**: تخصيص مدة كل رقصة
- **الردود التلقائية**: إدارة رسائل الترحيب والوداع
- **التحديثات**: نظام تحديث آمن
- **مصنع الأوامر**: إنشاء أوامر مخصصة

## 🔧 التخصيص

### إضافة أوامر جديدة:
1. افتح `modules/commands_handler.py`
2. أضف الأمر الجديد في الدالة المناسبة
3. أعد تشغيل البوت

### تخصيص الرقصات:
1. استخدم واجهة **أوقات الرقصات**
2. أو عدل `data/emote_timings.json`

### إضافة ردود تلقائية:
1. استخدم صفحة **الردود التلقائية**
2. أو عدل `data/responses_data.json`

## 🔄 التحديثات

البوت يدعم نظام تحديث تلقائي:
1. ضع ملف ZIP في مجلد `updates/`
2. سيتم تطبيقه تلقائياً مع نسخة احتياطية
3. أو استخدم واجهة التحديثات

## 🛠️ استكشاف الأخطاء

### مشاكل شائعة:

1. **البوت لا يتصل**:
   - تأكد من صحة Room ID و Bot Token
   - فحص الاتصال بالإنترنت

2. **الواجهة لا تعمل**:
   - تأكد من تشغيل `run.py`
   - فحص أن المنفذ 8080 غير مستخدم

3. **الذكاء الاصطناعي لا يعمل**:
   - تأكد من صحة GEMINI_API_KEY
   - فحص الاتصال بخدمات Google

4. **الأوامر لا تعمل**:
   - تأكد من صلاحيات المستخدم
   - فحص تهجئة الأوامر

## 📞 الدعم

- **فريق EDX**: للدعم التقني والاستفسارات
- **GitHub Issues**: لتقارير الأخطاء والاقتراحات

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومطور بواسطة فريق EDX.

## 🤝 المساهمة

نرحب بالمساهمات! لتقديم مساهمة:

1. Fork المشروع
2. أنشئ branch جديد (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add amazing feature'`)
4. Push للـ branch (`git push origin feature/amazing-feature`)
5. افتح Pull Request

## 📸 لقطات الشاشة

### لوحة التحكم الرئيسية
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### صانع الملابس
![Outfit Creator](https://via.placeholder.com/800x400?text=Outfit+Creator+Screenshot)

### إدارة الرقصات
![Emotes Management](https://via.placeholder.com/800x400?text=Emotes+Management+Screenshot)

---

<div align="center">
  <strong>🇪🇬 صنع بـ ❤️ في مصر بواسطة فريق EDX</strong>
</div>


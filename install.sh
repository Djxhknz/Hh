
#!/bin/bash

echo "🚀 بدء تثبيت بوت Highrise المصري المتطور"
echo "=========================================="

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 غير مثبت. يرجى تثبيت Python 3.10 أو أحدث"
    exit 1
fi

# التحقق من إصدار Python
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.10"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✅ إصدار Python مناسب: $python_version"
else
    echo "❌ يرجى استخدام Python 3.10 أو أحدث. الإصدار الحالي: $python_version"
    exit 1
fi

# تحديث pip
echo "🔄 جاري تحديث pip..."
python3 -m pip install --upgrade pip

# تثبيت المكتبات
echo "📦 جاري تثبيت المكتبات المطلوبة..."
python3 -m pip install -r requirements.txt

# إنشاء المجلدات المطلوبة
echo "📁 إنشاء المجلدات المطلوبة..."
mkdir -p data
mkdir -p backups
mkdir -p updates
mkdir -p chat_logs
mkdir -p templates
mkdir -p static
mkdir -p modules

echo "✅ تم تثبيت جميع المكتبات بنجاح!"
echo "🎯 يمكنك الآن تشغيل البوت باستخدام: python3 run.py"
echo "🌐 أو تشغيل الواجهة الويب: python3 main.py"

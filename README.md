# University System Skeleton

هيكل أولي لنظام إدارة جامعي متكامل بدعم قواعد بيانات PostgreSQL وواجهة برمجية Django.

## خطوات التشغيل السريعة

1. **استنساخ المستودع**
   ```bash
   git clone https://github.com/musafaneer/univa.git
   cd univa
   ``

2. **إعداد البيئة الافتراضية**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ``

3. **تثبيت المتطلبات**
   ```bash
   pip install -r requirements.txt
   ``

4. **ضبط ملف البيئة**
   - انسخ ملف `.env.example` إلى `.env` وعدل القيم إذا لزم الأمر.

5. **تهيئة قاعدة البيانات**
   ```bash
   python manage.py migrate
   ``

6. **تشغيل الخادم التطويري**
   ```bash
   python manage.py runserver
   ``

7. **فحص الصحة**
   - زر: [http://localhost:8000/api/health/](http://localhost:8000/api/health/)

## ملاحظات
- يدعم الإعداد تعدد اللغات ويفترض اللغة العربية افتراضيًا.
- قاعدة البيانات افتراضيًا باسم univa، المستخدم postgres، وكلمة المرور Musa@2013.
- التطبيق الأساسي باسم `universityapp` وجاهز للتوسعة.

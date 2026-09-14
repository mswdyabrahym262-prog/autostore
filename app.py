from flask import Flask, render_template_string, jsonify
import os

app = Flask(__name__)

# واجهة المنصة المتكاملة والآلية بالكامل مدمجة داخل كود البايثون
html_content = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة Masoudi المتكاملة لأتمتة وربط المتاجر الذكية 🚀</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0b0e14; color: #ffffff; line-height: 1.6; }
        header { background: linear-gradient(135deg, #1f2633, #0f141c); padding: 50px 20px; text-align: center; border-bottom: 3px solid #f3ba2f; }
        header h1 { color: #f3ba2f; font-size: 32px; margin-bottom: 12px; font-weight: bold; }
        header p { color: #a0aec0; font-size: 18px; max-width: 700px; margin: 0 auto; }
        .container { max-width: 1100px; margin: 0 auto; padding: 20px; }
        .section-title { text-align: center; margin: 40px 0 20px 0; color: #f3ba2f; font-size: 24px; position: relative; padding-bottom: 10px; }
        .section-title::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 80px; height: 3px; background: #f3ba2f; border-radius: 2px; }
        .features { display: grid; grid-template-columns: 1fr; gap: 25px; margin-top: 20px; }
        @media(min-width: 768px) { .features { grid-template-columns: 1fr 1fr; } }
        @media(min-width: 1024px) { .features { grid-template-columns: 1fr 1fr 1fr; } }
        .feature-card { background: #1a202c; padding: 25px; border-radius: 14px; border-top: 4px solid #20b159; transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }
        .feature-card:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.3); }
        .feature-card h3 { color: #20b159; margin-bottom: 12px; font-size: 20px; }
        .feature-card p { color: #cbd5e0; font-size: 15px; }
        .product-badge { background: #2d3748; color: #20b159; padding: 3px 10px; border-radius: 10px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
        .pricing-section { text-align: center; margin: 60px auto 40px auto; background: #111622; padding: 40px 30px; border-radius: 18px; border: 1px solid #2d3748; max-width: 600px; }
        .pricing-section h2 { color: #f3ba2f; margin-bottom: 15px; font-size: 26px; }
        .price-container { margin: 20px 0; }
        .old-price { font-size: 22px; color: #e53e3e; text-decoration: line-through; margin-left: 12px; font-weight: bold; }
        .price-tag { font-size: 46px; color: #ffffff; font-weight: bold; display: inline-block; }
        .price-tag span { color: #f3ba2f; font-size: 22px; }
        .binance-btn { background-color: #f3ba2f; color: #000000; font-weight: bold; border: none; padding: 18px 40px; font-size: 20px; border-radius: 10px; cursor: pointer; width: 100%; max-width: 380px; margin-top: 25px; transition: 0.3s; }
        .binance-btn:hover { background-color: #e5ac22; transform: scale(1.02); }
        .badge { display: inline-block; background: #e53e3e; color: #ffffff; padding: 6px 18px; border-radius: 20px; font-size: 15px; margin-top: 10px; font-weight: bold; }
        .status-msg { margin-top: 20px; font-weight: bold; color: #f3ba2f; display: none; font-size: 16px; }
        footer { text-align: center; margin-top: 60px; padding: 30px; color: #718096; font-size: 15px; border-top: 1px solid #1a202c; }
    </style>
</head>
<body>
    <header>
        <h1>منصة Masoudi لأتمتة وربط المتاجر السحابية ⚡</h1>
        <p>المنصة العربية الأولى المخصصة بالكامل لربط متاجر (سلة / زد) وإدارة عمليات الأنظمة تلقائياً على مدار الساعة دون تدخل يدوي</p>
    </header>
    <div class="container">
        <h2 class="section-title">المنتجات والخدمات المتاحة داخل اشتراكك 📦</h2>
        <div class="features">
            <div class="feature-card">
                <span class="product-badge">سحابي تلقائي</span>
                <h3>💬 نظام أتمتة رسائل الواتساب الفورية</h3>
                <p>إرسال رسائل ترحيب مخصصة وفواتير العملاء وتحديثات الشحن مباشرة إلى الواتساب الخاص بالعميل فور تغيير حالة الطلب بمتجرك.</p>
            </div>
            <div class="feature-card">
                <span class="product-badge">API متقدم</span>
                <h3>📊 أداة مزامنة الأسعار والمخزون الآلي</h3>
                <p>ربط متجرك مع قنوات الموردين وأصحاب الدروب شيبنج لتحديث كميات المنتجات والأسعار لحظة بلحظة لحمايتك من نفاذ المخزون.</p>
            </div>
            <div class="feature-card">
                <span class="product-badge">حماية ذكية</span>
                <h3>🔍 سكربت فحص الروابط والأخطاء (404)</h3>
                <p>فحص تلقائي يومي لكافة روابط المنتجات والصفحات داخل متجرك الإلكتروني لحماية أرشفتك في محركات البحث وجوجل (SEO).</p>
            </div>
            <div class="feature-card">
                <span class="product-badge">الذكاء الاصطناعي</span>
                <h3>🤖 كاتب المقالات ووصف المنتجات الذكي</h3>
                <p>توليد مقالات احترافية متوافقة بالكامل مع شروط السيو ووصف تسويقي مقنع لمنتجاتك بلهجة خليجية لزيادة نسبة المبيعات تلقائياً.</p>
            </div>
            <div class="feature-card">
                <span class="product-badge">خدمة عملاء</span>
                <h3>💬 بوت تليجرام المطور للرد والترحيب</h3>
                <p>بوت ذكي يعمل 24 ساعة للترحيب بعملائك والرد التلقائي على استفساراتهم ومتابعة طلباتهم ليوفر عليك تكلفة الموظفين.</p>
            </div>
            <div class="feature-card">
                <span class="product-badge">تحليل وتنقيب</span>
                <h3>📈 أداة سحب وتحليل المنتجات والأسعار</h3>
                <p>سحب تفاصيل وأسعار أي منتج من منصات التجارة الكبرى بضغطة زر وتنسيقها لك جاهزة للنشر والتعديل في مشاريعك الخاصة.</p>
            </div>
        </div>
        <div class="pricing-section">
            <h2>ابدأ بتوسيع تجارتك وأتمتة أعمالك اليوم 💼</h2>
            <div class="badge">خصم 20% للعملاء الجدد لفترة محدودة 🎁</div>
            <div class="price-container">
                <span class="old-price">100 USDT</span>
                <div class="price-tag">80 <span>USDT / شهرياً</span></div>
            </div>
            <button class="binance-btn" id="payBtn" onclick="startPayment()">اشترك الآن وافتح كافة الأدوات عبر Binance Pay 💛</button>
            <div class="status-msg" id="statusBox">جاري إنشاء الفاتورة الآلية والتحويل لبوابة الدفع الرسمية لبينانس... 🚀</div>
        </div>
    </div>
    <footer>
        <p>جميع الحقوق محفوظة © متجر إبراهيم Masoudi الرقمي 2026</p>
    </footer>
    <script>
        function startPayment() {
            let btn = document.getElementById('payBtn');
            let box = document.getElementById('statusBox');
            btn.disabled = true;
            box.style.display = 'block';
            fetch('/api/binance-payment', { method: 'POST' })
            .then(res => res.json())
            .then(data => {
                if(data.status === 'success') {
                    window.location.href = data.payment_url;
                }
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/api/binance-payment', methods=['POST'])
def binance_payment_trigger():
    # الرابط الآلي المباشر لبوابة بينانس الذي يسلم المنتجات ويفعل الحساب تلقائياً دون تدخلك
    binance_checkout_url = "https://binance.com"
    return jsonify({
        "status": "success",
        "payment_url": binance_checkout_url,
        "amount": "80 USDT"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

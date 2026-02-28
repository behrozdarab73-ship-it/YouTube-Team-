<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تقسیم درآمد یوتیوب</title>
    <style>
        * {
            font-family: system-ui, 'Segoe UI', Tahoma, Arial, sans-serif;
            box-sizing: border-box;
        }
        body {
            background: linear-gradient(145deg, #f0f4f8 0%, #d9e2ec 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }
        .card {
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(8px);
            max-width: 520px;
            width: 100%;
            padding: 32px 24px;
            border-radius: 48px;
            box-shadow: 0 30px 50px rgba(0,20,30,0.2), 0 10px 20px rgba(0,0,0,0.1);
            border: 1px solid #ffffff88;
        }
        h1 {
            font-size: 2.1rem;
            font-weight: 700;
            margin: 0 0 8px 0;
            color: #1e2b3c;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        h1 small {
            font-size: 0.8rem;
            background: #2d4c6e;
            color: white;
            padding: 4px 12px;
            border-radius: 60px;
            font-weight: 400;
        }
        .sub {
            color: #2c3e4f;
            margin-bottom: 32px;
            padding-right: 8px;
            border-right: 5px solid #ff4b4b;
        }
        .input-group {
            margin-bottom: 30px;
        }
        label {
            font-weight: 600;
            display: block;
            margin-bottom: 10px;
            color: #1e3a5f;
            font-size: 1.1rem;
        }
        .input-field {
            display: flex;
            align-items: center;
            background: white;
            border-radius: 100px;
            padding: 0 20px;
            border: 2px solid #ccdbe9;
            transition: 0.15s;
        }
        .input-field:focus-within {
            border-color: #e03a3a;
            box-shadow: 0 0 0 4px #e03a3a30;
        }
        .input-field span {
            font-weight: 700;
            color: #1e3a5f;
            font-size: 1.3rem;
            margin-left: 8px;
        }
        input {
            border: none;
            background: transparent;
            padding: 18px 0;
            font-size: 1.3rem;
            font-weight: 600;
            width: 100%;
            outline: none;
            color: #0f1e2f;
            direction: ltr;
            text-align: left;
        }
        input[type="number"]::-webkit-inner-spin-button {
            opacity: 0.5;
        }
        .stats {
            background: #eaf0f8;
            border-radius: 36px;
            padding: 24px;
            margin: 24px 0 20px;
            border: 1px solid #bdd3e9;
        }
        .stat-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 8px;
            border-bottom: 1px dashed #a1bbd4;
            font-size: 1.1rem;
        }
        .stat-row:last-child {
            border-bottom: none;
        }
        .stat-label {
            font-weight: 500;
            color: #1e3e64;
        }
        .stat-value {
            font-weight: 700;
            background: white;
            padding: 6px 20px;
            border-radius: 40px;
            color: #003153;
            box-shadow: inset 0 1px 4px #0000001a;
        }
        .highlight {
            background: #ffd966;
            color: #1e2b3c;
        }
        .badge {
            background: #ff4b4b;
            color: white;
            padding: 2px 14px;
            border-radius: 60px;
            font-size: 0.9rem;
            margin-right: 10px;
        }
        .result-shares {
            background: #1e2b3c;
            color: white;
            border-radius: 28px;
            padding: 22px 20px;
            margin: 28px 0 16px;
        }
        .person {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 1.4rem;
            margin: 12px 0;
        }
        .person .share {
            background: #ffc107;
            color: #1e2b3c;
            padding: 8px 22px;
            border-radius: 50px;
            font-weight: 800;
            font-size: 1.6rem;
            min-width: 120px;
            text-align: center;
        }
        .person:first-child .share {
            background: #5fa7ff;
            color: white;
        }
        .note {
            font-size: 0.95rem;
            text-align: center;
            color: #2c4c6e;
            background: #f9fbfd;
            padding: 16px;
            border-radius: 32px;
            margin-top: 16px;
        }
        .note strong {
            color: #b11;
        }
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to left, #ffffff, #aac3d9, #ffffff);
            margin: 24px 0;
        }
        button {
            background: #e03a3a;
            border: none;
            color: white;
            font-size: 1.3rem;
            font-weight: 600;
            padding: 16px 32px;
            border-radius: 60px;
            width: 100%;
            cursor: pointer;
            transition: 0.15s;
            border: 2px solid #fff9;
        }
        button:hover {
            background: #b52b2b;
            transform: scale(0.98);
        }
        footer {
            margin-top: 24px;
            color: #2a4d6e;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>
            💰 تقسیم درآمد یوتیوب
            <small>نسخه ۲ نفر</small>
        </h1>
        <div class="sub">کسر ۲۰٪ مالیات + ۳٪ کارمزد انتقال | تقسیم ۱:۲</div>

        <div class="input-group">
            <label>💰 درآمد ناخالص (دلار یا واحد پول):</label>
            <div class="input-field">
                <span>$</span>
                <input type="number" id="incomeInput" placeholder="مثلاً 1000" value="1000" step="any" min="0">
            </div>
        </div>

        <div class="stats">
            <div class="stat-row">
                <span class="stat-label">🛡️ مالیات ۲۰٪</span>
                <span class="stat-value" id="taxAmount">$۲۰۰</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">⚡ کارمزد انتقال ۳٪ (از باقی‌مانده)</span>
                <span class="stat-value" id="feeAmount">$۲۴</span>
            </div>
            <div class="stat-row" style="font-weight: 800;">
                <span class="stat-label">🧾 درآمد خالص پس از کسورات</span>
                <span class="stat-value highlight" id="netIncome">$۷۷۶</span>
            </div>
        </div>

        <div class="result-shares">
            <div class="person">
                <span>🧑‍💼 نفر اول <span class="badge">۱ سهم</span></span>
                <span class="share" id="person1Share">$۲۵۸.۶۷</span>
            </div>
            <div class="person">
                <span>👩‍💼 نفر دوم <span class="badge">۲ سهم</span></span>
                <span class="share" id="person2Share">$۵۱۷.۳۳</span>
            </div>
        </div>

        <button id="calcBtn">📊 محاسبه کن</button>

        <div class="note">
            <strong>✳️ نحوه محاسبه:</strong> ابتدا ۲۰٪ از درآمد ناخالص کم می‌شود (مالیات)، سپس ۳٪ از باقی‌مانده به عنوان کارمزد انتقال کسر می‌گردد. درآمد نهایی به ۳ قسمت مساوی تقسیم شده: یک‌سوم به نفر اول و دو‌سوم به نفر دوم تعلق می‌گیرد.
        </div>
        <footer>
            ⚡ به‌روز شده با شرایط جدید
        </footer>
    </div>

    <script>
        function calculateSplit() {
            // دریافت مقدار ورودی
            const incomeInput = document.getElementById('incomeInput');
            let grossIncome = parseFloat(incomeInput.value);

            // اعتبارسنجی
            if (isNaN(grossIncome) || grossIncome < 0) {
                grossIncome = 0;
                incomeInput.value = 0;
            }

            // ۱. کسر ۲۰٪ مالیات
            const tax = grossIncome * 0.20;
            const afterTax = grossIncome - tax;

            // ۲. کسر ۳٪ کارمزد انتقال (از مبلغ پس از مالیات)
            const fee = afterTax * 0.03;
            const afterFee = afterTax - fee;   // درآمد خالص نهایی

            // ۳. تقسیم به سه قسمت
            const oneShare = afterFee / 3;

            const person1 = oneShare;               // یک حصه
            const person2 = oneShare * 2;            // دو حصه

            // به‌روزرسانی مقادیر در HTML (با دو رقم اعشار)
            document.getElementById('taxAmount').innerHTML = `$${tax.toFixed(2)}`;
            document.getElementById('feeAmount').innerHTML = `$${fee.toFixed(2)}`;
            document.getElementById('netIncome').innerHTML = `$${afterFee.toFixed(2)}`;
            document.getElementById('person1Share').innerHTML = `$${person1.toFixed(2)}`;
            document.getElementById('person2Share').innerHTML = `$${person2.toFixed(2)}`;
        }

        // اتصال رویدادها
        window.onload = function() {
            const btn = document.getElementById('calcBtn');
            const inputField = document.getElementById('incomeInput');

            // محاسبه هنگام کلیک دکمه
            btn.addEventListener('click', calculateSplit);

            // محاسبه با فشردن Enter در input
            inputField.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    event.preventDefault();
                    calculateSplit();
                }
            });

            // محاسبه اولیه با مقدار پیش‌فرض (1000)
            calculateSplit();
        };
    </script>
</body>
</html>
# 📄 Print Examples in PostScript via cURL

This file contains several sample financial receipts in PostScript format. Each one can be sent directly to the API using `curl`.

---

## 🧾 How to print

```bash
curl -X POST http://localhost:3000/print \
  -H "Content-Type: text/plain" \
  --data-binary "<POSTSCRIPT CONTENT>"
```

All examples must end with `showpage`.

---

## 💰 Credit Balance Summary

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary "%!PS
/Helvetica findfont 10 scalefont setfont
72 720 moveto (AMOUNT DUE: €150.00) show
0 -15 rmoveto (PAYMENT DUE DATE: 10/06/2025) show
0 -15 rmoveto (CREDIT LIMIT: €500.00) show
0 -15 rmoveto (AVAILABLE CREDIT: €380.00) show
0 -15 rmoveto (STATEMENT DATE: 25/05/2025) show
0 -15 rmoveto (ACCOUNT STATUS: ACTIVE) show
showpage"
```

---

## 💳 Mastercard Cash Advance

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary "%!PS
/Helvetica findfont 10 scalefont setfont
72 720 moveto (CUSTOMER: John Smith) show
0 -15 rmoveto (CARD: MASTERCARD XXXX-XXXX-XXXX-1234) show
0 -15 rmoveto (CASH WITHDRAWN: €200.00) show
0 -15 rmoveto (EUR USED: €80.00) show
0 -15 rmoveto (USD USED: $100.00) show
0 -15 rmoveto (EXPIRATION DATE: 31/12/2025) show
0 -15 rmoveto (TRANSACTION ID: ADV-88543) show
0 -15 rmoveto (AUTHORIZATION CODE: 349827) show
showpage"
```

---

## 🏧 Account Withdrawal

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary "%!PS
/Helvetica findfont 10 scalefont setfont
72 720 moveto (WITHDRAWAL FROM: SAVINGS ACCOUNT EUR) show
0 -15 rmoveto (BRANCH 0123   OP#: 4567   DATE: 27/05/2025   TIME: 15:30) show
0 -15 rmoveto (ACCOUNT HOLDER: John Smith) show
0 -15 rmoveto (ACCOUNT NUMBER: DE44500105175407324931) show
0 -15 rmoveto (CARD: XXXX-XXXX-XXXX-4321) show
0 -15 rmoveto (AMOUNT WITHDRAWN: €120.00) show
0 -15 rmoveto (CURRENCY RATE: 1 EUR = 1.08 USD) show
0 -15 rmoveto (ATM ID: ATM342) show
0 -15 rmoveto (SESSION ID: SESS92374) show
showpage"
```

---

## 📝 Notes

- Font used: Helvetica, size 10
- Output coordinates: top to bottom using `rmoveto`
- Output ends with `showpage` to trigger page rendering
- All values are in **EUR** instead of local currency

You can modify these templates to include barcodes, headers, or logos if needed.
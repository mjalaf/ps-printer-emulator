# 💶 ESC/POS Financial Receipt Examples

This document contains cURL commands using ESC/POS commands to simulate financial transactions such as credit balance, cash advances, and account withdrawals. All examples are in English and use EUR currency formatting.

---

## 💳 Credit Balance Summary

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1b\x61\x01Credit Summary\n\x1b\x61\x00Amount Due:        €150.00\nDue Date:          10/06/2025\nCredit Limit:      €500.00\nAvailable Credit:  €350.00\nStatement Date:    25/05/2025\nAccount Status:    ACTIVE\n\n\x1d\x56\x41\x10'
```

---

## 💰 Mastercard Cash Advance

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1b\x61\x01Cash Advance Receipt\n\x1b\x61\x00Client:            John Smith\nCard:              Mastercard ****1234\nWithdrawn Amount:  €200.00\nEUR Used:          €80.00\nUSD Used:          $100.00\nExpiration Date:   31/12/2025\nTransaction ID:    ADV-88543\nAuthorization:     349827\n\n\x1d\x56\x41\x10'
```

---

## 🏦 Account Withdrawal

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1b\x61\x01Account Withdrawal\n\x1b\x61\x00Type:        Savings EUR\nBranch:      0123   Op#: 4567\nDate/Time:   27/05/2025 15:30\nClient:      John Smith\nAccount:     DE44500105175407324931\nCard:        ****4321\nAmount:      €120.00\nRate:        1 EUR = 1.08 USD\nATM ID:      ATM342\nSession:     SESS92374\n\n\x1d\x56\x41\x10'
```

---

## 📌 Notes

- Commands start with `\x1b\x40` (reset).
- `\x1b\x61\x01` centers a line; `\x1b\x61\x00` left-aligns.
- Each line uses `\n` to print a new line.
- Ends with `\x1d\x56\x41\x10` to signal cut (used by emulators).
- Wrap `$'...'` syntax works in Bash to support binary-style escapes.

These examples simulate common financial receipt scenarios for testing ESC/POS printers or emulators.
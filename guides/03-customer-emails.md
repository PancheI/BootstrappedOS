# Head of Support: customer emails

**The emails every business needs, written as short notes from you.** Welcome, the follow-ups, failed payment, renewal notice, cancellation, win-back. You approve each one and set it up in your email tool.

## Set it up (30 minutes, once)
1. Type `/write-emails` and add your site's URL, for example `/write-emails https://yoursite.com`.

   **You should see** one draft per email: a subject that states the fact, a short preheader, 2-3 lines (under 80 words), one button and your first name. Under each: when it sends, when it stops, and the key that makes sure it sends only once.
2. Mark anything it asked you to confirm, fix it, and put the emails into your email tool (Mailchimp, Kit, Resend, Loops, or your shop platform).

## Every month (10 minutes)
1. Type `/write-emails review` and paste the emails you send today.

   **You should see** for each email: the word count, what to cut, and the line to replace.
2. Rewrite the one email that gets the fewest replies.

## What a good result looks like
```
Subject: Your card expired
Preheader: Your order still ships on Thursday.

I roast on Thursday. Update the card before then and your bag ships as usual.

[Update my card]
Ana
```
Trigger: payment failed. Stops when: the card is updated. Sent once per person, per order.

## One memory
It reads your voice from `knowledge/how-to/voice.md` and your customers from `knowledge/customers.md`, so the emails sound like your posts and replies.

## Avoid
- **A discount as the default save.** Ask why they're leaving first.
- **Long marketing emails.** One fact, one button.
- **Signing as "The Team".** Sign with your first name.

**Files behind this role:** `plugins/bootstrapped-os/agents/head-of-support.md`, `skills/customer-emails/` (templates in `skills/customer-emails/references/templates.md`), `commands/write-emails.md`

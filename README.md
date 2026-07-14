# Invensis Learning: Lifecycle Email Templates

Responsive, table-based HTML email templates for Invensis Learning, spanning the full
customer, learner, trainer, and internal-sales lifecycle. **46 templates across 7 flows.**

All templates are generated from a single source file, so copy and design never drift.

## Quick start

**Just want to look at the emails?**
Open `output/invensis-emails.html` in any browser. It is a self-contained gallery of all 46
templates with a **Copy HTML** button on each one that gives you the full standalone email.

**Want to change an email?**
1. Edit the relevant `em(id="...")` block in `src/generate_emails.py`
2. Rebuild:
   ```bash
   cd src
   python3 generate_emails.py
   ```
3. Open `output/invensis-emails.html` to review, then commit.

Requires Python 3 with no third-party packages for the build itself.

## Repo layout

```
invensis-emails/
├── README.md
├── .gitignore
├── src/
│   └── generate_emails.py     # single source of truth: all copy + the renderer
└── output/
    ├── invensis-emails.html   # gallery + copyable per-email HTML (open this)
    └── invensis-emails.md     # plain-text copy deck of every email
```

## The 7 flows

| Flow | Purpose | IDs |
|------|---------|-----|
| A | Enquiry & Purchase | A1–A9 |
| B | Certification Cohort | B1–B8 (B6.1–B6.6 = voucher reminder ladder) |
| C | Non-Certification Cohort | C1–C3 |
| D | Support Tickets | D1–D8 |
| E | Payment Recovery | E1–E4 |
| F | Trainer | F1–F4 |
| G | Internal Sales (alerts) | G1–G5 |

Each email's ID appears in the top-right corner of its card in the gallery. Use it to
reference a specific template when giving or logging feedback.

## Using git to track review feedback

The commit history is the change log. A good loop:

1. Open `output/invensis-emails.html` and review (with your CEO, or anyone).
2. For each requested change, edit `src/generate_emails.py`, rebuild, and commit:
   ```
   git commit -am "B8: soften exam-fail opening per CEO; advisor line stays"
   ```
   The message captures both *what* changed and *why*.
3. To trial risky changes without touching the approved set, branch first:
   ```
   git checkout -b ceo-review
   ```
   Merge it if approved, delete it if not.

`git log --oneline` then reads as your full change history.

## House rules baked into these templates

These conventions are applied throughout. Keep them when editing.

- **British English** (enrolment, programme, organise).
- **No em-dashes** anywhere in copy. Use commas, colons, or full stops.
- **No decorative emoji** in subjects or headlines.
- **Brand palette** (from the official Invensis PMP brochure): navy `#101030`,
  brochure blue `#018BD4`, action orange `#F8981C`. Every call-to-action button is orange.
- **Semantic colour** on hero washes and accents: blue = lifecycle, green = success,
  amber = action needed, red = failure / final notice, navy = internal & sensitive.
- **Legal entity:** Invensis Inc., 2785 Rockbrook Dr STE 204, Lewisville, TX 75067, USA.
- **Footer policy links** point to live URLs; marketing emails carry a preferences link,
  transactional emails do not require one.
- **No customer-facing advisor or trainer names** : those appear only in internal (F/G) emails.
- **Certificates are never gated behind feedback.** Feedback is requested, never required.
- **Nothing is "attached"** to emails : receipts and invoices live in the dashboard.

## Merge tokens

Templates use `{{double_brace}}` placeholders (e.g. `{{first_name}}`, `{{course_name}}`,
`{{order_id}}`, `{{decline_reason}}`). Swap the delimiter for your ESP if needed. Populate a
sensible fallback for `{{first_name}}` (such as "there") so subjects never render blank.

## Open items before sending

- Legal sign-off on the A4/A7 order-confirmation disclaimer wording (removed from body; confirm
  policy links cover it).
- Confirm the social handles in the footer point to the correct accounts.
- Confirm `{{dashboard_url}}` routes first-time recipients into a set-password flow (A1/A6 promise this).

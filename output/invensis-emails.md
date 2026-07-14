# Invensis Learning | Lifecycle Emails v3.0

Voice and visual system matched to the official Invensis PMP brochure.
46 templates across 7 flows. British English. HTML in `invensis-emails.html`.


---

## FLOW A. Enquiry & Purchase

### A1 | Your {{course_name}} brochure is ready, {{first_name}}

**From:** learn@invensislearning.com · **Trigger:** Brochure form submitted · **T+0**

**Subject:** Your {{course_name}} brochure is ready, {{first_name}}  
**Preview:** Full syllabus, accreditation route, and the next four cohort dates. All in your dashboard.

**WELCOME TO INVENSIS LEARNING**

###  Welcome, {{first_name}}

Thank you for your interest in {{course_name}}. You have taken an important first step, and your brochure is ready and waiting in your dashboard.

**What's inside**

1. **The full syllabus**: Every module, hour by hour, with the learning outcomes for each
2. **Your accreditation route**: What {{governing_body}} requires, and exactly where the exam sits
3. **Upcoming cohort dates**: The next four cohorts with timings in your timezone
4. **Where alumni went next**: Roles, salary movement, and the certifications people stacked on top

**[ Read the Brochure ]** → `{{dashboard_url}}`

_Set your password once to access the latest brochure anytime, no need to download it again_

> **Have a question the brochure doesn't answer?**
> Just reply to this email. A real person on our enrolment team reads every one, and we usually reply within four working hours. No question is too small.

Welcome aboard,
**The Invensis Learning Team**

### A2 | Welcome, {{first_name}}: let's talk about {{course_name}}

**From:** learn@invensislearning.com · **Trigger:** Individual enquiry submitted · **T+0**

**Subject:** Welcome, {{first_name}}: let's talk about {{course_name}}  
**Preview:** Thank you for reaching out. A training advisor will call you within one working day.

**WELCOME TO INVENSIS LEARNING**

###  Thank you for getting in touch, {{first_name}}

Thank you for enquiring about {{course_name}}, and welcome to Invensis Learning. Choosing a certification is an important decision, and we are here to help you make the right choice for your goals.

**Your enquiry**

| | |
|---|---|
| Reference | {{ticket_id}} |
| Course | {{course_name}} |
| Response by | 1 working day |

**What happens next**

1. **Within 1 working day**: A training advisor will call to talk through cohort options, the accreditation route, and pricing
2. **On that call**: Our advisors will guide you to the right option
3. **If it's a fit**: You'll get a written summary with the exact cohort, price, and what's included, so you can take it to your manager

**[ Book a Time That Suits You ]** → `{{booking_url}}`

_15 minutes · pick a slot · talk to a real advisor_

Kind regards,
**The Invensis Learning Team**

### A3 | Thanks {{first_name}}: let's plan your {{course_name}} training

**From:** learn@invensislearning.com · **Trigger:** Group enquiry submitted · **T+0**

**Subject:** Thanks {{first_name}}: let's plan your {{course_name}} training  
**Preview:** Welcome to Invensis Learning. A training advisor will be in touch within one working day.

**WELCOME TO INVENSIS LEARNING**

###  Thank you for thinking of us, {{first_name}}

Thank you for enquiring about {{course_name}} for your team, and welcome to Invensis Learning. Developing a team's capability together is one of the most valuable investments an organisation can make, and we would be glad to help you shape it properly.

**Your enquiry**

| | |
|---|---|
| Reference | {{ticket_id}} |
| Course | {{course_name}} |
| Response by | 1 working day |

**What we'll cover on the call**

1. **Team size and starting point**: How many learners, and how much they already know. This shapes the pacing more than anything else
2. **Private cohort or public seats**: Private gives you a tailored agenda. Public is quicker and lighter on budget
3. **Delivery format**: Live virtual classroom, on-site at your offices, or a blend of both
4. **Timelines and approvals**: When you need this live, and what has to be signed off internally to get there

**[ Book a Scoping Call ]** → `{{booking_url}}`

_30 minutes · no obligation · scoping only_

> **Need to get budget approved first?**
> Reply and we will send a one-page business case template your L&D or HR team can take to finance, at no cost.

Looking forward to working with you,
**The Corporate Training Team**

### A4 | Order {{order_id}} confirmed: here's what you've booked

**From:** billing@invensislearning.com · **Trigger:** Order created at checkout · **T+0**

**Subject:** Order {{order_id}} confirmed: here's what you've booked  
**Preview:** Your order summary. Payment is processing now; your receipt follows the moment it clears.

**ORDER CONFIRMED**

###  Welcome aboard, {{first_name}}

Thank you for choosing Invensis Learning. Here is exactly what you have booked. We are processing your payment now, and your receipt will follow as soon as it clears.

**Order summary**

| | |
|---|---|
| Order # | {{order_id}} |
| Course | {{course_name}} |
| Course code | {{course_code}} |
| Cohort | {{batch_code}} |
| Dates | {{batch_start_date}} to {{batch_end_date}} |
| Time | {{session_time}} {{timezone}} |
| Format | Live Virtual Classroom (via Zoom) |
| **Total** | **USD {{amount}}** |

**What happens next**

1. **Right now**: Payment processing. Your payment receipt is emailed the moment it clears
2. **Within 15 minutes**: Your dashboard opens with course materials and your cohort schedule
3. **Within 24 hours**: Calendar invites for every cohort session, sent to Google and Outlook
4. **7 days before kick-off**: Your pre-course preparation guide and checklist

**[ View My Order ]** → `{{dashboard_url}}/orders/{{order_id}}`

_Order #{{order_id}}_

> **About your invoice**
> Your payment receipt is issued as soon as payment clears. Your official invoice is provided after training completion, alongside your certificate, for employer reimbursement or tax purposes.

We look forward to supporting you,
**The Invensis Learning Team**

### A5 | Payment received: you're officially enrolled, {{first_name}}

**From:** billing@invensislearning.com · **Trigger:** Stripe payment_intent.succeeded · **T+0**

**Subject:** Payment received: you're officially enrolled, {{first_name}}  
**Preview:** Your seat in the {{batch_code}} cohort is locked. Your receipt is in your dashboard.

**ENROLMENT CONFIRMED**

###  You're officially in, {{first_name}}

Payment received. Your seat in the {{batch_start_date}} cohort is locked, and your payment receipt is now available in your dashboard.

**Payment receipt**

| | |
|---|---|
| Order # | {{order_id}} |
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Payment method | {{payment_method}} |
| Date | {{payment_date}} |
| **Total paid** | **USD {{amount}}** |

You've just joined thousands of professionals who started exactly where you are right now, at the moment they decided to back themselves.

**[ View Order & Download Receipt ]** → `{{invoice_url}}`

_Order #{{order_id}} · paid via {{payment_method}}_

> **Your official invoice comes later**
> This is your payment receipt. Your official invoice is provided after training completion, together with your certificate, so you can use it for employer reimbursement or tax filing.

Welcome aboard,
**The Invensis Learning Team**

### A6 | Welcome to {{course_name}}: set up your dashboard, {{first_name}}

**From:** learn@invensislearning.com · **Trigger:** Payment cleared · **T+15m**

**Subject:** Welcome to {{course_name}}: set up your dashboard, {{first_name}}  
**Preview:** Congratulations on enrolling. Everything for your course lives in one place. Set up your dashboard to access it.

**ENROLMENT COMPLETE**

###  Congratulations, {{first_name}}

You are now enrolled on {{course_name}}, and we are pleased to welcome you. Everything you need for your course lives in one place: your dashboard. Please take a moment to set it up, and from then on it is where you will manage your entire learning experience.

**[ Set Up My Dashboard ]** → `{{dashboard_url}}`

_Set your password once, then access everything below anytime_

**Everything you'll access in your dashboard**

1. **Course materials**: Pre-reading, slides, and resources for {{course_name}}
2. **Session details**: Your cohort schedule, timings, and your join link
3. **Payment receipt**: Your receipt now, and your official invoice after training completes
4. **Feedback forms**: Share a quick note each day to help shape your trainer's next session
5. **Support tickets**: Raise and track any reschedule, change, or query in one place

**Your cohort details**

| | |
|---|---|
| Course | {{course_name}} |
| Dates | {{batch_dates}} |
| Time | {{session_time}} {{timezone}} |
| Format | Live Virtual Classroom (via Zoom) |

We look forward to having you in the cohort,
**The Cohort Team**

### A7 | Order {{order_id}} confirmed: {{seat_count}} seats on {{course_name}}

**From:** billing@invensislearning.com · **Trigger:** Group order created · **T+0**

**Subject:** Order {{order_id}} confirmed: {{seat_count}} seats on {{course_name}}  
**Preview:** Your order summary for {{company}}. Payment is processing; the receipt follows on clearance.

**GROUP ORDER CONFIRMED**

###  Welcome aboard, {{company}}

Thank you for choosing Invensis Learning for your team, {{first_name}}. Here is exactly what you have booked. We are processing your payment now, and your receipt will follow as soon as it clears.

**Order summary**

| | |
|---|---|
| Order # | {{order_id}} |
| Organisation | {{company}} |
| Course | {{course_name}} |
| Seats | {{seat_count}} |
| Cohort | {{batch_code}} |
| Dates | {{batch_start_date}} to {{batch_end_date}} |
| Format | Live Virtual Classroom (via Zoom) |
| **Total** | **USD {{amount}}** |

**What happens next**

1. **Right now**: Payment processing. Your payment receipt is emailed the moment it clears
2. **Within 15 minutes**: Your administrator dashboard opens, where you add your learners
3. **As you add each learner**: They receive their own login, materials, and joining instructions automatically
4. **5 working days before kick-off**: Deadline to have every seat allocated

**[ View My Order ]** → `{{dashboard_url}}/orders/{{order_id}}`

_Order #{{order_id}} · {{seat_count}} seats_

> **About your invoice**
> Your payment receipt is issued as soon as payment clears. Your official invoice is provided after training completion, for employer reimbursement or tax purposes.

We look forward to supporting your team,
**The Corporate Training Team**

### A8 | Payment received: all {{seat_count}} seats are locked

**From:** billing@invensislearning.com · **Trigger:** Stripe success, group order · **T+0**

**Subject:** Payment received: all {{seat_count}} seats are locked  
**Preview:** Your receipt is in your dashboard. Add your learners next.

**SEATS CONFIRMED**

###  All {{seat_count}} seats are locked

Payment received, {{first_name}}. Every seat in the {{batch_code}} cohort is now held for {{company}}, and your payment receipt is now available in your dashboard.

**Payment receipt**

| | |
|---|---|
| Order # | {{order_id}} |
| Organisation | {{company}} |
| Course | {{course_name}} |
| Seats | {{seat_count}} |
| Payment method | {{payment_method}} |
| **Total paid** | **USD {{amount}}** |

**[ Add My Learners ]** → `{{dashboard_url}}/admin/learners`

_Each learner gets their own login automatically_

> **Please add everyone within 5 working days**
> Learners must be in the dashboard at least five working days before {{batch_start_date}} so we can issue their joining instructions on time. Unallocated seats may be released.

> **Your official invoice comes later**
> This is your payment receipt. The official invoice is provided after training completion, for employer reimbursement or tax filing.

Welcome aboard,
**The Corporate Training Team**

### A9 | {{first_name}}, add your {{seat_count}} learners

**From:** learn@invensislearning.com · **Trigger:** Payment cleared, group order · **T+15m**

**Subject:** {{first_name}}, add your {{seat_count}} learners  
**Preview:** Your administrator dashboard is live. Here's everything between now and your cohort.

**ADMINISTRATOR DASHBOARD LIVE**

###  Time to add your team, {{first_name}}

Your administrator dashboard for {{company}} is open. Your next step is to add your {{seat_count}} learners. Each one gets their own login, materials, and joining instructions automatically the moment you add them.

**[ Add My Learners ]** → `{{dashboard_url}}/admin/learners`

_{{seat_count}} seats to allocate · takes about 5 minutes_

**Your timeline**

1. **Right now**: Add your learners. Names and email addresses are all we need
2. **5 working days before kick-off**: Hard deadline for seat allocation. Unallocated seats may be released
3. **48 hours before kick-off**: Last point at which you can swap one named learner for another, free of charge
4. **After the cohort ends**: Certificates, session recordings, your official invoice, and a completion report for {{company}}

**What else is in your dashboard**

1. **Attendance and progress**: Live view across all {{seat_count}} learners
2. **Feedback overview**: See daily feedback across your learners, which helps us tailor each session
3. **Your payment receipt**: For order {{order_id}}. The official invoice follows after training completion

Looking forward to having your team in the cohort,
**The Cohort Team**


---

## FLOW B. Certification Cohort

### B1 | Three days to kick-off: your join link & prep guide

**From:** cohort@invensislearning.com · **Trigger:** 72 hours before cohort start · **T-3d**

**Subject:** Three days to kick-off: your join link & prep guide  
**Preview:** Your join link, the Day 1 schedule, and a five-minute checklist to show up ready.

**THREE DAYS TO GO**

###  Almost time, {{first_name}}

Your cohort begins on {{batch_start_date}} at {{session_time}} {{timezone}}. Here's everything you need so you can turn up relaxed and ready.

**[ Join My Cohort ]** → `{{zoom_url}}`

_Same link works for every cohort day · bookmark it now_

**Your five-minute checklist**

- [ ] **Check your internet connection**: This matters most for a live session. Use a wired cable or sit close to your router, and close other bandwidth-heavy apps before you join
- [ ] **Test your camera and microphone**: The 30-second test link is in your cohort hub. Headphones help avoid echo during discussions
- [ ] **Bookmark the join link**: The same link works every cohort day. Save it now so there's no scramble at 8:55 AM on Day 1
- [ ] **Set up in a quiet space**: You'll be in live discussion and breakout groups, not just listening, so somewhere you can speak freely helps
- [ ] **Block your calendar and grab a notepad**: {{session_time}} for every cohort day, no meetings or interruptions, and something to hand for the live exercises

**How the sessions run**

1. **Join five minutes early**: We start on time, every time
2. **Camera on where you can**: This is a workshop, not a webinar. The breakouts don't work without faces
3. **Ask in the moment**: Don't save questions for the end. The person next to you has the same one
4. **Mute when you're not speaking**: Two breaks and a lunch break each day

> **Please don't**
> Record the session, or share your join link outside your cohort. And try not to multitask through the exercises. They're where the learning actually happens.

> **Attendance and your certificate**
> Attendance across all cohort days is required for your certificate of participation. If something comes up, tell your cohort manager early rather than late.

See you on {{batch_start_date}},
**The Cohort Team**

### B2 | Action needed: register with {{governing_body}}

**From:** operations@invensislearning.com · **Trigger:** Ops console button · **MANUAL**

**Subject:** Action needed: register with {{governing_body}}  
**Preview:** You need your own account there before we can release your official study material.

**ACTION REQUIRED**

###  One account to create, {{first_name}}

To sit the {{course_name}} examination and access the official study material, you need your own account on the {{governing_body}} website. This takes about five minutes.

**[ Create My {{governing_body}} Account ]** → `{{governing_body_url}}`

_Free · about 5 minutes · do this before {{batch_start_date}}_

> **Use the same name and email you booked with**
> If they don't match, {{governing_body}} can't link your registration to your training. Your material stays locked and your exam booking gets delayed. This is the single most common hold-up we see.

**Then what**

1. **Reply with your registration ID**: Just hit reply and paste it in. No form to fill
2. **We link it to your cohort**: Usually within a few working hours
3. **Your official material unlocks**: Straight into your {{governing_body}} account

> **Stuck on their website?**
> It happens. Reply to this email and our operations team will walk you through it, or do it with you on a five-minute call.

We'll take it from there,
**The Operations Team**

### B3 | Day {{day_number}} recap: and two minutes, please

**From:** cohort@invensislearning.com · **Trigger:** Trainer marks day complete · **T+1h · repeats per day**

**Subject:** Day {{day_number}} recap: and two minutes, please  
**Preview:** What you covered today, tonight's recording, and a feedback form that reaches your trainer before tomorrow.

**DAY {{DAY_NUMBER}} COMPLETE**

###  Day {{day_number}} complete, {{first_name}}

Day {{day_number}} of {{course_name}} is complete. Here is what your trainer covered, and what is waiting for you this evening.

> **Today's topics**
> {{topics_covered}}

**Tonight, if you have twenty minutes**

1. **Skim the recording**: It's in your dashboard now. Jump to anything that felt shaky. That's the bit worth revisiting
2. **Download today's slides**: Same place. Annotate them while today is still fresh

**[ Give Feedback on Day {{day_number}} ]** → `{{feedback_url}}`

_2 minutes · reaches your trainer before tomorrow_

> **Why we ask**
> Your feedback goes to your trainer tonight, so it genuinely shapes tomorrow's session. It takes about two minutes, and it makes a real difference.

See you tomorrow,
**The Cohort Team**

### B4 | Cohort complete, {{first_name}}: download your certificate

**From:** cohort@invensislearning.com · **Trigger:** Final day marked complete · **T+2h**

**Subject:** Cohort complete, {{first_name}}: download your certificate  
**Preview:** Your certificate of completion, session recordings, and your official invoice are ready.

**COHORT COMPLETE**

###  You did it, {{first_name}}

You've completed {{course_name}}. That's {{total_hours}} hours of real work, alongside a full-time job and everything else. Most people who intend to do this never start. Plenty who start don't finish. You're in neither group.

**[ Download My Certificate ]** → `{{certificate_url}}`

_Signed PDF, ready now, yours to keep_

**What comes next**

1. **Your certificate of completion**: A signed PDF, ready to download. Save it for LinkedIn, your records, or employer reimbursement
2. **Your official invoice**: Available in your dashboard now that training is complete. Use it for reimbursement or tax filing
3. **Session recordings**: Shared by email within 48 hours. Revisit any topic at your own pace
4. **Your exam voucher**: Issued separately by our operations team. Watch for it

> **Book your exam early**
> Learners who book within three weeks of finishing pass at a substantially higher rate. The material is at its sharpest in your head right now, and it will not be in five months.

> **We'd value your feedback**
> If you have three minutes, your thoughts on the programme help us make it better for the next cohort. It's entirely optional, and genuinely appreciated.

One more thing: if the cohort was useful, would you consider leaving a short review? It helps the next person make the same decision you did.

Wishing you every success,
**The Cohort Team**

### B5 | Your exam voucher is here: valid until {{voucher_expiry}}

**From:** exams@invensislearning.com · **Trigger:** Voucher assigned in ops console · **MANUAL**

**Subject:** Your exam voucher is here: valid until {{voucher_expiry}}  
**Preview:** Voucher code inside. Six months of validity, and it goes faster than anyone expects.

**EXAM VOUCHER ISSUED**

###  The last mile, {{first_name}}

Your {{governing_body}} examination voucher has been issued. Everything you need is below.

**Your voucher**

| | |
|---|---|
| Voucher code | {{voucher_code}} |
| Examination | {{exam_name}} |
| Administered by | {{governing_body}} |
| Issued | {{voucher_issue_date}} |
| **Valid until** | **{{voucher_expiry}}** |

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots available 24/7 · no test centre needed_

> **Honest advice from our own data**
> Learners who book within three weeks of finishing training pass at a substantially higher rate than those who leave it. The material is fresh now. It will not be in five months. Book the slot and revise into it.

**Before you sit it**

1. **Take the practice test**: It's in your dashboard. Score above 70% and you're ready. Most people underestimate themselves here
2. **Check your tech**: Online proctoring needs a webcam, a clear desk, and a stable connection. Test it the day before
3. **Read {{governing_body}}'s rules**: ID requirements, what's allowed on your desk, and their reschedule policy

> **Six months, and no extensions**
> Your voucher expires on {{voucher_expiry}}. It cannot be extended, transferred, or refunded once issued. After that date you'd pay {{governing_body}} directly for a new attempt.

We are here to support you,
**The Certification Team**

### B6.1 | Your exam voucher is still unbooked, {{first_name}}

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Month 1**

**Subject:** Your exam voucher is still unbooked, {{first_name}}  
**Preview:** Five months of validity left, and the material is at its sharpest right now.

**FIVE MONTHS LEFT**

###  Right now, you know this material

Voucher {{voucher_code}} is still unbooked, and five months of validity remain. The strongest reason to book is one you won't have in five months' time: you finished training four weeks ago and it's all still in your head.

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

> **One more thing**
> That advantage decays quietly. You won't notice it going.

We're here if you need us,
**The Certification Team**

### B6.2 | Not booked yet? Here's what usually stops people

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Month 2**

**Subject:** Not booked yet? Here's what usually stops people  
**Preview:** Three common blockers, and exactly what to do about each one.

**FOUR MONTHS LEFT**

###  Three reasons people stall

Voucher {{voucher_code}} expires {{voucher_expiry}}. If you haven't booked yet, it's almost always one of three things. Here's what to do about each.

**And what to do about each**

1. **You don't feel ready**: Take the practice test in your dashboard. Score above 70% and book. Almost everyone underestimates themselves at this stage
2. **You can't find a slot that works**: {{governing_body}} runs online proctored exams around the clock, seven days a week. You do not need a test centre
3. **You simply haven't got to it**: Book the slot and revise into it. A fixed date does more for preparation than an open one ever will

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

We're here if you need us,
**The Certification Team**

### B6.3 | Halfway point on your exam voucher

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Month 3, halfway**

**Subject:** Halfway point on your exam voucher  
**Preview:** Three months left on {{voucher_code}}. Retention drops sharply past six months.

**THREE MONTHS LEFT**

###  Halfway point, {{first_name}}

Voucher {{voucher_code}} expires on {{voucher_expiry}}, three months from today. Retention on this material drops sharply past the six-month mark, and the learners who pass first time are, almost without exception, the ones who sat it early.

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

> **One more thing**
> Stuck on something specific? Reply and tell us what. We'll point you at the right revision resource, free.

Don't let this one go,
**The Certification Team**

### B6.4 | Two months left on voucher {{voucher_code}}

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Month 4**

**Subject:** Two months left on voucher {{voucher_code}}  
**Preview:** After {{voucher_expiry}} it cannot be extended, transferred, or refunded.

**TWO MONTHS LEFT**

###  Two months left, {{first_name}}

Two months of validity remain on voucher {{voucher_code}}. After {{voucher_expiry}} it expires and cannot be extended, transferred, or refunded.

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

> **One more thing**
> Replacing it means paying the full examination fee directly to {{governing_body}}.

Don't let this one go,
**The Certification Team**

### B6.5 | One month left: book now, sit later

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Month 5**

**Subject:** One month left: book now, sit later  
**Preview:** You don't need to sit it this month. You need to book it this month.

**ONE MONTH LEFT**

###  Book now. Sit later.

One month remains on voucher {{voucher_code}}. Here's the thing people miss: you don't need to sit the exam this month. You need to book it this month.

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

> **One more thing**
> As long as the booking is made before {{voucher_expiry}}, you're covered. Book a date six weeks out if you want to. Just book it.

Don't let this one go,
**The Certification Team**

### B6.6 | Final call: your voucher expires in 7 days

**From:** exams@invensislearning.com · **Trigger:** Voucher unredeemed · exits on booked or redeemed · **Final, T-7d**

**Subject:** Final call: your voucher expires in 7 days  
**Preview:** This is the last email you'll get about it.

**SEVEN DAYS LEFT**

###  Final call, {{first_name}}

Voucher {{voucher_code}} expires on {{voucher_expiry}}. That is seven days away, and once it's gone it's gone. Not extended, not refunded, not reissued. You'd pay {{governing_body}} directly for a new attempt.

**[ Book My Exam ]** → `{{exam_booking_url}}`

_Online proctored · slots 24/7 · voucher {{voucher_code}}_

> **One more thing**
> If something is genuinely blocking you, reply today and we'll see what can be done. After {{voucher_expiry}}, there's nothing we can do.

_This is the last reminder we'll send about this voucher._

Don't let this one go,
**The Certification Team**

### B7 | Congratulations, {{first_name}}: you passed {{exam_name}}

**From:** exams@invensislearning.com · **Trigger:** Result marked Pass · **MANUAL**

**Subject:** Congratulations, {{first_name}}: you passed {{exam_name}}  
**Preview:** {{exam_name}}, certified. Here's what to do with it this week.

**EXAMINATION PASSED**

###  Congratulations, {{first_name}}

You passed {{exam_name}}. This is a genuine achievement, earned through your own hard work, and you should take a moment to enjoy it.

**Your result**

| | |
|---|---|
| Examination | {{exam_name}} |
| Result | Pass |
| Score | {{exam_score}} |
| Date | {{result_date}} |
| Awarding body | {{governing_body}} |

> **Your official certificate comes from {{governing_body}}**
> They'll issue your certificate and digital badge directly, usually within {{cert_issue_days}} working days. It comes from them, not from us, so keep an eye on the inbox you registered with.

**Three things worth doing this week**

1. **Add it to LinkedIn while it's still news**: It gets seen, and it gets you approached. Certifications that stay quiet do nothing for you
2. **Tell your manager in writing**: One line on what you can now do that you couldn't before. Not the credential. The capability
3. **Decide what it unlocks**: The certificate isn't the return. What you now say yes to is the return

**[ See What's Next ]** → `{{dashboard_url}}/recommended`

_{{next_course_suggestion}} · alumni get {{alumni_discount}} off_

Quick favour: would you mind leaving a 60-second review? It helps the next person decide.

Congratulations once again,
**The Certification Team**

### B8 | About your {{exam_name}} result, {{first_name}}

**From:** exams@invensislearning.com · **Trigger:** Result marked Fail · **MANUAL**

**Subject:** About your {{exam_name}} result, {{first_name}}  
**Preview:** A setback, not a verdict. We'll stay with you all the way to certification, and an advisor will be in touch.

**YOUR EXAMINATION RESULT**

###  About your result, {{first_name}}

You didn't pass {{exam_name}} this time. That's a disappointing email to open, and there's no way to write it that changes that.

Here's what's also true. A first-attempt fail is common on this exam, and the great majority of people who resit go on to pass. The gap is usually narrow and specific, not broad.

And you are not doing this on your own. Your enrolment with us doesn't end at an exam result. We will stay with you all the way through to certification, and one of our training advisors will reach out shortly to help you plan your next step at a pace that suits you.

**Your result**

| | |
|---|---|
| Examination | {{exam_name}} |
| Attempt | {{attempt_number}} |
| Your score | {{exam_score}} |
| Pass mark | {{pass_mark}} |
| Weaker domains | {{weak_domains}} |

> **Your score report is the most useful thing you have right now**
> {{governing_body}} breaks the result down by domain. It tells you which two or three areas to work on, instead of making you revise everything again from scratch.

**How we'll support you from here**

1. **A training advisor will be in touch**: Someone from our team will contact you to talk through your options and next steps. No pressure, just support
2. **A free 30-minute review call**: Your trainer will go through your score report with you and build a focused revision plan, at no charge
3. **Your dashboard stays open**: Materials, recordings, and practice tests remain available to you

**[ Book a Review Call ]** → `{{review_booking_url}}`

_30 minutes · free · pick any time that suits_

Take a few days. Then let's look at the report together. We're with you until you have that certificate in hand.

We're not going anywhere,
**The Certification Team**


---

## FLOW C. Non-Certification Cohort

### C1 | Three days to kick-off: your join link & prep guide

**From:** cohort@invensislearning.com · **Trigger:** 72 hours before cohort start · **T-3d**

**Subject:** Three days to kick-off: your join link & prep guide  
**Preview:** Your join link, the Day 1 schedule, and one thing to bring that changes everything.

**THREE DAYS TO GO**

###  Almost time, {{first_name}}

Your cohort begins on {{batch_start_date}} at {{session_time}} {{timezone}}.

**[ Join My Cohort ]** → `{{zoom_url}}`

_Same link works for every cohort day · bookmark it now_

> **Bring a live problem from your own work**
> This is the single biggest predictor of who gets value from this course. Not a hypothetical. Something real, currently unsolved, that you'd like to leave with a plan for.

**Your five-minute checklist**

- [ ] **Check your internet connection**: This matters most for a live session. Use a wired cable or sit close to your router, and close other bandwidth-heavy apps before you join
- [ ] **Test your camera and microphone**: The 30-second test link is in your cohort hub. Headphones help avoid echo during discussions
- [ ] **Bookmark the join link**: The same link works every cohort day. Save it now so there's no scramble on Day 1
- [ ] **Set up in a quiet space**: You'll be in live discussion and breakout groups, not just listening, so somewhere you can speak freely helps
- [ ] **Block your calendar**: {{session_time}} for every cohort day. No meetings, no interruptions

**How the sessions run**

1. **Join five minutes early**: We start on time, every time
2. **Camera on where you can**: This is a workshop, not a webinar
3. **Ask in the moment**: The person next to you has the same question
4. **Mute when you're not speaking**: Two breaks and a lunch break each day

> **Please don't**
> Record the session or share your join link outside your cohort. Attendance across all days is required for your certificate of participation.

See you on {{batch_start_date}},
**The Cohort Team**

### C2 | Day {{day_number}} recap: and two minutes, please

**From:** cohort@invensislearning.com · **Trigger:** Trainer marks day complete · **T+1h · repeats per day**

**Subject:** Day {{day_number}} recap: and two minutes, please  
**Preview:** What you covered today, tonight's recording, and a feedback form that reaches your trainer before tomorrow.

**DAY {{DAY_NUMBER}} COMPLETE**

###  Day {{day_number}} complete, {{first_name}}

Day {{day_number}} of {{course_name}} is complete. Here is what your trainer covered, and what is waiting for you this evening.

> **Today's topics**
> {{topics_covered}}

**Tonight, if you have twenty minutes**

1. **Skim the recording**: It's in your dashboard now. Jump to anything that felt shaky
2. **Try one thing at work tomorrow**: Even a small one. The gap between knowing and doing closes with repetition, not with notes

**[ Give Feedback on Day {{day_number}} ]** → `{{feedback_url}}`

_2 minutes · reaches your trainer before tomorrow_

> **Why we ask**
> Your feedback goes to your trainer tonight, so it genuinely shapes tomorrow's session. It takes about two minutes, and it makes a real difference.

See you tomorrow,
**The Cohort Team**

### C3 | Cohort complete, {{first_name}}: download your certificate

**From:** cohort@invensislearning.com · **Trigger:** Final day marked complete · **T+2h**

**Subject:** Cohort complete, {{first_name}}: download your certificate  
**Preview:** Your certificate of completion, session recordings, and your official invoice are ready.

**COHORT COMPLETE**

###  You did it, {{first_name}}

You've completed {{course_name}}. The value of this isn't what you now know. It's what you do differently on Monday, when nobody's watching and there's no trainer in the room.

**[ Download My Certificate ]** → `{{certificate_url}}`

_Signed PDF, ready now, yours to keep_

**What comes next**

1. **Your certificate of completion**: A signed PDF, ready to download. Save it for LinkedIn, your records, or employer reimbursement
2. **Your official invoice**: Available in your dashboard now that training is complete. Use it for reimbursement or tax filing
3. **Session recordings**: Shared by email within 48 hours
4. **Apply one thing this week**: Pick the smallest idea from the cohort and use it before Friday. That's how it sticks

> **We'd value your feedback**
> If you have three minutes, your thoughts on the programme help us make it better for the next cohort. It's entirely optional, and genuinely appreciated.

> **Your support doesn't stop here**
> Reply to this email with any question about applying the material. Average reply in 4 hours. Alumni also get exclusive pricing on every other course in our catalogue.

Wishing you every success,
**The Cohort Team**


---

## FLOW D. Support Tickets

### D1 | Reschedule request received: ticket {{ticket_id}}

**From:** help@invensislearning.com · **Trigger:** Reschedule ticket created · **T+0**

**Subject:** Reschedule request received: ticket {{ticket_id}}  
**Preview:** Nothing has changed yet. Your current seat stays reserved until the new date is confirmed.

**RESCHEDULE REQUESTED**

###  We've got your request

Thanks {{first_name}}. We have your request to move {{course_name}} from the {{batch_code}} cohort.

**Your request**

| | |
|---|---|
| Ticket | {{ticket_id}} |
| Course | {{course_name}} |
| Current cohort | {{batch_code}} |
| Requested date | {{requested_date}} |
| Response by | 1 working day |

> **Nothing has changed yet**
> Your current seat in {{batch_code}} stays reserved until your new date is confirmed, so you are never at risk of losing your place.

**What happens next**

1. **Within 1 working day**: Operations checks availability on your requested cohort
2. **If it's available**: You get a confirmation with new dates, timings, and trainer. Your dashboard updates automatically
3. **If it's full**: We come back with the two closest alternatives and hold your current seat while you choose

**[ View My Ticket ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Add anything further, any time_

We'll sort it,
**The Cohort Team**

### D2 | Confirmed: you're now in the {{new_batch_code}} cohort

**From:** help@invensislearning.com · **Trigger:** Ops console button · **MANUAL**

**Subject:** Confirmed: you're now in the {{new_batch_code}} cohort  
**Preview:** New dates, same course. A fresh join link is on its way.

**RESCHEDULE CONFIRMED**

###  All moved, {{first_name}}

Your reschedule is confirmed and your dashboard has already updated.

**Your new cohort**

| | |
|---|---|
| Course | {{course_name}} |
| Was | {{batch_code}}, from {{batch_start_date}} |
| Now | {{new_batch_code}}, from {{new_batch_start_date}} |
| Time | {{new_session_time}} {{timezone}} |

> **Discard your old join link**
> It won't work. A fresh link and joining instructions arrive three days before {{new_batch_start_date}}.

**[ View My Cohort ]** → `{{dashboard_url}}`

_Updated schedule · materials · calendar invites_

See you there,
**The Cohort Team**

### D3 | Cancellation request received: ticket {{ticket_id}}

**From:** help@invensislearning.com · **Trigger:** Cancellation ticket created · **T+0**

**Subject:** Cancellation request received: ticket {{ticket_id}}  
**Preview:** Nothing has been cancelled yet. Here are your options before we process anything.

**CANCELLATION REQUESTED**

###  Before we proceed, {{first_name}}

We have received your request to cancel {{course_name}} ({{batch_code}}). Nothing has been cancelled yet, and no refund has been processed. One of our advisors will reach out to you shortly to talk it through.

**Your request**

| | |
|---|---|
| Ticket | {{ticket_id}} |
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Order | {{order_id}} |
| Response by | 1 working day |

> **One question, and it's a real one**
> If the issue is the dates rather than the course itself, a reschedule lets you keep your place and move to a date that works better. This isn't a retention tactic. It's often the simpler route for you than cancelling and rebooking later.

**If something else is in the way**

Pick whichever fits and reply, or use the button below.

**A.** **I just need a different date**: We can move you to another cohort. Reply and we'll talk through the available dates
**B.** **My employer pulled the budget**: Reply and we'll hold your seat for 60 days while you sort approvals
**C.** **I'm not sure this is the right course**: Book a free 15-minute call. Our advisors will guide you to the option that genuinely fits
**D.** **I want to go ahead and cancel**: No problem at all. One of our advisors will call to confirm the details with you, and then operations will process it

**[ View My Ticket ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Add anything you'd like us to know_

Whatever works for you,
**The Cohort Team**

### D4 | {{course_name}} cancelled: refund details inside

**From:** help@invensislearning.com · **Trigger:** Ops console button · **MANUAL**

**Subject:** {{course_name}} cancelled: refund details inside  
**Preview:** Your refund amount and timeline are confirmed below.

**CANCELLATION PROCESSED**

###  All done, {{first_name}}

Your booking for {{course_name}} ({{batch_code}}) has been cancelled. Here are the details.

**Refund summary**

| | |
|---|---|
| Order | {{order_id}} |
| Amount paid | USD {{amount}} |
| Refund due | USD {{refund_amount}} |
| Method | Original payment method |
| Expected by | {{refund_eta}} |

_{{refund_policy_note}}_

> **If you change your mind**
> If you decide to return within the next six months, we'll offer you this course at the same price you paid today, even if our prices have risen in the meantime. Just reply to this email.

**[ View My Ticket ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Ticket {{ticket_id}}_

The door stays open,
**The Cohort Team**

### D5 | Request to update your details: ticket {{ticket_id}}

**From:** help@invensislearning.com · **Trigger:** Details change ticket created · **T+0**

**Subject:** Request to update your details: ticket {{ticket_id}}  
**Preview:** We'll confirm within one working day.

**UPDATE REQUESTED**

###  We've got your request

Thanks {{first_name}}. We have your request to update the following on your booking for {{course_name}}.

> **What you asked us to change**
> {{requested_changes}}

**Your request**

| | |
|---|---|
| Ticket | {{ticket_id}} |
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Response by | 1 working day |

> **We may need to verify one thing**
> If the change affects the name printed on your certificate, or the email registered with {{governing_body}}, we'll ask you for a document to verify it. Better to catch it now than after the certificate is issued.

**[ View My Ticket ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Add anything further, any time_

We'll take it from here,
**The Cohort Team**

### D6 | Your details have been updated

**From:** help@invensislearning.com · **Trigger:** Ops console button · **MANUAL**

**Subject:** Your details have been updated  
**Preview:** Please check the spelling of your name carefully.

**DETAILS UPDATED**

###  All updated, {{first_name}}

Your booking has been updated. Here's exactly what changed.

> **What we changed**
> {{changes_applied_table}}

> **Please check the spelling of your name**
> It's what gets printed on your certificate, and correcting it after issue is slow and, with some accrediting bodies, chargeable. If anything above is wrong, reply to this email today.

**[ View My Details ]** → `{{dashboard_url}}/profile`

_Ticket {{ticket_id}} · closed_

Thanks for checking,
**The Cohort Team**

### D7 | We've received your concern: ticket {{ticket_id}}

**From:** help@invensislearning.com · **Trigger:** Training escalation ticket created · **T+0**

**Subject:** We've received your concern: ticket {{ticket_id}}  
**Preview:** We've taken this as a high priority and a programme manager is now on it.

**HIGH PRIORITY**

###  We're on this, {{first_name}}

Thanks for telling us, {{first_name}}. We've received your concern about {{course_name}} ({{batch_code}}) and taken it as a high priority.

**Your escalation**

| | |
|---|---|
| Ticket | {{ticket_id}} |
| Owner | {{escalation_owner}}, Programme Manager |
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Response by | 4 working hours |

> **You won't have to repeat yourself**
> Everything you sent us has been passed to {{escalation_owner}} in full. They'll have read it before they contact you.

**[ Add Anything Further ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Goes straight to {{escalation_owner}}_

_If this is urgent, reply to this email or call {{support_phone}}._

We'll make this right,
**The Cohort Team**

### D8 | Resolved: your concern about {{course_name}}

**From:** help@invensislearning.com · **Trigger:** Ops console button · **MANUAL**

**Subject:** Resolved: your concern about {{course_name}}  
**Preview:** What you raised, what we did, and what changes as a result.

**ESCALATION RESOLVED**

###  Sorted, {{first_name}}

Your escalation is closed. Here's the full picture, in case you want it on record.

**The resolution**

1. **What you raised**: {{issue_summary}}
2. **What we did**: {{resolution_summary}}
3. **What changes as a result**: {{corrective_action}}

**[ View My Ticket ]** → `{{dashboard_url}}/tickets/{{ticket_id}}`

_Ticket {{ticket_id}} · resolved_

Thanks for your patience,
**{{escalation_owner}}, Programme Manager**


---

## FLOW E. Payment Recovery

### E1 | Your payment didn't go through: let's fix it

**From:** help@invensislearning.com · **Trigger:** Stripe payment_intent.payment_failed · **T+5m**

**Subject:** Your payment didn't go through: let's fix it  
**Preview:** Don't worry, this happens. We've held your seat. One-click resume inside.

**PAYMENT SUPPORT**

###  A quick issue to resolve, {{first_name}}

We regret to inform you, {{first_name}}, that your payment could not be processed and the transaction has failed. We have held your {{batch_start_date}} cohort seat for the next 24 hours while you try again, and no charge has been made.

> **What your bank told us**
> {{decline_reason}}

> **What to try next**
> {{recommended_action}}

**Your payment**

| | |
|---|---|
| Order | {{order_id}} |
| Course | {{course_name}} |
| Amount | USD {{amount}} |

**[ Resume Checkout, 1 Click ]** → `{{retry_url}}`

_Your cart is saved · seat held 24 hrs · no re-entry needed_

> **Still stuck?**
> Reply to this email or call our payment team on {{support_phone}}. If the card isn't the problem, we can invoice your employer, take a bank transfer, or hold your seat while a purchase order clears. Just ask.

We've got you,
**The Payment Support Team**

### E2 | Your seat is still being held, {{first_name}}

**From:** help@invensislearning.com · **Trigger:** Still unpaid after 1 hour · **T+1h**

**Subject:** Your seat is still being held, {{first_name}}  
**Preview:** Your cart is intact, your price is locked, and one click puts you back at the payment step.

**CART HELD**

###  We saved your spot

Your cart is intact. Your price is unchanged. Your {{batch_start_date}} cohort seat is held for another 23 hours. One click and you're back at the payment step, exactly where you left off.

**Your saved cart**

| | |
|---|---|
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Seats | {{seat_count}} |
| Reason for decline | {{decline_reason}} |
| **Total due** | **USD {{amount}}** |

**[ Resume My Checkout ]** → `{{retry_url}}`

_Same cart · same price · same seat_

> **If your bank blocked it**
> A quick call to the number on the back of your card usually clears it inside two minutes. First-time payments to overseas training providers get flagged constantly. This is routine and not a reflection on you.

Here when you're ready,
**The Payment Support Team**

### E3 | {{first_name}}: four ways to complete your enrolment

**From:** help@invensislearning.com · **Trigger:** Still unpaid after 6 hours · **T+6h**

**Subject:** {{first_name}}: four ways to complete your enrolment  
**Preview:** If the card is the problem, it doesn't have to be. Corporate billing, bank transfer, or a call.

**ENROLMENT ASSISTANCE**

###  One of these will work

Order {{order_id}} is still unpaid and your held seat releases in 18 hours. If your card declined, here's the full menu. We accept whatever works for you.

**Four ways to pay**

Pick whichever fits and reply, or use the button below.

**A.** **Try the card again**: Bank blocks usually clear after one phone call. Same cart, same price, one click
**B.** **Bank transfer**: Payment receipt issued immediately. Official invoice provided after training completion
**C.** **Corporate or employer billing**: Reply with your billing contact and we'll arrange it. We'll also supply any sponsorship documentation your L&D or HR team needs, free
**D.** **Talk it through first**: Book a free 15-minute call. Our advisors will guide you to the right decision, even if that means a later cohort

**[ Resume My Checkout ]** → `{{retry_url}}`

_Same cart · same price · seat held 18 more hours_

> **Need a different cohort date?**
> The {{next_cohort_start}} cohort is also open at the same price. We can switch your cart across in one click. Just reply.

However works for you,
**The Enrolment Team**

### E4 | Final hour: your seat in {{batch_code}} releases today

**From:** help@invensislearning.com · **Trigger:** Still unpaid after 24 hours · **T+24h · final**

**Subject:** Final hour: your seat in {{batch_code}} releases today  
**Preview:** After this, we return it to general sale. This is the last automated email about this order.

**FINAL REMINDER**

###  Last call, {{first_name}}

This is the last email about your saved cart. Order {{order_id}} is still unpaid, and we're returning your held seat in the {{batch_code}} cohort to general sale today.

**What's being released**

| | |
|---|---|
| Order | {{order_id}} |
| Course | {{course_name}} |
| Cohort | {{batch_code}} |
| Seats remaining | {{seats_remaining}} |
| **Total due** | **USD {{amount}}** |

**[ Pay Now & Keep My Seat ]** → `{{retry_url}}`

_Direct payment link · bypasses the cart_

> **If the cohort fills before you get to this**
> It isn't the end. Reply to this email and we'll put you on the next cohort at exactly the same price. No penalty, no admin fee.

_This is the last automated email you'll receive about order {{order_id}}._

Here if you need us,
**The Payment Support Team**


---

## FLOW F. Trainer

### F1 | Cohort assigned: {{course_name}}, {{batch_code}}

**From:** operations@invensislearning.com · **Trigger:** Trainer assigned to cohort · **T+0**

**Subject:** Cohort assigned: {{course_name}}, {{batch_code}}  
**Preview:** Full brief, learner list, and materials inside.

**COHORT ASSIGNMENT**

###  {{learner_count}} learners are counting on this

Hi {{trainer_name}}. You've been allocated the following cohort. Everything you need is in the brief.

**Cohort details**

| | |
|---|---|
| Course | {{course_name}} ({{course_code}}) |
| Cohort | {{batch_code}} |
| Dates | {{batch_start_date}} to {{batch_end_date}} |
| Time | {{session_time}} {{timezone}} |
| Learners | {{learner_count}} |
| Client | {{company}} |
| Delivery | {{delivery_mode}} |
| Coordinator | {{ops_coordinator_name}} |

**[ Open Cohort Brief ]** → `{{trainer_portal_url}}/batches/{{batch_code}}`

_Learner list · agenda · deck · client notes_

**What's in the brief**

1. **The learner list**: Names, roles, and experience levels. Worth ten minutes before Day 1
2. **The agreed agenda**: Including anything {{company}} asked us to add or drop
3. **The deck and exercises**: Current version, already branded
4. **Client-specific notes**: Context from the sales conversation that didn't fit anywhere else

Thanks as always,
**The Operations Team**

### F2 | Tomorrow: {{batch_code}}, day {{day_number}}

**From:** operations@invensislearning.com · **Trigger:** 24 hours before each session day · **T-1d · per session**

**Subject:** Tomorrow: {{batch_code}}, day {{day_number}}  
**Preview:** Your host link, tomorrow's agenda, and today's learner feedback.

**TOMORROW'S SESSION**

###  Day {{day_number}} tomorrow

Hi {{trainer_name}}. {{batch_code}} day {{day_number}} runs on {{session_date}} at {{session_time}} {{timezone}}.

**[ Start Session as Host ]** → `{{zoom_host_url}}`

_Host link · do not share with learners_

**Tomorrow at a glance**

| | |
|---|---|
| Agenda | {{day_agenda}} |
| Learners registered | {{learner_count}} |
| Expected absences | {{known_absences}} |
| Yesterday's feedback score | {{feedback_score}} |

**Your pre-class checklist**

- [ ] **Check your internet connection**: A wired connection is best for hosting. Sit close to your router if not, and close other bandwidth-heavy apps before you start
- [ ] **Test your camera, microphone, and screen share**: Run through the host controls, and confirm your slides and any demo screens share cleanly
- [ ] **Have your materials and agenda open**: Slides, exercise files, and the agenda for day {{day_number}} ready before learners arrive
- [ ] **Set up in a quiet, well-lit space**: Headphones to avoid echo, and a plain background so learners stay focused on you
- [ ] **Prepare your breakout rooms**: If today uses group work, set the rooms up in advance so you're not doing it live
- [ ] **Keep the coordinator's number handy**: {{ops_coordinator_name}} is on standby if anything technical goes wrong at the start

> **Please join ten minutes early**
> Learners are told to arrive five minutes early. We'd rather they weren't sitting in an empty room wondering if they've got the right link.

Have a good session,
**The Operations Team**

### F3 | Two minutes: log day {{day_number}} for {{batch_code}}

**From:** operations@invensislearning.com · **Trigger:** 30 minutes after scheduled session end · **T+30m · per session**

**Subject:** Two minutes: log day {{day_number}} for {{batch_code}}  
**Preview:** It triggers the learner recap and records attendance. Please do it tonight.

**END OF DAY**

###  Two minutes, tonight

Hi {{trainer_name}}. Day {{day_number}} of {{batch_code}} has finished. Please log what you covered.

**[ Log Day {{day_number}} ]** → `{{trainer_portal_url}}/batches/{{batch_code}}/day/{{day_number}}`

_About 2 minutes · free text, no forms_

**This isn't admin for its own sake**

1. **It sends the recap**: Your {{learner_count}} learners get their day summary and feedback request within the hour
2. **It records attendance**: Each learner's attendance for day {{day_number}} is logged against their record
3. **It surfaces feedback**: Tonight's learner feedback lands in your inbox before tomorrow's session, not after

> **Tonight rather than tomorrow morning**
> The recap loses most of its value if it arrives after learners have gone to bed on Day {{day_number}} and woken up on Day {{next_day_number}}.

Thanks,
**The Operations Team**

### F4 | Reminder: day {{day_number}} topics for {{batch_code}}

**From:** operations@invensislearning.com · **Trigger:** Day still not logged · several hours after F3 · exits once logged · **Reminder**

**Subject:** Reminder: day {{day_number}} topics for {{batch_code}}  
**Preview:** We still need the topics you covered today. Log them in the dashboard, or just reply to this email.

**DAILY TOPICS REMINDER**

###  We still need day {{day_number}}, {{trainer_name}}

Hi {{trainer_name}}. We haven't yet received the topics you covered in day {{day_number}} of {{batch_code}}. Your {{learner_count}} learners are waiting on their recap, so a couple of minutes now makes a real difference to them.

**[ Log Day {{day_number}} in the Dashboard ]** → `{{trainer_portal_url}}/batches/{{batch_code}}/day/{{day_number}}`

_About 2 minutes · free text, no forms_

> **Short on time? Just reply to this email**
> If it's quicker for you, simply reply with the topics you covered today, in a few bullet points or a short paragraph. Our operations team will log them in the dashboard for you and send the learner recap on your behalf.

**Why we're chasing this**

1. **Your learners' recap is on hold**: The day summary and feedback request only go out once the topics are logged
2. **Attendance is recorded at the same time**: Day {{day_number}} attendance is captured when you log the session
3. **Tomorrow builds on today**: Learners revise best when the recap reaches them the same evening

> **If today's session didn't run**
> If day {{day_number}} was cancelled, postponed, or rescheduled, reply and let us know so we don't keep chasing, and so learners are informed correctly.

With thanks for your help,
**The Operations Team**


---

## FLOW G. Internal Sales

### G1 | [LEAD] {{full_name}}, {{company}} | {{course_name}} | score {{lead_score}}

**From:** alerts@invensislearning.com (no-reply) · **Trigger:** Lead routed to rep · To: {{sales_rep_email}} · **T+0**

**Subject:** [LEAD] {{full_name}}, {{company}} | {{course_name}} | score {{lead_score}}  
**Preview:** Assigned to you. The two-hour response clock has started.

**NEW LEAD ASSIGNED**

###  {{full_name}}, {{company}}

**Lead detail**

| | |
|---|---|
| Name | {{full_name}} |
| Company | {{company}} |
| Role | {{job_title}} |
| Email | {{email}} |
| Phone | {{phone}} |
| Interest | {{course_name}} |
| Type | {{lead_type}} |
| Seats | {{seat_count}} |
| Source | {{lead_source}} |
| **Lead score** | **{{lead_score}}** |

> **What they wrote**
> {{enquiry_message}}

**[ Open in CRM ]** → `{{crm_url}}`

_Log a call, email, or reassignment_

> **Two-hour response clock**
> If no activity is logged against this lead by {{escalation_time}}, it escalates to Jaya automatically. Logging a call attempt counts.

### G2 | [ESCALATED] Untouched 2 hrs: {{full_name}}, {{company}}

**From:** alerts@invensislearning.com (no-reply) · **Trigger:** No logged activity after 2 hours · To: {{sales_rep_email}} · Cc: Jaya · **T+2h**

**Subject:** [ESCALATED] Untouched 2 hrs: {{full_name}}, {{company}}  
**Preview:** No activity logged since assignment. Jaya is copied.

**ESCALATION**

###  No activity in two hours

The following lead has had no activity logged against it since it was assigned.

**Lead detail**

| | |
|---|---|
| Lead | {{full_name}}, {{company}} |
| Assigned | {{assigned_time}} to {{sales_rep_name}} |
| Interest | {{course_name}}, {{seat_count}} seat(s) |
| Source | {{lead_source}} |
| **Lead score** | **{{lead_score}}** |

**[ Open in CRM ]** → `{{crm_url}}`

_Log activity or request reassignment_

**Actions**

1. **{{sales_rep_name}}**: Log a call, an email, or a reassignment request within the next hour
2. **Jaya**: Reassign directly from the CRM record if {{sales_rep_name}} is unavailable

### G3 | [ACTION] {{full_name}} did not pass {{exam_name}}

**From:** alerts@invensislearning.com (no-reply) · **Trigger:** Result marked Fail · To: {{sales_rep_email}} · **T+0**

**Subject:** [ACTION] {{full_name}} did not pass {{exam_name}}  
**Preview:** Call within 48 hours. Do not lead with resit pricing.

**LEARNER DID NOT PASS**

###  {{full_name}}, {{company}}

**Result detail**

| | |
|---|---|
| Learner | {{full_name}} |
| Company | {{company}} |
| Course | {{course_name}}, {{batch_code}} |
| Trainer | {{trainer_name}} |
| Exam | {{exam_name}} |
| Attempt | {{attempt_number}} |
| Score | {{exam_score}} (pass mark {{pass_mark}}) |
| Weak domains | {{weak_domains}} |
| Result date | {{result_date}} |

> **The learner has already heard from us**
> They've received their result email, which offers a free 30-minute score-report review with {{trainer_name}}. Please do not be the second person to tell them.

> **How to handle this call**
> Call within 48 hours. Do not lead with resit pricing. Lead with the review call. Resit fees come up only if they raise it, or on a second contact. A learner who feels supported resits. A learner who feels sold to churns.

**[ Open in CRM ]** → `{{crm_url}}`

_Log the call outcome_

_If this learner is part of a group booking, {{company}} may have others in the same position. Check the cohort before you call the sponsor._

### G4 | [CANCEL] {{full_name}}, {{company}} | USD {{amount}} at risk

**From:** alerts@invensislearning.com (no-reply) · **Trigger:** D3 fires · To: {{sales_rep_email}} · **T+0**

**Subject:** [CANCEL] {{full_name}}, {{company}} | USD {{amount}} at risk  
**Preview:** Ticket {{ticket_id}}. Reschedule is still on the table.

**CANCELLATION REQUESTED**

###  USD {{amount}} at risk

**Ticket detail**

| | |
|---|---|
| Learner | {{full_name}} |
| Company | {{company}} |
| Course | {{course_name}}, {{batch_code}} |
| Order | {{order_id}} |
| Ticket | {{ticket_id}} |
| Raised | {{ticket_raised_time}} |
| Stated reason | {{cancellation_reason}} |
| **Value** | **USD {{amount}}** |

> **Your window is now**
> Operations reviews against the refund policy within one working day. The learner has already been offered a reschedule as an alternative. If you know this account and can find out what actually changed, do it before the refund is processed.

**[ Open Ticket ]** → `{{ops_url}}/tickets/{{ticket_id}}`

_Ticket {{ticket_id}}_

### G5 | [CHANGE] {{full_name}}, {{company}} | details update requested

**From:** alerts@invensislearning.com (no-reply) · **Trigger:** D5 fires · To: {{sales_rep_email}} · **T+0**

**Subject:** [CHANGE] {{full_name}}, {{company}} | details update requested  
**Preview:** FYI only. No action unless the change is material.

**DETAILS CHANGE REQUESTED**

###  {{full_name}}, {{company}}

**Ticket detail**

| | |
|---|---|
| Learner | {{full_name}} |
| Company | {{company}} |
| Course | {{course_name}}, {{batch_code}} |
| Ticket | {{ticket_id}} |
| Requested | {{requested_changes}} |

> **Operations handles this**
> No action needed from you unless the change is one of the three below.

**Worth a call if it's any of these**

1. **Substitution of the named learner**: Someone left, or someone was reassigned. Either way the account has moved
2. **Change of billing entity**: Usually means a restructure, an acquisition, or a budget moving departments
3. **Change of company**: The learner has left {{company}}. Both the account and the individual are now in play

**[ Open Ticket ]** → `{{ops_url}}/tickets/{{ticket_id}}`

_Ticket {{ticket_id}}_

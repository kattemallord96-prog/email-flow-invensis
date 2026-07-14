"""
Invensis Learning lifecycle emails v3.0
Voice + visual system matched to Post-Checkout_Email_Flows reference.
Emits gallery HTML (with per-email copyable source) + markdown copy deck.
"""
import html as _h, os, re

# ---- palette extracted from the official Invensis PMP brochure PDF
NAVY="#101030"; BLUE="#018BD4"; BLUE_D="#0a6aa8"; BLUE_W="#eef6fc"; ORANGE="#F8981C"; ORANGE_W="#fff7ec"
INK="#101030"; MUT="#6b7280"; SOFT="#374151"; RULE="#e5e7eb"; WASH="#f4f7fb"; PAPER="#ffffff"
# semantic accents (hero washes/eyebrows/icons keep meaning; CTA button is always brand orange)
VIO=BLUE; VIO_D=BLUE_D; VIO_W=BLUE_W                     # "primary/lifecycle" now brochure blue
GRN="#16a34a"; GRN_W="#f0fdf4"; GRN_D="#166534"
AMB="#d97706"; AMB_W="#fffbeb"; AMB_B="#fde68a"; AMB_D="#92400e"
RED="#dc2626"; RED_W="#fef2f2"; RED_D="#991b1b"
SLT=NAVY; SLT_W="#f0f1f6"

DISP="'Plus Jakarta Sans', system-ui, -apple-system, 'Segoe UI', sans-serif"   # brochure uses a bold sans, no serif
BODY="'Plus Jakarta Sans', system-ui, -apple-system, 'Segoe UI', sans-serif"
MONO="'SF Mono','Courier New',monospace"

# tuple = (accent, accent_dark, wash, border)
THEME={
 "violet":(BLUE,BLUE_D,BLUE_W,"#bae0f5"),   # lifecycle -> brochure blue
 "green": (GRN,GRN_D,GRN_W,"#bbf7d0"),
 "amber": (AMB,AMB_D,AMB_W,AMB_B),
 "red":   (RED,RED_D,RED_W,"#fecaca"),
 "slate": (NAVY,NAVY,SLT_W,"#d6d9e6"),
}
CTA_BG=ORANGE; CTA_TX=NAVY   # brochure action colour: orange button, navy label
ENTITY="Invensis Inc."
ADDR_LINE="Invensis Inc., 2785 Rockbrook Dr STE 204, Lewisville, TX 75067, United States"
COPYRIGHT="Copyright &copy; 2026 Invensis Inc. All rights reserved."
CONTACT_EMAIL="support@invensislearning.com"
# Emails that are marketing under CAN-SPAM/GDPR and must carry an unsubscribe/preferences control.
MARKETING={"A1","A2","A3","B6.1","B6.2","B6.3","B6.4","B6.5","B6.6","B7","E2","E3"}
# Internal alerts (G-flow) get a minimal internal footer, no consumer legal block.
PHONE_BLOCK=[
 ("USA/Canada","+1 470-260-0084"),("Switzerland","+41 22 518 20 42"),("Australia","+61 2 5300 2805"),
 ("Netherlands","+31 20 262 2348"),("Belgium","+32 2 585 31 34"),("Denmark","+32 2 585 31 34"),
 ("Poland","+48 91 883 47 51"),("UK","+44 20 3322 3280"),("India","+91 96202-00784"),
]
SOCIAL=[("LinkedIn","https://www.linkedin.com/company/invensis-learning","#0A66C2"),
        ("YouTube","https://www.youtube.com/@invensislearning","#FF0000"),
        ("X","https://x.com/invensislearn","#000000"),
        ("Facebook","https://www.facebook.com/invensislearning","#1877F2")]

def build_footer(e):
    """Branded footer. Marketing emails add preferences link; internal G-flow gets a lean footer."""
    is_marketing = e["id"] in MARKETING
    is_internal  = e["id"].startswith("G")
    # from-address for reply routing; support@ shown as public contact
    from_addr = re.sub(r"\s*\(no-reply\)","",e["sender"]).strip()

    if is_internal:
        return (f'<tr><td style="background:{NAVY};padding:18px 34px;font:400 11px/1.7 {BODY};color:#8f98c0;">'
                f'Internal notification from Invensis Inc. sales operations. Not for forwarding outside the team.<br>'
                f'Routed from <a href="mailto:{from_addr}" style="color:#aeb6d6;">{from_addr}</a>. '
                f'Reply-to <a href="mailto:operations@invensislearning.com" style="color:#aeb6d6;">operations@invensislearning.com</a>.'
                f'</td></tr>')

    # social icons row (navy footer)
    soc=""
    for name,url,col in SOCIAL:
        soc+=(f'<td style="padding:0 5px;"><a href="{url}" style="text-decoration:none;">'
              f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tbody><tr>'
              f'<td width="34" height="34" align="center" valign="middle" bgcolor="{col}" '
              f'style="border-radius:50%;font:700 13px/34px {BODY};color:#ffffff;">{name[0]}</td>'
              f'</tr></tbody></table></a></td>')

    # phone block, three-per-row
    ph=""
    for i in range(0,len(PHONE_BLOCK),3):
        chunk=PHONE_BLOCK[i:i+3]
        cells=" &nbsp;|&nbsp; ".join(f'<strong style="color:#c3c9dd;">{r}:</strong> {n}' for r,n in chunk)
        ph+=f'<div style="margin:0 0 4px;">{cells}</div>'

    legal_note = ("You're receiving this email because you created an account/enquired with Invensis Learning, "
                  "or you opted to receive email from Invensis Learning."
                  if is_marketing else
                  "This is a service email relating to your enrolment or enquiry with Invensis Inc.")

    return f'''<tr><td style="background:{NAVY};padding:30px 34px 26px;text-align:center;">
  <p style="margin:0 0 16px;font:700 15px/1.4 {BODY};color:#ffffff;">Connect with Invensis Learning</p>
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="margin:0 auto 20px;"><tbody><tr>{soc}</tr></tbody></table>
  <p style="margin:0 0 4px;font:400 12.5px/1.5 {BODY};color:#aeb6d6;">For any query, contact us at</p>
  <p style="margin:0 0 16px;font:600 13px/1.5 {BODY};"><a href="mailto:{CONTACT_EMAIL}" style="color:{ORANGE};text-decoration:none;">{CONTACT_EMAIL}</a></p>
  <div style="font:400 11px/1.7 {BODY};color:#8f98c0;max-width:470px;margin:0 auto 16px;">{ph}</div>
  <p style="margin:0 0 18px;font:400 11.5px/1.6 {BODY};color:#aeb6d6;">{ADDR_LINE}</p>
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tbody><tr><td height="1" style="background:#2a2a55;font-size:0;line-height:0;">&nbsp;</td></tr></tbody></table>
  <p style="margin:16px 0 12px;font:400 11px/1.9 {BODY};color:#8f98c0;">
    <a href="https://www.invensislearning.com/terms-and-conditions" style="color:#8f98c0;">Terms &amp; Conditions</a> &nbsp;|&nbsp;
    <a href="https://www.invensislearning.com/privacy-policy" style="color:#8f98c0;">Privacy Policy</a> &nbsp;|&nbsp;
    <a href="https://www.invensislearning.com/refund-policy" style="color:#8f98c0;">Refund Policy</a> &nbsp;|&nbsp;
    <a href="https://www.invensislearning.com/rescheduling-policy" style="color:#8f98c0;">Rescheduling Policy</a> &nbsp;|&nbsp;
    <a href="{{{{preferences_url}}}}" style="color:#8f98c0;text-decoration:underline;">Update email preferences</a></p>
  <p style="margin:0;font:400 10.5px/1.6 {BODY};color:#6f78a0;">{COPYRIGHT}<br>{legal_note}</p>
</td></tr>'''

# ---- block constructors
def eyebrow(t): return ("eyebrow",t)
def hero(emoji,label,head): return ("hero",(emoji,label,head))
def lead(t): return ("lead",t)
def p(t): return ("p",t)
def steps(title,items): return ("steps",(title,items))
def checks(title,items): return ("checks",(title,items))
def receipt(title,rows,total=None): return ("receipt",(title,rows,total))
def options(title,intro,items): return ("options",(title,intro,items))
def cta(label,url,sub): return ("cta",(label,url,sub))
def note(kind,title,body): return ("note",(kind,title,body))
def rule(): return ("rule",None)
def small(t): return ("small",t)
def signoff(line,team): return ("signoff",(line,team))
def disc(t): return ("disc",t)

E=[]
def em(**k):
    k.setdefault("feedback","")
    E.append(k)

# ======================================================= FLOW A
em(id="A1",flow="A. Enquiry &amp; Purchase",theme="violet",sender="learn@invensislearning.com",
   trigger="Brochure form submitted",timing="T+0",
   subject="Your {{course_name}} brochure is ready, {{first_name}}",
   preview="Full syllabus, accreditation route, and the next four cohort dates. All in your dashboard.",
   blocks=[
     hero("","Welcome to Invensis Learning",'Welcome, <em>{{first_name}}</em>'),
     lead("Thank you for your interest in {{course_name}}. You have taken an important first step, and your brochure is ready and waiting in your dashboard."),
     steps("What's inside",[
       ("The full syllabus","Every module, hour by hour, with the learning outcomes for each"),
       ("Your accreditation route","What {{governing_body}} requires, and exactly where the exam sits"),
       ("Upcoming cohort dates","The next four cohorts with timings in your timezone"),
       ("Where alumni went next","Roles, salary movement, and the certifications people stacked on top"),
     ]),
     cta("Read the Brochure","{{dashboard_url}}","Set your password once to access the latest brochure anytime, no need to download it again"),
     note("info","Have a question the brochure doesn't answer?","Just reply to this email. A real person on our enrolment team reads every one, and we usually reply within four working hours. No question is too small."),
     signoff("Welcome aboard,","The Invensis Learning Team"),
   ])

em(id="A2",flow="A. Enquiry &amp; Purchase",theme="violet",sender="learn@invensislearning.com",
   trigger="Individual enquiry submitted",timing="T+0",
   subject="Welcome, {{first_name}}: let's talk about {{course_name}}",
   preview="Thank you for reaching out. A training advisor will call you within one working day.",
   blocks=[
     hero("","Welcome to Invensis Learning",'Thank you for getting in touch, <em>{{first_name}}</em>'),
     lead("Thank you for enquiring about {{course_name}}, and welcome to Invensis Learning. Choosing a certification is an important decision, and we are here to help you make the right choice for your goals."),
     receipt("Your enquiry",[("Reference","{{ticket_id}}"),("Course","{{course_name}}"),("Response by","1 working day")]),
     steps("What happens next",[
       ("Within 1 working day","A training advisor will call to talk through cohort options, the accreditation route, and pricing"),
       ("On that call","Our advisors will guide you to the right option"),
       ("If it's a fit","You'll get a written summary with the exact cohort, price, and what's included, so you can take it to your manager"),
     ]),
     cta("Book a Time That Suits You","{{booking_url}}","15 minutes &middot; pick a slot &middot; talk to a real advisor"),
     signoff("Kind regards,","The Invensis Learning Team"),
   ])

em(id="A3",flow="A. Enquiry &amp; Purchase",theme="violet",sender="learn@invensislearning.com",
   trigger="Group enquiry submitted",timing="T+0",
   subject="Thanks {{first_name}}: let's plan your {{course_name}} training",
   preview="Welcome to Invensis Learning. A training advisor will be in touch within one working day.",
   blocks=[
     hero("","Welcome to Invensis Learning",'Thank you for thinking of us, <em>{{first_name}}</em>'),
     lead("Thank you for enquiring about {{course_name}} for your team, and welcome to Invensis Learning. Developing a team's capability together is one of the most valuable investments an organisation can make, and we would be glad to help you shape it properly."),
     receipt("Your enquiry",[("Reference","{{ticket_id}}"),("Course","{{course_name}}"),("Response by","1 working day")]),
     steps("What we'll cover on the call",[
       ("Team size and starting point","How many learners, and how much they already know. This shapes the pacing more than anything else"),
       ("Private cohort or public seats","Private gives you a tailored agenda. Public is quicker and lighter on budget"),
       ("Delivery format","Live virtual classroom, on-site at your offices, or a blend of both"),
       ("Timelines and approvals","When you need this live, and what has to be signed off internally to get there"),
     ]),
     cta("Book a Scoping Call","{{booking_url}}","30 minutes &middot; no obligation &middot; scoping only"),
     note("info","Need to get budget approved first?","Reply and we will send a one-page business case template your L&amp;D or HR team can take to finance, at no cost."),
     signoff("Looking forward to working with you,","The Corporate Training Team"),
   ])

em(id="A4",flow="A. Enquiry &amp; Purchase",theme="violet",sender="billing@invensislearning.com",
   trigger="Order created at checkout",timing="T+0",
   subject="Order {{order_id}} confirmed: here's what you've booked",
   preview="Your order summary. Payment is processing now; your receipt follows the moment it clears.",
   blocks=[
     hero("","Order Confirmed",'Welcome aboard, <em>{{first_name}}</em>'),
     lead("Thank you for choosing Invensis Learning. Here is exactly what you have booked. We are processing your payment now, and your receipt will follow as soon as it clears."),
     receipt("Order summary",[
       ("Order #","{{order_id}}"),("Course","{{course_name}}"),("Course code","{{course_code}}"),
       ("Cohort","{{batch_code}}"),("Dates","{{batch_start_date}} to {{batch_end_date}}"),
       ("Time","{{session_time}} {{timezone}}"),("Format","Live Virtual Classroom (via Zoom)"),
     ],("Total","USD {{amount}}")),
     steps("What happens next",[
       ("Right now","Payment processing. Your payment receipt is emailed the moment it clears"),
       ("Within 15 minutes","Your dashboard opens with course materials and your cohort schedule"),
       ("Within 24 hours","Calendar invites for every cohort session, sent to Google and Outlook"),
       ("7 days before kick-off","Your pre-course preparation guide and checklist"),
     ]),
     cta("View My Order","{{dashboard_url}}/orders/{{order_id}}","Order #{{order_id}}"),
     note("warn","About your invoice","Your <strong>payment receipt</strong> is issued as soon as payment clears. Your <strong>official invoice</strong> is provided after training completion, alongside your certificate, for employer reimbursement or tax purposes."),
     signoff("We look forward to supporting you,","The Invensis Learning Team"),
   ])

em(id="A5",flow="A. Enquiry &amp; Purchase",theme="green",sender="billing@invensislearning.com",
   trigger="Stripe payment_intent.succeeded",timing="T+0",
   subject="Payment received: you're officially enrolled, {{first_name}}",
   preview="Your seat in the {{batch_code}} cohort is locked. Your receipt is in your dashboard.",
   blocks=[
     hero("","Enrolment Confirmed",'You&rsquo;re officially <em>in</em>, {{first_name}}'),
     lead("Payment received. Your seat in the {{batch_start_date}} cohort is locked, and your payment receipt is now available in your dashboard."),
     receipt("Payment receipt",[("Order #","{{order_id}}"),("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Payment method","{{payment_method}}"),("Date","{{payment_date}}")],("Total paid","USD {{amount}}")),
     p("You've just joined thousands of professionals who started exactly where you are right now, at the moment they decided to back themselves."),
     cta("View Order &amp; Download Receipt","{{invoice_url}}","Order #{{order_id}} &middot; paid via {{payment_method}}"),
     note("info","Your official invoice comes later","This is your payment receipt. Your official invoice is provided after training completion, together with your certificate, so you can use it for employer reimbursement or tax filing."),
     signoff("Welcome aboard,","The Invensis Learning Team"),
   ])

em(id="A6",flow="A. Enquiry &amp; Purchase",theme="violet",sender="learn@invensislearning.com",
   trigger="Payment cleared",timing="T+15m",
   subject="Welcome to {{course_name}}: set up your dashboard, {{first_name}}",
   preview="Congratulations on enrolling. Everything for your course lives in one place. Set up your dashboard to access it.",
   blocks=[
     hero("","Enrolment Complete",'Congratulations, <em>{{first_name}}</em>'),
     lead("You are now enrolled on {{course_name}}, and we are pleased to welcome you. Everything you need for your course lives in one place: your dashboard. Please take a moment to set it up, and from then on it is where you will manage your entire learning experience."),
     cta("Set Up My Dashboard","{{dashboard_url}}","Set your password once, then access everything below anytime"),
     steps("Everything you'll access in your dashboard",[
       ("Course materials","Pre-reading, slides, and resources for {{course_name}}"),
       ("Session details","Your cohort schedule, timings, and your join link"),
       ("Payment receipt","Your receipt now, and your official invoice after training completes"),
       ("Feedback forms","Share a quick note each day to help shape your trainer's next session"),
       ("Support tickets","Raise and track any reschedule, change, or query in one place"),
     ]),
     receipt("Your cohort details",[("Course","{{course_name}}"),("Dates","{{batch_dates}}"),("Time","{{session_time}} {{timezone}}"),("Format","Live Virtual Classroom (via Zoom)")]),
     signoff("We look forward to having you in the cohort,","The Cohort Team"),
   ])

em(id="A7",flow="A. Enquiry &amp; Purchase",theme="violet",sender="billing@invensislearning.com",
   trigger="Group order created",timing="T+0",
   subject="Order {{order_id}} confirmed: {{seat_count}} seats on {{course_name}}",
   preview="Your order summary for {{company}}. Payment is processing; the receipt follows on clearance.",
   blocks=[
     hero("","Group Order Confirmed",'Welcome aboard, <em>{{company}}</em>'),
     lead("Thank you for choosing Invensis Learning for your team, {{first_name}}. Here is exactly what you have booked. We are processing your payment now, and your receipt will follow as soon as it clears."),
     receipt("Order summary",[
       ("Order #","{{order_id}}"),("Organisation","{{company}}"),("Course","{{course_name}}"),
       ("Seats","{{seat_count}}"),("Cohort","{{batch_code}}"),("Dates","{{batch_start_date}} to {{batch_end_date}}"),
       ("Format","Live Virtual Classroom (via Zoom)"),
     ],("Total","USD {{amount}}")),
     steps("What happens next",[
       ("Right now","Payment processing. Your payment receipt is emailed the moment it clears"),
       ("Within 15 minutes","Your administrator dashboard opens, where you add your learners"),
       ("As you add each learner","They receive their own login, materials, and joining instructions automatically"),
       ("5 working days before kick-off","Deadline to have every seat allocated"),
     ]),
     cta("View My Order","{{dashboard_url}}/orders/{{order_id}}","Order #{{order_id}} &middot; {{seat_count}} seats"),
     note("warn","About your invoice","Your <strong>payment receipt</strong> is issued as soon as payment clears. Your <strong>official invoice</strong> is provided after training completion, for employer reimbursement or tax purposes."),
     signoff("We look forward to supporting your team,","The Corporate Training Team"),
   ])

em(id="A8",flow="A. Enquiry &amp; Purchase",theme="green",sender="billing@invensislearning.com",
   trigger="Stripe success, group order",timing="T+0",
   subject="Payment received: all {{seat_count}} seats are locked",
   preview="Your receipt is in your dashboard. Add your learners next.",
   blocks=[
     hero("","Seats Confirmed",'All {{seat_count}} seats are <em>locked</em>'),
     lead("Payment received, {{first_name}}. Every seat in the {{batch_code}} cohort is now held for {{company}}, and your payment receipt is now available in your dashboard."),
     receipt("Payment receipt",[("Order #","{{order_id}}"),("Organisation","{{company}}"),("Course","{{course_name}}"),("Seats","{{seat_count}}"),("Payment method","{{payment_method}}")],("Total paid","USD {{amount}}")),
     cta("Add My Learners","{{dashboard_url}}/admin/learners","Each learner gets their own login automatically"),
     note("warn","Please add everyone within 5 working days","Learners must be in the dashboard at least five working days before {{batch_start_date}} so we can issue their joining instructions on time. Unallocated seats may be released."),
     note("info","Your official invoice comes later","This is your payment receipt. The official invoice is provided after training completion, for employer reimbursement or tax filing."),
     signoff("Welcome aboard,","The Corporate Training Team"),
   ])

em(id="A9",flow="A. Enquiry &amp; Purchase",theme="violet",sender="learn@invensislearning.com",
   trigger="Payment cleared, group order",timing="T+15m",
   subject="{{first_name}}, add your {{seat_count}} learners",
   preview="Your administrator dashboard is live. Here's everything between now and your cohort.",
   blocks=[
     hero("","Administrator Dashboard Live",'Time to add your <em>team</em>, {{first_name}}'),
     lead("Your administrator dashboard for {{company}} is open. Your next step is to add your {{seat_count}} learners. Each one gets their own login, materials, and joining instructions automatically the moment you add them."),
     cta("Add My Learners","{{dashboard_url}}/admin/learners","{{seat_count}} seats to allocate &middot; takes about 5 minutes"),
     steps("Your timeline",[
       ("Right now","Add your learners. Names and email addresses are all we need"),
       ("5 working days before kick-off","Hard deadline for seat allocation. Unallocated seats may be released"),
       ("48 hours before kick-off","Last point at which you can swap one named learner for another, free of charge"),
       ("After the cohort ends","Certificates, session recordings, your official invoice, and a completion report for {{company}}"),
     ]),
     steps("What else is in your dashboard",[
       ("Attendance and progress","Live view across all {{seat_count}} learners"),
       ("Feedback overview","See daily feedback across your learners, which helps us tailor each session"),
       ("Your payment receipt","For order {{order_id}}. The official invoice follows after training completion"),
     ]),
     signoff("Looking forward to having your team in the cohort,","The Cohort Team"),
   ])

# ======================================================= FLOW B
em(id="B1",flow="B. Certification Cohort",theme="violet",sender="cohort@invensislearning.com",
   trigger="72 hours before cohort start",timing="T&minus;3d",
   subject="Three days to kick-off: your join link &amp; prep guide",
   preview="Your join link, the Day 1 schedule, and a five-minute checklist to show up ready.",
   blocks=[
     hero("","Three Days to Go",'Almost <em>time</em>, {{first_name}}'),
     lead("Your cohort begins on {{batch_start_date}} at {{session_time}} {{timezone}}. Here's everything you need so you can turn up relaxed and ready."),
     cta("Join My Cohort","{{zoom_url}}","Same link works for every cohort day &middot; bookmark it now"),
     checks("Your five-minute checklist",[
       ("Check your internet connection","This matters most for a live session. Use a wired cable or sit close to your router, and close other bandwidth-heavy apps before you join"),
       ("Test your camera and microphone","The 30-second test link is in your cohort hub. Headphones help avoid echo during discussions"),
       ("Bookmark the join link","The same link works every cohort day. Save it now so there's no scramble at 8:55 AM on Day 1"),
       ("Set up in a quiet space","You'll be in live discussion and breakout groups, not just listening, so somewhere you can speak freely helps"),
       ("Block your calendar and grab a notepad","{{session_time}} for every cohort day, no meetings or interruptions, and something to hand for the live exercises"),
     ]),
     steps("How the sessions run",[
       ("Join five minutes early","We start on time, every time"),
       ("Camera on where you can","This is a workshop, not a webinar. The breakouts don't work without faces"),
       ("Ask in the moment","Don't save questions for the end. The person next to you has the same one"),
       ("Mute when you're not speaking","Two breaks and a lunch break each day"),
     ]),
     note("warn","Please don't","Record the session, or share your join link outside your cohort. And try not to multitask through the exercises. They're where the learning actually happens."),
     note("info","Attendance and your certificate","Attendance across all cohort days is required for your certificate of participation. If something comes up, tell your cohort manager early rather than late."),
     signoff("See you on {{batch_start_date}},","The Cohort Team"),
   ])

em(id="B2",flow="B. Certification Cohort",theme="amber",sender="operations@invensislearning.com",
   trigger="Ops console button",timing="MANUAL",
   subject="Action needed: register with {{governing_body}}",
   preview="You need your own account there before we can release your official study material.",
   blocks=[
     hero("","Action Required",'One account to <em>create</em>, {{first_name}}'),
     lead("To sit the {{course_name}} examination and access the official study material, you need your own account on the {{governing_body}} website. This takes about five minutes."),
     cta("Create My {{governing_body}} Account","{{governing_body_url}}","Free &middot; about 5 minutes &middot; do this before {{batch_start_date}}"),
     note("warn","Use the same name and email you booked with","If they don't match, {{governing_body}} can't link your registration to your training. Your material stays locked and your exam booking gets delayed. This is the single most common hold-up we see."),
     steps("Then what",[
       ("Reply with your registration ID","Just hit reply and paste it in. No form to fill"),
       ("We link it to your cohort","Usually within a few working hours"),
       ("Your official material unlocks","Straight into your {{governing_body}} account"),
     ]),
     note("info","Stuck on their website?","It happens. Reply to this email and our operations team will walk you through it, or do it with you on a five-minute call."),
     signoff("We'll take it from there,","The Operations Team"),
   ])

em(id="B3",flow="B. Certification Cohort",theme="violet",sender="cohort@invensislearning.com",
   trigger="Trainer marks day complete",timing="T+1h &middot; repeats per day",
   subject="Day {{day_number}} recap: and two minutes, please",
   preview="What you covered today, tonight's recording, and a feedback form that reaches your trainer before tomorrow.",
   blocks=[
     hero("","Day {{day_number}} Complete",'Day {{day_number}} <em>complete</em>, {{first_name}}'),
     lead("Day {{day_number}} of {{course_name}} is complete. Here is what your trainer covered, and what is waiting for you this evening."),
     note("info","Today's topics","{{topics_covered}}"),
     steps("Tonight, if you have twenty minutes",[
       ("Skim the recording","It's in your dashboard now. Jump to anything that felt shaky. That's the bit worth revisiting"),
       ("Download today's slides","Same place. Annotate them while today is still fresh"),
     ]),
     cta("Give Feedback on Day {{day_number}}","{{feedback_url}}","2 minutes &middot; reaches your trainer before tomorrow"),
     note("info","Why we ask","Your feedback goes to your trainer tonight, so it genuinely shapes tomorrow's session. It takes about two minutes, and it makes a real difference."),
     signoff("See you tomorrow,","The Cohort Team"),
   ])

em(id="B4",flow="B. Certification Cohort",theme="green",sender="cohort@invensislearning.com",
   trigger="Final day marked complete",timing="T+2h",
   subject="Cohort complete, {{first_name}}: download your certificate",
   preview="Your certificate of completion, session recordings, and your official invoice are ready.",
   blocks=[
     hero("","Cohort Complete",'You <em>did</em> it, {{first_name}}'),
     lead("You've completed {{course_name}}. That's {{total_hours}} hours of real work, alongside a full-time job and everything else. Most people who intend to do this never start. Plenty who start don't finish. You're in neither group."),
     cta("Download My Certificate","{{certificate_url}}","Signed PDF, ready now, yours to keep"),
     steps("What comes next",[
       ("Your certificate of completion","A signed PDF, ready to download. Save it for LinkedIn, your records, or employer reimbursement"),
       ("Your official invoice","Available in your dashboard now that training is complete. Use it for reimbursement or tax filing"),
       ("Session recordings","Shared by email within 48 hours. Revisit any topic at your own pace"),
       ("Your exam voucher","Issued separately by our operations team. Watch for it"),
     ]),
     note("info","Book your exam early","Learners who book within three weeks of finishing pass at a substantially higher rate. The material is at its sharpest in your head right now, and it will not be in five months."),
     note("info","We'd value your feedback","If you have three minutes, your thoughts on the programme help us make it better for the next cohort. It's entirely optional, and genuinely appreciated."),
     p('<strong>One more thing:</strong> if the cohort was useful, would you consider <a href="{{review_url}}" style="color:'+VIO+';font-weight:600;">leaving a short review</a>? It helps the next person make the same decision you did.'),
     signoff("Wishing you every success,","The Cohort Team"),
   ])

em(id="B5",flow="B. Certification Cohort",theme="amber",sender="exams@invensislearning.com",
   trigger="Voucher assigned in ops console",timing="MANUAL",
   subject="Your exam voucher is here: valid until {{voucher_expiry}}",
   preview="Voucher code inside. Six months of validity, and it goes faster than anyone expects.",
   blocks=[
     hero("","Exam Voucher Issued",'The last <em>mile</em>, {{first_name}}'),
     lead("Your {{governing_body}} examination voucher has been issued. Everything you need is below."),
     receipt("Your voucher",[("Voucher code","{{voucher_code}}"),("Examination","{{exam_name}}"),("Administered by","{{governing_body}}"),("Issued","{{voucher_issue_date}}")],("Valid until","{{voucher_expiry}}")),
     cta("Book My Exam","{{exam_booking_url}}","Online proctored &middot; slots available 24/7 &middot; no test centre needed"),
     note("info","Honest advice from our own data","Learners who book within three weeks of finishing training pass at a substantially higher rate than those who leave it. The material is fresh now. It will not be in five months. Book the slot and revise into it."),
     steps("Before you sit it",[
       ("Take the practice test","It's in your dashboard. Score above 70% and you're ready. Most people underestimate themselves here"),
       ("Check your tech","Online proctoring needs a webcam, a clear desk, and a stable connection. Test it the day before"),
       ("Read {{governing_body}}'s rules","ID requirements, what's allowed on your desk, and their reschedule policy"),
     ]),
     note("warn","Six months, and no extensions","Your voucher expires on {{voucher_expiry}}. It cannot be extended, transferred, or refunded once issued. After that date you'd pay {{governing_body}} directly for a new attempt."),
     signoff("We are here to support you,","The Certification Team"),
   ])

# ---- voucher ladder
_ladder=[
 ("B6.1","Month 1","violet","","Five Months Left",
  'Right now, you <em>know</em> this material',
  "Voucher {{voucher_code}} is still unbooked, and five months of validity remain. The strongest reason to book is one you won't have in five months' time: you finished training four weeks ago and it's all still in your head.",
  "That advantage decays quietly. You won't notice it going.",None),
 ("B6.2","Month 2","violet","","Four Months Left",
  'Three reasons people <em>stall</em>',
  "Voucher {{voucher_code}} expires {{voucher_expiry}}. If you haven't booked yet, it's almost always one of three things. Here's what to do about each.",
  None,
  [("You don't feel ready","Take the practice test in your dashboard. Score above 70% and book. Almost everyone underestimates themselves at this stage"),
   ("You can't find a slot that works","{{governing_body}} runs online proctored exams around the clock, seven days a week. You do not need a test centre"),
   ("You simply haven't got to it","Book the slot and revise into it. A fixed date does more for preparation than an open one ever will")]),
 ("B6.3","Month 3, halfway","amber","","Three Months Left",
  'Halfway <em>point</em>, {{first_name}}',
  "Voucher {{voucher_code}} expires on {{voucher_expiry}}, three months from today. Retention on this material drops sharply past the six-month mark, and the learners who pass first time are, almost without exception, the ones who sat it early.",
  "Stuck on something specific? Reply and tell us what. We'll point you at the right revision resource, free.",None),
 ("B6.4","Month 4","amber","","Two Months Left",
  'Two months <em>left</em>, {{first_name}}',
  "Two months of validity remain on voucher {{voucher_code}}. After {{voucher_expiry}} it expires and cannot be extended, transferred, or refunded.",
  "Replacing it means paying the full examination fee directly to {{governing_body}}.",None),
 ("B6.5","Month 5","amber","","One Month Left",
  'Book now. Sit <em>later</em>.',
  "One month remains on voucher {{voucher_code}}. Here's the thing people miss: you don't need to <em>sit</em> the exam this month. You need to <em>book</em> it this month.",
  "As long as the booking is made before {{voucher_expiry}}, you're covered. Book a date six weeks out if you want to. Just book it.",None),
 ("B6.6","Final, T&minus;7d","red","","Seven Days Left",
  'Final <em>call</em>, {{first_name}}',
  "Voucher {{voucher_code}} expires on {{voucher_expiry}}. That is seven days away, and once it's gone it's gone. Not extended, not refunded, not reissued. You'd pay {{governing_body}} directly for a new attempt.",
  "If something is genuinely blocking you, reply today and we'll see what can be done. After {{voucher_expiry}}, there's nothing we can do.",None),
]
_subj={
 "B6.1":"Your exam voucher is still unbooked, {{first_name}}",
 "B6.2":"Not booked yet? Here's what usually stops people",
 "B6.3":"Halfway point on your exam voucher",
 "B6.4":"Two months left on voucher {{voucher_code}}",
 "B6.5":"One month left: book now, sit later",
 "B6.6":"Final call: your voucher expires in 7 days",
}
_prev={
 "B6.1":"Five months of validity left, and the material is at its sharpest right now.",
 "B6.2":"Three common blockers, and exactly what to do about each one.",
 "B6.3":"Three months left on {{voucher_code}}. Retention drops sharply past six months.",
 "B6.4":"After {{voucher_expiry}} it cannot be extended, transferred, or refunded.",
 "B6.5":"You don't need to sit it this month. You need to book it this month.",
 "B6.6":"This is the last email you'll get about it.",
}
for _id,_lbl,_th,_emo,_eye,_head,_body1,_body2,_opts in _ladder:
    blocks=[hero(_emo,_eye,_head), lead(_body1)]
    if _opts: blocks.append(steps("And what to do about each",_opts))
    blocks.append(cta("Book My Exam","{{exam_booking_url}}","Online proctored &middot; slots 24/7 &middot; voucher {{voucher_code}}"))
    if _body2: blocks.append(note("warn" if _th!="violet" else "info","One more thing",_body2))
    if _id=="B6.6": blocks.append(small("This is the last reminder we'll send about this voucher."))
    blocks.append(signoff("We're here if you need us," if _th=="violet" else "Don't let this one go,","The Certification Team"))
    em(id=_id,flow="B. Certification Cohort",theme=_th,sender="exams@invensislearning.com",
       trigger="Voucher unredeemed &middot; exits on booked or redeemed",timing=_lbl,
       subject=_subj[_id],preview=_prev[_id],blocks=blocks)

em(id="B7",flow="B. Certification Cohort",theme="green",sender="exams@invensislearning.com",
   trigger="Result marked Pass",timing="MANUAL",
   subject="Congratulations, {{first_name}}: you passed {{exam_name}}",
   preview="{{exam_name}}, certified. Here's what to do with it this week.",
   blocks=[
     hero("","Examination Passed",'Congratulations, <em>{{first_name}}</em>'),
     lead("You passed {{exam_name}}. This is a genuine achievement, earned through your own hard work, and you should take a moment to enjoy it."),
     receipt("Your result",[("Examination","{{exam_name}}"),("Result","Pass"),("Score","{{exam_score}}"),("Date","{{result_date}}"),("Awarding body","{{governing_body}}")]),
     note("info","Your official certificate comes from {{governing_body}}","They'll issue your certificate and digital badge directly, usually within {{cert_issue_days}} working days. It comes from them, not from us, so keep an eye on the inbox you registered with."),
     steps("Three things worth doing this week",[
       ("Add it to LinkedIn while it's still news","It gets seen, and it gets you approached. Certifications that stay quiet do nothing for you"),
       ("Tell your manager in writing","One line on what you can now do that you couldn't before. Not the credential. The capability"),
       ("Decide what it unlocks","The certificate isn't the return. What you now say yes to is the return"),
     ]),
     cta("See What's Next","{{dashboard_url}}/recommended","{{next_course_suggestion}} &middot; alumni get {{alumni_discount}} off"),
     p('<strong>Quick favour:</strong> would you mind <a href="{{review_url}}" style="color:'+GRN+';font-weight:600;">leaving a 60-second review</a>? It helps the next person decide.'),
     signoff("Congratulations once again,","The Certification Team"),
   ])

em(id="B8",flow="B. Certification Cohort",theme="slate",sender="exams@invensislearning.com",
   trigger="Result marked Fail",timing="MANUAL",
   subject="About your {{exam_name}} result, {{first_name}}",
   preview="A setback, not a verdict. We'll stay with you all the way to certification, and an advisor will be in touch.",
   blocks=[
     hero("","Your Examination Result",'About your <em>result</em>, {{first_name}}'),
     lead("You didn't pass {{exam_name}} this time. That's a disappointing email to open, and there's no way to write it that changes that."),
     p("Here's what's also true. A first-attempt fail is common on this exam, and the great majority of people who resit go on to pass. The gap is usually narrow and specific, not broad."),
     p("And you are not doing this on your own. Your enrolment with us doesn't end at an exam result. We will stay with you all the way through to certification, and one of our training advisors will reach out shortly to help you plan your next step at a pace that suits you."),
     receipt("Your result",[("Examination","{{exam_name}}"),("Attempt","{{attempt_number}}"),("Your score","{{exam_score}}"),("Pass mark","{{pass_mark}}"),("Weaker domains","{{weak_domains}}")]),
     note("info","Your score report is the most useful thing you have right now","{{governing_body}} breaks the result down by domain. It tells you which two or three areas to work on, instead of making you revise everything again from scratch."),
     steps("How we'll support you from here",[
       ("A training advisor will be in touch","Someone from our team will contact you to talk through your options and next steps. No pressure, just support"),
       ("A free 30-minute review call","Your trainer will go through your score report with you and build a focused revision plan, at no charge"),
       ("Your dashboard stays open","Materials, recordings, and practice tests remain available to you"),
     ]),
     cta("Book a Review Call","{{review_booking_url}}","30 minutes &middot; free &middot; pick any time that suits"),
     p("Take a few days. Then let's look at the report together. We're with you until you have that certificate in hand."),
     signoff("We're not going anywhere,","The Certification Team"),
   ])

# ======================================================= FLOW C
em(id="C1",flow="C. Non-Certification Cohort",theme="violet",sender="cohort@invensislearning.com",
   trigger="72 hours before cohort start",timing="T&minus;3d",
   subject="Three days to kick-off: your join link &amp; prep guide",
   preview="Your join link, the Day 1 schedule, and one thing to bring that changes everything.",
   blocks=[
     hero("","Three Days to Go",'Almost <em>time</em>, {{first_name}}'),
     lead("Your cohort begins on {{batch_start_date}} at {{session_time}} {{timezone}}."),
     cta("Join My Cohort","{{zoom_url}}","Same link works for every cohort day &middot; bookmark it now"),
     note("info","Bring a live problem from your own work","This is the single biggest predictor of who gets value from this course. Not a hypothetical. Something real, currently unsolved, that you'd like to leave with a plan for."),
     checks("Your five-minute checklist",[
       ("Check your internet connection","This matters most for a live session. Use a wired cable or sit close to your router, and close other bandwidth-heavy apps before you join"),
       ("Test your camera and microphone","The 30-second test link is in your cohort hub. Headphones help avoid echo during discussions"),
       ("Bookmark the join link","The same link works every cohort day. Save it now so there's no scramble on Day 1"),
       ("Set up in a quiet space","You'll be in live discussion and breakout groups, not just listening, so somewhere you can speak freely helps"),
       ("Block your calendar","{{session_time}} for every cohort day. No meetings, no interruptions"),
     ]),
     steps("How the sessions run",[
       ("Join five minutes early","We start on time, every time"),
       ("Camera on where you can","This is a workshop, not a webinar"),
       ("Ask in the moment","The person next to you has the same question"),
       ("Mute when you're not speaking","Two breaks and a lunch break each day"),
     ]),
     note("warn","Please don't","Record the session or share your join link outside your cohort. Attendance across all days is required for your certificate of participation."),
     signoff("See you on {{batch_start_date}},","The Cohort Team"),
   ])

em(id="C2",flow="C. Non-Certification Cohort",theme="violet",sender="cohort@invensislearning.com",
   trigger="Trainer marks day complete",timing="T+1h &middot; repeats per day",
   subject="Day {{day_number}} recap: and two minutes, please",
   preview="What you covered today, tonight's recording, and a feedback form that reaches your trainer before tomorrow.",
   blocks=[
     hero("","Day {{day_number}} Complete",'Day {{day_number}} <em>complete</em>, {{first_name}}'),
     lead("Day {{day_number}} of {{course_name}} is complete. Here is what your trainer covered, and what is waiting for you this evening."),
     note("info","Today's topics","{{topics_covered}}"),
     steps("Tonight, if you have twenty minutes",[
       ("Skim the recording","It's in your dashboard now. Jump to anything that felt shaky"),
       ("Try one thing at work tomorrow","Even a small one. The gap between knowing and doing closes with repetition, not with notes"),
     ]),
     cta("Give Feedback on Day {{day_number}}","{{feedback_url}}","2 minutes &middot; reaches your trainer before tomorrow"),
     note("info","Why we ask","Your feedback goes to your trainer tonight, so it genuinely shapes tomorrow's session. It takes about two minutes, and it makes a real difference."),
     signoff("See you tomorrow,","The Cohort Team"),
   ])

em(id="C3",flow="C. Non-Certification Cohort",theme="green",sender="cohort@invensislearning.com",
   trigger="Final day marked complete",timing="T+2h",
   subject="Cohort complete, {{first_name}}: download your certificate",
   preview="Your certificate of completion, session recordings, and your official invoice are ready.",
   blocks=[
     hero("","Cohort Complete",'You <em>did</em> it, {{first_name}}'),
     lead("You've completed {{course_name}}. The value of this isn't what you now know. It's what you do differently on Monday, when nobody's watching and there's no trainer in the room."),
     cta("Download My Certificate","{{certificate_url}}","Signed PDF, ready now, yours to keep"),
     steps("What comes next",[
       ("Your certificate of completion","A signed PDF, ready to download. Save it for LinkedIn, your records, or employer reimbursement"),
       ("Your official invoice","Available in your dashboard now that training is complete. Use it for reimbursement or tax filing"),
       ("Session recordings","Shared by email within 48 hours"),
       ("Apply one thing this week","Pick the smallest idea from the cohort and use it before Friday. That's how it sticks"),
     ]),
     note("info","We'd value your feedback","If you have three minutes, your thoughts on the programme help us make it better for the next cohort. It's entirely optional, and genuinely appreciated."),
     note("info","Your support doesn't stop here","Reply to this email with any question about applying the material. Average reply in 4 hours. Alumni also get exclusive pricing on every other course in our catalogue."),
     signoff("Wishing you every success,","The Cohort Team"),
   ])

# ======================================================= FLOW D
em(id="D1",flow="D. Support Tickets",theme="violet",sender="help@invensislearning.com",
   trigger="Reschedule ticket created",timing="T+0",
   subject="Reschedule request received: ticket {{ticket_id}}",
   preview="Nothing has changed yet. Your current seat stays reserved until the new date is confirmed.",
   blocks=[
     hero("","Reschedule Requested",'We&rsquo;ve got your <em>request</em>'),
     lead("Thanks {{first_name}}. We have your request to move {{course_name}} from the {{batch_code}} cohort."),
     receipt("Your request",[("Ticket","{{ticket_id}}"),("Course","{{course_name}}"),("Current cohort","{{batch_code}}"),("Requested date","{{requested_date}}"),("Response by","1 working day")]),
     note("info","Nothing has changed yet","Your current seat in {{batch_code}} stays reserved until your new date is confirmed, so you are never at risk of losing your place."),
     steps("What happens next",[
       ("Within 1 working day","Operations checks availability on your requested cohort"),
       ("If it's available","You get a confirmation with new dates, timings, and trainer. Your dashboard updates automatically"),
       ("If it's full","We come back with the two closest alternatives and hold your current seat while you choose"),
     ]),
     cta("View My Ticket","{{dashboard_url}}/tickets/{{ticket_id}}","Add anything further, any time"),
     signoff("We'll sort it,","The Cohort Team"),
   ])

em(id="D2",flow="D. Support Tickets",theme="green",sender="help@invensislearning.com",
   trigger="Ops console button",timing="MANUAL",
   subject="Confirmed: you're now in the {{new_batch_code}} cohort",
   preview="New dates, same course. A fresh join link is on its way.",
   blocks=[
     hero("","Reschedule Confirmed",'All <em>moved</em>, {{first_name}}'),
     lead("Your reschedule is confirmed and your dashboard has already updated."),
     receipt("Your new cohort",[("Course","{{course_name}}"),("Was","{{batch_code}}, from {{batch_start_date}}"),("Now","{{new_batch_code}}, from {{new_batch_start_date}}"),("Time","{{new_session_time}} {{timezone}}")]),
     note("warn","Discard your old join link","It won't work. A fresh link and joining instructions arrive three days before {{new_batch_start_date}}."),
     cta("View My Cohort","{{dashboard_url}}","Updated schedule &middot; materials &middot; calendar invites"),
     signoff("See you there,","The Cohort Team"),
   ])

em(id="D3",flow="D. Support Tickets",theme="amber",sender="help@invensislearning.com",
   trigger="Cancellation ticket created",timing="T+0",
   subject="Cancellation request received: ticket {{ticket_id}}",
   preview="Nothing has been cancelled yet. Here are your options before we process anything.",
   blocks=[
     hero("","Cancellation Requested",'Before we <em>proceed</em>, {{first_name}}'),
     lead("We have received your request to cancel {{course_name}} ({{batch_code}}). Nothing has been cancelled yet, and no refund has been processed. One of our advisors will reach out to you shortly to talk it through."),
     receipt("Your request",[("Ticket","{{ticket_id}}"),("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Order","{{order_id}}"),("Response by","1 working day")]),
     note("info","One question, and it's a real one","If the issue is the dates rather than the course itself, a reschedule lets you keep your place and move to a date that works better. This isn't a retention tactic. It's often the simpler route for you than cancelling and rebooking later."),
     options("If something else is in the way","Pick whichever fits and reply, or use the button below.",[
       ("A","I just need a different date","We can move you to another cohort. Reply and we'll talk through the available dates"),
       ("B","My employer pulled the budget","Reply and we'll hold your seat for 60 days while you sort approvals"),
       ("C","I'm not sure this is the right course","Book a free 15-minute call. Our advisors will guide you to the option that genuinely fits"),
       ("D","I want to go ahead and cancel","No problem at all. One of our advisors will call to confirm the details with you, and then operations will process it"),
     ]),
     cta("View My Ticket","{{dashboard_url}}/tickets/{{ticket_id}}","Add anything you'd like us to know"),
     signoff("Whatever works for you,","The Cohort Team"),
   ])

em(id="D4",flow="D. Support Tickets",theme="slate",sender="help@invensislearning.com",
   trigger="Ops console button",timing="MANUAL",
   subject="{{course_name}} cancelled: refund details inside",
   preview="Your refund amount and timeline are confirmed below.",
   blocks=[
     hero("","Cancellation Processed",'All <em>done</em>, {{first_name}}'),
     lead("Your booking for {{course_name}} ({{batch_code}}) has been cancelled. Here are the details."),
     receipt("Refund summary",[("Order","{{order_id}}"),("Amount paid","USD {{amount}}"),("Refund due","USD {{refund_amount}}"),("Method","Original payment method"),("Expected by","{{refund_eta}}")]),
     small("{{refund_policy_note}}"),
     note("info","If you change your mind","If you decide to return within the next six months, we'll offer you this course at the same price you paid today, even if our prices have risen in the meantime. Just reply to this email."),
     cta("View My Ticket","{{dashboard_url}}/tickets/{{ticket_id}}","Ticket {{ticket_id}}"),
     signoff("The door stays open,","The Cohort Team"),
   ])

em(id="D5",flow="D. Support Tickets",theme="violet",sender="help@invensislearning.com",
   trigger="Details change ticket created",timing="T+0",
   subject="Request to update your details: ticket {{ticket_id}}",
   preview="We'll confirm within one working day.",
   blocks=[
     hero("","Update Requested",'We&rsquo;ve got your <em>request</em>'),
     lead("Thanks {{first_name}}. We have your request to update the following on your booking for {{course_name}}."),
     note("info","What you asked us to change","{{requested_changes}}"),
     receipt("Your request",[("Ticket","{{ticket_id}}"),("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Response by","1 working day")]),
     note("warn","We may need to verify one thing","If the change affects the name printed on your certificate, or the email registered with {{governing_body}}, we'll ask you for a document to verify it. Better to catch it now than after the certificate is issued."),
     cta("View My Ticket","{{dashboard_url}}/tickets/{{ticket_id}}","Add anything further, any time"),
     signoff("We'll take it from here,","The Cohort Team"),
   ])

em(id="D6",flow="D. Support Tickets",theme="green",sender="help@invensislearning.com",
   trigger="Ops console button",timing="MANUAL",
   subject="Your details have been updated",
   preview="Please check the spelling of your name carefully.",
   blocks=[
     hero("","Details Updated",'All <em>updated</em>, {{first_name}}'),
     lead("Your booking has been updated. Here's exactly what changed."),
     note("info","What we changed","{{changes_applied_table}}"),
     note("warn","Please check the spelling of your name","It's what gets printed on your certificate, and correcting it after issue is slow and, with some accrediting bodies, chargeable. If anything above is wrong, reply to this email today."),
     cta("View My Details","{{dashboard_url}}/profile","Ticket {{ticket_id}} &middot; closed"),
     signoff("Thanks for checking,","The Cohort Team"),
   ])

em(id="D7",flow="D. Support Tickets",theme="amber",sender="help@invensislearning.com",
   trigger="Training escalation ticket created",timing="T+0",
   subject="We've received your concern: ticket {{ticket_id}}",
   preview="We've taken this as a high priority and a programme manager is now on it.",
   blocks=[
     hero("","High Priority",'We\'re on this, <em>{{first_name}}</em>'),
     lead("Thanks for telling us, {{first_name}}. We've received your concern about {{course_name}} ({{batch_code}}) and taken it as a high priority."),
     receipt("Your escalation",[("Ticket","{{ticket_id}}"),("Owner","{{escalation_owner}}, Programme Manager"),("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Response by","4 working hours")]),
     note("info","You won't have to repeat yourself","Everything you sent us has been passed to {{escalation_owner}} in full. They'll have read it before they contact you."),
     cta("Add Anything Further","{{dashboard_url}}/tickets/{{ticket_id}}","Goes straight to {{escalation_owner}}"),
     small("If this is urgent, reply to this email or call {{support_phone}}."),
     signoff("We'll make this right,","The Cohort Team"),
   ])

em(id="D8",flow="D. Support Tickets",theme="green",sender="help@invensislearning.com",
   trigger="Ops console button",timing="MANUAL",
   subject="Resolved: your concern about {{course_name}}",
   preview="What you raised, what we did, and what changes as a result.",
   blocks=[
     hero("","Escalation Resolved",'Sorted, <em>{{first_name}}</em>'),
     lead("Your escalation is closed. Here's the full picture, in case you want it on record."),
     steps("The resolution",[
       ("What you raised","{{issue_summary}}"),
       ("What we did","{{resolution_summary}}"),
       ("What changes as a result","{{corrective_action}}"),
     ]),
     cta("View My Ticket","{{dashboard_url}}/tickets/{{ticket_id}}","Ticket {{ticket_id}} &middot; resolved"),
     signoff("Thanks for your patience,","{{escalation_owner}}, Programme Manager"),
   ])

# ======================================================= FLOW E
em(id="E1",flow="E. Payment Recovery",theme="red",sender="help@invensislearning.com",
   trigger="Stripe payment_intent.payment_failed",timing="T+5m",
   subject="Your payment didn't go through: let's fix it",
   preview="Don't worry, this happens. We've held your seat. One-click resume inside.",
   blocks=[
     hero("","Payment Support",'A quick issue to <em>resolve</em>, {{first_name}}'),
     lead("We regret to inform you, {{first_name}}, that your payment could not be processed and the transaction has failed. <strong>We have held your {{batch_start_date}} cohort seat for the next 24 hours</strong> while you try again, and no charge has been made."),
     note("warn","What your bank told us","{{decline_reason}}"),
     note("info","What to try next","{{recommended_action}}"),
     receipt("Your payment",[("Order","{{order_id}}"),("Course","{{course_name}}"),("Amount","USD {{amount}}")]),
     cta("Resume Checkout, 1 Click","{{retry_url}}","Your cart is saved &middot; seat held 24 hrs &middot; no re-entry needed"),
     note("info","Still stuck?","Reply to this email or call our payment team on {{support_phone}}. If the card isn't the problem, we can invoice your employer, take a bank transfer, or hold your seat while a purchase order clears. Just ask."),
     signoff("We've got you,","The Payment Support Team"),
   ])

em(id="E2",flow="E. Payment Recovery",theme="amber",sender="help@invensislearning.com",
   trigger="Still unpaid after 1 hour",timing="T+1h",
   subject="Your seat is still being held, {{first_name}}",
   preview="Your cart is intact, your price is locked, and one click puts you back at the payment step.",
   blocks=[
     hero("","Cart Held",'We saved your <em>spot</em>'),
     lead("Your cart is intact. Your price is unchanged. Your {{batch_start_date}} cohort seat is held for another 23 hours. One click and you're back at the payment step, exactly where you left off."),
     receipt("Your saved cart",[("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Seats","{{seat_count}}"),("Reason for decline","{{decline_reason}}")],("Total due","USD {{amount}}")),
     cta("Resume My Checkout","{{retry_url}}","Same cart &middot; same price &middot; same seat"),
     note("info","If your bank blocked it","A quick call to the number on the back of your card usually clears it inside two minutes. First-time payments to overseas training providers get flagged constantly. This is routine and not a reflection on you."),
     signoff("Here when you're ready,","The Payment Support Team"),
   ])

em(id="E3",flow="E. Payment Recovery",theme="amber",sender="help@invensislearning.com",
   trigger="Still unpaid after 6 hours",timing="T+6h",
   subject="{{first_name}}: four ways to complete your enrolment",
   preview="If the card is the problem, it doesn't have to be. Corporate billing, bank transfer, or a call.",
   blocks=[
     hero("","Enrolment Assistance",'One of these <em>will</em> work'),
     lead("Order {{order_id}} is still unpaid and your held seat releases in 18 hours. If your card declined, here's the full menu. We accept whatever works for you."),
     options("Four ways to pay","Pick whichever fits and reply, or use the button below.",[
       ("A","Try the card again","Bank blocks usually clear after one phone call. Same cart, same price, one click"),
       ("B","Bank transfer","Payment receipt issued immediately. Official invoice provided after training completion"),
       ("C","Corporate or employer billing","Reply with your billing contact and we'll arrange it. We'll also supply any sponsorship documentation your L&amp;D or HR team needs, free"),
       ("D","Talk it through first","Book a free 15-minute call. Our advisors will guide you to the right decision, even if that means a later cohort"),
     ]),
     cta("Resume My Checkout","{{retry_url}}","Same cart &middot; same price &middot; seat held 18 more hours"),
     note("info","Need a different cohort date?","The {{next_cohort_start}} cohort is also open at the same price. We can switch your cart across in one click. Just reply."),
     signoff("However works for you,","The Enrolment Team"),
   ])

em(id="E4",flow="E. Payment Recovery",theme="red",sender="help@invensislearning.com",
   trigger="Still unpaid after 24 hours",timing="T+24h &middot; final",
   subject="Final hour: your seat in {{batch_code}} releases today",
   preview="After this, we return it to general sale. This is the last automated email about this order.",
   blocks=[
     hero("","Final Reminder",'Last <em>call</em>, {{first_name}}'),
     lead("This is the last email about your saved cart. Order {{order_id}} is still unpaid, and we're returning your held seat in the {{batch_code}} cohort to general sale today."),
     receipt("What's being released",[("Order","{{order_id}}"),("Course","{{course_name}}"),("Cohort","{{batch_code}}"),("Seats remaining","{{seats_remaining}}")],("Total due","USD {{amount}}")),
     cta("Pay Now &amp; Keep My Seat","{{retry_url}}","Direct payment link &middot; bypasses the cart"),
     note("info","If the cohort fills before you get to this","It isn't the end. Reply to this email and we'll put you on the next cohort at exactly the same price. No penalty, no admin fee."),
     small("This is the last automated email you'll receive about order {{order_id}}."),
     signoff("Here if you need us,","The Payment Support Team"),
   ])

# ======================================================= FLOW F
em(id="F1",flow="F. Trainer",theme="violet",sender="operations@invensislearning.com",
   trigger="Trainer assigned to cohort",timing="T+0",
   subject="Cohort assigned: {{course_name}}, {{batch_code}}",
   preview="Full brief, learner list, and materials inside.",
   blocks=[
     hero("","Cohort Assignment",'{{learner_count}} learners are <em>counting</em> on this'),
     lead("Hi {{trainer_name}}. You've been allocated the following cohort. Everything you need is in the brief."),
     receipt("Cohort details",[
       ("Course","{{course_name}} ({{course_code}})"),("Cohort","{{batch_code}}"),
       ("Dates","{{batch_start_date}} to {{batch_end_date}}"),("Time","{{session_time}} {{timezone}}"),
       ("Learners","{{learner_count}}"),("Client","{{company}}"),("Delivery","{{delivery_mode}}"),
       ("Coordinator","{{ops_coordinator_name}}"),
     ]),
     cta("Open Cohort Brief","{{trainer_portal_url}}/batches/{{batch_code}}","Learner list &middot; agenda &middot; deck &middot; client notes"),
     steps("What's in the brief",[
       ("The learner list","Names, roles, and experience levels. Worth ten minutes before Day 1"),
       ("The agreed agenda","Including anything {{company}} asked us to add or drop"),
       ("The deck and exercises","Current version, already branded"),
       ("Client-specific notes","Context from the sales conversation that didn't fit anywhere else"),
     ]),
     signoff("Thanks as always,","The Operations Team"),
   ])

em(id="F2",flow="F. Trainer",theme="violet",sender="operations@invensislearning.com",
   trigger="24 hours before each session day",timing="T&minus;1d &middot; per session",
   subject="Tomorrow: {{batch_code}}, day {{day_number}}",
   preview="Your host link, tomorrow's agenda, and today's learner feedback.",
   blocks=[
     hero("","Tomorrow's Session",'Day {{day_number}} <em>tomorrow</em>'),
     lead("Hi {{trainer_name}}. {{batch_code}} day {{day_number}} runs on {{session_date}} at {{session_time}} {{timezone}}."),
     cta("Start Session as Host","{{zoom_host_url}}","Host link &middot; do not share with learners"),
     receipt("Tomorrow at a glance",[("Agenda","{{day_agenda}}"),("Learners registered","{{learner_count}}"),("Expected absences","{{known_absences}}"),("Yesterday's feedback score","{{feedback_score}}")]),
     checks("Your pre-class checklist",[
       ("Check your internet connection","A wired connection is best for hosting. Sit close to your router if not, and close other bandwidth-heavy apps before you start"),
       ("Test your camera, microphone, and screen share","Run through the host controls, and confirm your slides and any demo screens share cleanly"),
       ("Have your materials and agenda open","Slides, exercise files, and the agenda for day {{day_number}} ready before learners arrive"),
       ("Set up in a quiet, well-lit space","Headphones to avoid echo, and a plain background so learners stay focused on you"),
       ("Prepare your breakout rooms","If today uses group work, set the rooms up in advance so you're not doing it live"),
       ("Keep the coordinator's number handy","{{ops_coordinator_name}} is on standby if anything technical goes wrong at the start"),
     ]),
     note("info","Please join ten minutes early","Learners are told to arrive five minutes early. We'd rather they weren't sitting in an empty room wondering if they've got the right link."),
     signoff("Have a good session,","The Operations Team"),
   ])

em(id="F3",flow="F. Trainer",theme="amber",sender="operations@invensislearning.com",
   trigger="30 minutes after scheduled session end",timing="T+30m &middot; per session",
   subject="Two minutes: log day {{day_number}} for {{batch_code}}",
   preview="It triggers the learner recap and records attendance. Please do it tonight.",
   blocks=[
     hero("","End of Day","Two minutes, <em>tonight</em>"),
     lead("Hi {{trainer_name}}. Day {{day_number}} of {{batch_code}} has finished. Please log what you covered."),
     cta("Log Day {{day_number}}","{{trainer_portal_url}}/batches/{{batch_code}}/day/{{day_number}}","About 2 minutes &middot; free text, no forms"),
     steps("This isn't admin for its own sake",[
       ("It sends the recap","Your {{learner_count}} learners get their day summary and feedback request within the hour"),
       ("It records attendance","Each learner's attendance for day {{day_number}} is logged against their record"),
       ("It surfaces feedback","Tonight's learner feedback lands in your inbox before tomorrow's session, not after"),
     ]),
     note("warn","Tonight rather than tomorrow morning","The recap loses most of its value if it arrives after learners have gone to bed on Day {{day_number}} and woken up on Day {{next_day_number}}."),
     signoff("Thanks,","The Operations Team"),
   ])

em(id="F4",flow="F. Trainer",theme="amber",sender="operations@invensislearning.com",
   trigger="Day still not logged &middot; several hours after F3 &middot; exits once logged",timing="Reminder",
   subject="Reminder: day {{day_number}} topics for {{batch_code}}",
   preview="We still need the topics you covered today. Log them in the dashboard, or just reply to this email.",
   blocks=[
     hero("","Daily Topics Reminder",'We still need day {{day_number}}, <em>{{trainer_name}}</em>'),
     lead("Hi {{trainer_name}}. We haven't yet received the topics you covered in day {{day_number}} of {{batch_code}}. Your {{learner_count}} learners are waiting on their recap, so a couple of minutes now makes a real difference to them."),
     cta("Log Day {{day_number}} in the Dashboard","{{trainer_portal_url}}/batches/{{batch_code}}/day/{{day_number}}","About 2 minutes &middot; free text, no forms"),
     note("info","Short on time? Just reply to this email","If it's quicker for you, simply reply with the topics you covered today, in a few bullet points or a short paragraph. Our operations team will log them in the dashboard for you and send the learner recap on your behalf."),
     steps("Why we're chasing this",[
       ("Your learners' recap is on hold","The day summary and feedback request only go out once the topics are logged"),
       ("Attendance is recorded at the same time","Day {{day_number}} attendance is captured when you log the session"),
       ("Tomorrow builds on today","Learners revise best when the recap reaches them the same evening"),
     ]),
     note("warn","If today's session didn't run","If day {{day_number}} was cancelled, postponed, or rescheduled, reply and let us know so we don't keep chasing, and so learners are informed correctly."),
     signoff("With thanks for your help,","The Operations Team"),
   ])

# ======================================================= FLOW G
em(id="G1",flow="G. Internal Sales",theme="slate",sender="alerts@invensislearning.com (no-reply)",
   trigger="Lead routed to rep &middot; To: {{sales_rep_email}}",timing="T+0",
   subject="[LEAD] {{full_name}}, {{company}} | {{course_name}} | score {{lead_score}}",
   preview="Assigned to you. The two-hour response clock has started.",
   blocks=[
     hero("","New Lead Assigned",'{{full_name}}, <em>{{company}}</em>'),
     receipt("Lead detail",[
       ("Name","{{full_name}}"),("Company","{{company}}"),("Role","{{job_title}}"),
       ("Email","{{email}}"),("Phone","{{phone}}"),("Interest","{{course_name}}"),
       ("Type","{{lead_type}}"),("Seats","{{seat_count}}"),("Source","{{lead_source}}"),
     ],("Lead score","{{lead_score}}")),
     note("info","What they wrote","{{enquiry_message}}"),
     cta("Open in CRM","{{crm_url}}","Log a call, email, or reassignment"),
     note("warn","Two-hour response clock","If no activity is logged against this lead by {{escalation_time}}, it escalates to Jaya automatically. Logging a call attempt counts."),
   ])

em(id="G2",flow="G. Internal Sales",theme="red",sender="alerts@invensislearning.com (no-reply)",
   trigger="No logged activity after 2 hours &middot; To: {{sales_rep_email}} &middot; Cc: Jaya",timing="T+2h",
   subject="[ESCALATED] Untouched 2 hrs: {{full_name}}, {{company}}",
   preview="No activity logged since assignment. Jaya is copied.",
   blocks=[
     hero("","Escalation",'No activity in <em>two hours</em>'),
     lead("The following lead has had no activity logged against it since it was assigned."),
     receipt("Lead detail",[
       ("Lead","{{full_name}}, {{company}}"),("Assigned","{{assigned_time}} to {{sales_rep_name}}"),
       ("Interest","{{course_name}}, {{seat_count}} seat(s)"),("Source","{{lead_source}}"),
     ],("Lead score","{{lead_score}}")),
     cta("Open in CRM","{{crm_url}}","Log activity or request reassignment"),
     steps("Actions",[
       ("{{sales_rep_name}}","Log a call, an email, or a reassignment request within the next hour"),
       ("Jaya","Reassign directly from the CRM record if {{sales_rep_name}} is unavailable"),
     ]),
   ])

em(id="G3",flow="G. Internal Sales",theme="amber",sender="alerts@invensislearning.com (no-reply)",
   trigger="Result marked Fail &middot; To: {{sales_rep_email}}",timing="T+0",
   subject="[ACTION] {{full_name}} did not pass {{exam_name}}",
   preview="Call within 48 hours. Do not lead with resit pricing.",
   blocks=[
     hero("","Learner Did Not Pass",'{{full_name}}, <em>{{company}}</em>'),
     receipt("Result detail",[
       ("Learner","{{full_name}}"),("Company","{{company}}"),("Course","{{course_name}}, {{batch_code}}"),
       ("Trainer","{{trainer_name}}"),("Exam","{{exam_name}}"),("Attempt","{{attempt_number}}"),
       ("Score","{{exam_score}} (pass mark {{pass_mark}})"),("Weak domains","{{weak_domains}}"),("Result date","{{result_date}}"),
     ]),
     note("info","The learner has already heard from us","They've received their result email, which offers a free 30-minute score-report review with {{trainer_name}}. Please do not be the second person to tell them."),
     note("warn","How to handle this call","Call within 48 hours. <strong>Do not lead with resit pricing.</strong> Lead with the review call. Resit fees come up only if they raise it, or on a second contact. A learner who feels supported resits. A learner who feels sold to churns."),
     cta("Open in CRM","{{crm_url}}","Log the call outcome"),
     small("If this learner is part of a group booking, {{company}} may have others in the same position. Check the cohort before you call the sponsor."),
   ])

em(id="G4",flow="G. Internal Sales",theme="red",sender="alerts@invensislearning.com (no-reply)",
   trigger="D3 fires &middot; To: {{sales_rep_email}}",timing="T+0",
   subject="[CANCEL] {{full_name}}, {{company}} | USD {{amount}} at risk",
   preview="Ticket {{ticket_id}}. Reschedule is still on the table.",
   blocks=[
     hero("","Cancellation Requested",'USD {{amount}} <em>at risk</em>'),
     receipt("Ticket detail",[
       ("Learner","{{full_name}}"),("Company","{{company}}"),("Course","{{course_name}}, {{batch_code}}"),
       ("Order","{{order_id}}"),("Ticket","{{ticket_id}}"),("Raised","{{ticket_raised_time}}"),
       ("Stated reason","{{cancellation_reason}}"),
     ],("Value","USD {{amount}}")),
     note("warn","Your window is now","Operations reviews against the refund policy within one working day. The learner has already been offered a reschedule as an alternative. If you know this account and can find out what actually changed, do it before the refund is processed."),
     cta("Open Ticket","{{ops_url}}/tickets/{{ticket_id}}","Ticket {{ticket_id}}"),
   ])

em(id="G5",flow="G. Internal Sales",theme="slate",sender="alerts@invensislearning.com (no-reply)",
   trigger="D5 fires &middot; To: {{sales_rep_email}}",timing="T+0",
   subject="[CHANGE] {{full_name}}, {{company}} | details update requested",
   preview="FYI only. No action unless the change is material.",
   blocks=[
     hero("","Details Change Requested",'{{full_name}}, <em>{{company}}</em>'),
     receipt("Ticket detail",[
       ("Learner","{{full_name}}"),("Company","{{company}}"),("Course","{{course_name}}, {{batch_code}}"),
       ("Ticket","{{ticket_id}}"),("Requested","{{requested_changes}}"),
     ]),
     note("info","Operations handles this","No action needed from you unless the change is one of the three below."),
     steps("Worth a call if it's any of these",[
       ("Substitution of the named learner","Someone left, or someone was reassigned. Either way the account has moved"),
       ("Change of billing entity","Usually means a restructure, an acquisition, or a budget moving departments"),
       ("Change of company","The learner has left {{company}}. Both the account and the individual are now in play"),
     ]),
     cta("Open Ticket","{{ops_url}}/tickets/{{ticket_id}}","Ticket {{ticket_id}}"),
   ])

# ================================================================ renderers
def rb(blocks, th):
    A,AD,AW,AB = THEME[th]
    o=[]
    for k,v in blocks:
        if k=="eyebrow":
            o.append(f'<p style="margin:0 0 10px;font:700 11px/1 {BODY};letter-spacing:.14em;text-transform:uppercase;color:{A};">{v}</p>')
        elif k=="hero":
            emo,label,head = v
            # em() emphasis in headline -> brand orange bold (matches brochure), not serif italic
            head = head.replace("<em>", f'<span style="color:{ORANGE};">').replace("</em>","</span>")
            e = f'<span style="font-size:26px;line-height:1;vertical-align:-2px;margin-right:8px;">{emo}</span>' if emo else ''
            o.append(
              f'<div style="margin:0 0 20px;">'
              f'<p style="margin:0 0 9px;font:800 11px/1 {BODY};letter-spacing:.15em;text-transform:uppercase;color:{ORANGE};">{label}</p>'
              f'<h1 style="margin:0;font:800 30px/1.15 {DISP};color:{NAVY};letter-spacing:-.01em;">{e}{head}</h1>'
              f'</div>')
        elif k=="lead":
            o.append(f'<p style="margin:0 0 18px;font:400 16px/1.65 {BODY};color:{SOFT};">{v}</p>')
        elif k=="p":
            o.append(f'<p style="margin:0 0 16px;font:400 15px/1.68 {BODY};color:{SOFT};">{v}</p>')
        elif k in ("steps","checks"):
            title,items = v
            rows=""
            for i,(t,d) in enumerate(items,1):
                marker = "✓" if k=="checks" else str(i)
                rows+=(f'<tr><td valign="top" width="30" style="padding:0 12px 16px 0;">'
                       f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tbody><tr>'
                       f'<td width="26" height="26" align="center" bgcolor="{A}" style="border-radius:7px;font:700 12px/26px {BODY};color:#fff;">{marker}</td>'
                       f'</tr></tbody></table></td>'
                       f'<td style="padding:0 0 16px;">'
                       f'<div style="font:700 14px/1.45 {BODY};color:{INK};margin:0 0 3px;">{t}</div>'
                       f'<div style="font:400 13.5px/1.6 {BODY};color:{MUT};">{d}</div></td></tr>')
            o.append(f'<p style="margin:0 0 14px;font:700 15px/1.4 {BODY};color:{INK};">{title}</p>'
                     f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 22px;"><tbody>{rows}</tbody></table>')
        elif k=="options":
            title,intro,items=v
            rows=""
            for L,t,d in items:
                rows+=(f'<tr><td valign="top" width="34" style="padding:0 12px 14px 0;">'
                       f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tbody><tr>'
                       f'<td width="28" height="28" align="center" style="border:1.5px solid {A};border-radius:8px;font:700 12px/26px {BODY};color:{A};">{L}</td>'
                       f'</tr></tbody></table></td>'
                       f'<td style="padding:0 0 14px;">'
                       f'<div style="font:700 14px/1.45 {BODY};color:{INK};margin:0 0 3px;">{t}</div>'
                       f'<div style="font:400 13.5px/1.6 {BODY};color:{MUT};">{d}</div></td></tr>')
            o.append(f'<p style="margin:0 0 6px;font:700 15px/1.4 {BODY};color:{INK};">{title}</p>'
                     f'<p style="margin:0 0 14px;font:400 13.5px/1.6 {BODY};color:{MUT};">{intro}</p>'
                     f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 22px;"><tbody>{rows}</tbody></table>')
        elif k=="receipt":
            title,rows,total=v
            rr="".join(
              f'<tr><td style="padding:8px 0;font:500 13px/1.5 {BODY};color:{MUT};border-bottom:1px solid {RULE};">{a}</td>'
              f'<td align="right" style="padding:8px 0;font:600 13px/1.5 {BODY};color:{INK};border-bottom:1px solid {RULE};">{b}</td></tr>'
              for a,b in rows)
            if total:
                rr+=(f'<tr><td style="padding:13px 0 0;font:700 14px/1.5 {BODY};color:{INK};">{total[0]}</td>'
                     f'<td align="right" style="padding:13px 0 0;font:700 17px/1.5 {BODY};color:{A};">{total[1]}</td></tr>')
            o.append(f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 22px;background:{PAPER};border:1px solid {RULE};border-radius:12px;">'
                     f'<tbody><tr><td style="padding:20px 22px;">'
                     f'<p style="margin:0 0 12px;font:700 10.5px/1 {BODY};letter-spacing:.13em;text-transform:uppercase;color:{MUT};">{title}</p>'
                     f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tbody>{rr}</tbody></table>'
                     f'</td></tr></tbody></table>')
        elif k=="cta":
            label,url,sub=v
            o.append(f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:6px 0 22px;"><tbody>'
                     f'<tr><td align="center"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tbody><tr>'
                     f'<td align="center" bgcolor="{CTA_BG}" style="border-radius:10px;">'
                     f'<a href="{url}" style="display:inline-block;padding:15px 34px;font:800 14.5px/1 {BODY};color:{CTA_TX};text-decoration:none;border-radius:10px;letter-spacing:.01em;">{label} &rarr;</a>'
                     f'</td></tr></tbody></table></td></tr>'
                     f'<tr><td align="center" style="padding:11px 0 0;font:500 11.5px/1.5 {BODY};color:{MUT};">{sub}</td></tr>'
                     f'</tbody></table>')
        elif k=="note":
            kind,title,body=v
            cmap={"info":(VIO_W,VIO,VIO_D),"warn":(AMB_W,AMB_B,AMB_D),"success":(GRN_W,"#bbf7d0",GRN_D),"danger":(RED_W,"#fecaca",RED_D)}
            bg,bd,tc=cmap.get(kind,cmap["info"])
            o.append(f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:0 0 20px;background:{bg};border:1px solid {bd};border-radius:11px;">'
                     f'<tbody><tr><td style="padding:16px 18px;">'
                     f'<p style="margin:0 0 5px;font:700 13.5px/1.45 {BODY};color:{tc};">{title}</p>'
                     f'<p style="margin:0;font:400 13.5px/1.62 {BODY};color:{SOFT};">{body}</p>'
                     f'</td></tr></tbody></table>')
        elif k=="rule":
            o.append(f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:4px 0 20px;"><tbody><tr><td height="1" style="background:{RULE};font-size:0;line-height:0;">&nbsp;</td></tr></tbody></table>')
        elif k=="small":
            o.append(f'<p style="margin:0 0 14px;font:400 12.5px/1.6 {BODY};color:{MUT};">{v}</p>')
        elif k=="signoff":
            line,team=v
            o.append(f'<p style="margin:26px 0 0;font:400 15px/1.6 {BODY};color:{SOFT};">{line}<br>'
                     f'<strong style="color:{INK};">{team}</strong></p>')
        elif k=="disc":
            o.append(f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:24px 0 0;border-top:1px solid {RULE};">'
                     f'<tbody><tr><td style="padding:16px 0 0;font:400 11px/1.65 {BODY};color:{MUT};">{v}</td></tr></tbody></table>')
    return "\n".join(o)

def full_doc(e):
    A,AD,AW,AB=THEME[e["theme"]]
    inner=rb(e["blocks"],e["theme"])
    return f'''<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">
<title>{_h.escape(re.sub("<[^>]+>","",e["subject"]))}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@media only screen and (max-width:620px){{ .wrap{{width:100%!important}} .pad{{padding:26px 20px!important}} h1{{font-size:26px!important}} }}
a{{color:{A}}}
</style></head>
<body style="margin:0;padding:0;background:{WASH};">
<div style="display:none;font-size:1px;color:{WASH};line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">{_h.escape(re.sub("<[^>]+>","",e["preview"]))}&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;&#847;&zwnj;&nbsp;</div>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:{WASH};"><tbody><tr><td align="center" style="padding:30px 12px;">
<table role="presentation" class="wrap" cellpadding="0" cellspacing="0" border="0" width="600" style="width:600px;max-width:600px;background:{PAPER};border-radius:14px;overflow:hidden;box-shadow:0 2px 10px rgba(16,16,48,.07);">
<tbody>
<tr><td style="background:{NAVY};padding:20px 34px;">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tbody><tr>
    <td style="font:800 19px/1 {BODY};letter-spacing:.02em;color:#ffffff;">INV<span style="color:{ORANGE};">=</span>NSIS <span style="font:500 11px/1 {BODY};color:#aeb6d6;letter-spacing:.04em;">Global Learning Services</span></td>
    <td align="right" style="font:600 10px/1 {BODY};letter-spacing:.12em;text-transform:uppercase;color:#8f98c0;">{e["id"]}</td>
  </tr></tbody></table>
</td></tr>
<tr><td style="height:4px;background:{ORANGE};font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td class="pad" style="padding:32px 34px 34px;">
{inner}
</td></tr>
{build_footer(e)}
</tbody></table>
</td></tr></tbody></table>
</body></html>'''

# markdown deck
def strip(s): return re.sub(r"<[^>]+>","",s).replace("&mdash;",": ").replace("&middot;","·").replace("&amp;","&").replace("&rsquo;","'").replace("&minus;","-").replace("&reg;","")
def mdb(blocks):
    o=[]
    for k,v in blocks:
        if k=="hero":
            emo,label,head=v; o.append(f"**{label.upper()}**\n\n### {emo} {strip(head)}".strip())
        elif k in("lead","p"): o.append(strip(v))
        elif k=="small": o.append("_"+strip(v)+"_")
        elif k in("steps","checks"):
            t,items=v; o.append(f"**{t}**\n\n"+"\n".join(f"{i}. **{strip(a)}**: {strip(b)}" if k=="steps" else f"- [ ] **{strip(a)}**: {strip(b)}" for i,(a,b) in enumerate(items,1)))
        elif k=="options":
            t,intro,items=v; o.append(f"**{t}**\n\n{strip(intro)}\n\n"+"\n".join(f"**{L}.** **{strip(a)}**: {strip(b)}" for L,a,b in items))
        elif k=="receipt":
            t,rows,tot=v
            body="\n".join(f"| {strip(a)} | {strip(b)} |" for a,b in rows)
            if tot: body+=f"\n| **{strip(tot[0])}** | **{strip(tot[1])}** |"
            o.append(f"**{t}**\n\n| | |\n|---|---|\n{body}")
        elif k=="cta":
            l,u,s=v; o.append(f"**[ {strip(l)} ]** → `{u}`\n\n_{strip(s)}_")
        elif k=="note":
            kind,t,b=v; o.append(f"> **{strip(t)}**\n> {strip(b)}")
        elif k=="rule": o.append("---")
        elif k=="signoff":
            l,t=v; o.append(f"{strip(l)}\n**{strip(t)}**")
        elif k=="disc": o.append("```\n"+strip(v).strip()+"\n```")
    return "\n\n".join(o)

md=["# Invensis Learning | Lifecycle Emails v3.0","",
    "Voice and visual system matched to the official Invensis PMP brochure.",
    f"{len(E)} templates across 7 flows. British English. HTML in `invensis-emails.html`.",""]
cur=None
for e in E:
    if e["flow"]!=cur:
        cur=e["flow"]; md+=["","---","",f"## FLOW {strip(cur)}",""]
    fb_line = f"**Feedback:** {strip(e['feedback'])}" if e.get("feedback") else "**Feedback:** _none_"
    md+=[f"### {e['id']} | {strip(e['subject'])}","",
         f"**From:** {strip(e['sender'])} · **Trigger:** {strip(e['trigger'])} · **{strip(e['timing'])}**","",
         f"**Subject:** {strip(e['subject'])}  ",f"**Preview:** {strip(e['preview'])}","",
         fb_line,"",
         mdb(e["blocks"]),""]

os.makedirs("../output",exist_ok=True)
open("../output/invensis-emails.md","w",encoding="utf-8").write("\n".join(md))

# gallery
flows=[]
for e in E:
    if not flows or flows[-1][0]!=e["flow"]: flows.append((e["flow"],[]))
    flows[-1][1].append(e)
nav=""
for fn,items in flows:
    nav+=f'<div class="ng"><div class="nh">{fn}</div>'
    for e in items:
        nav+=f'<a href="#{e["id"]}"><span class="nid">{e["id"]}</span><span>{strip(e["subject"])[:34]}</span></a>'
    nav+="</div>"
cards=""
for e in E:
    A,AD,AW,AB=THEME[e["theme"]]
    cards+=f'''<section class="card" id="{e["id"]}">
<header class="meta">
 <div class="mr"><span class="dot" style="background:{A}"></span><span class="eid">{e["id"]}</span><h2>{strip(e["subject"])}</h2></div>
 <dl>
  <div><dt>From</dt><dd>{strip(e["sender"])}</dd></div>
  <div><dt>Trigger</dt><dd>{e["trigger"]}</dd></div>
  <div><dt>Timing</dt><dd>{e["timing"]}</dd></div>
  <div><dt>Preview text</dt><dd>{strip(e["preview"])}</dd></div>
  <div class="fb-row"><dt>Feedback</dt><dd><div class="fb-wrap"><textarea class="fb" data-id="{e["id"]}" placeholder="Add feedback for this email…">{_h.escape(e.get("feedback",""))}</textarea><div class="fb-actions"><button class="fb-save" data-id="{e["id"]}">Save</button><span class="fb-status" data-id="{e["id"]}"></span></div></div></dd></div>
 </dl>
 <button class="copy" data-t="s-{e["id"]}">Copy HTML</button>
</header>
<div class="stage"><div class="env">
 <div class="br"><span class="bd">INV<span style="color:{ORANGE}">=</span>NSIS <span style="font:500 10px/1 {BODY};color:#aeb6d6">Global Learning Services</span></span><span class="eids">{e["id"]}</span></div>
 <div class="tb" style="background:{ORANGE}"></div>
 <div class="eb">{rb(e["blocks"],e["theme"])}</div>
 <div class="ef">Connect with Invensis Learning<br>For any query: <a href="mailto:{CONTACT_EMAIL}" style="color:{ORANGE};text-decoration:none">{CONTACT_EMAIL}</a><br><span style="display:inline-block;max-width:470px;color:#8f98c0;padding:6px 0">{' &nbsp;|&nbsp; '.join(f'<strong style=\"color:#c3c9dd\">{r}:</strong> {n}' for r,n in PHONE_BLOCK)}</span><br>{ADDR_LINE}<br>Terms &amp; Conditions · Privacy Policy · Refund Policy · Rescheduling Policy · {'Update email preferences' if e["id"] in MARKETING else 'Service email'}<br>{COPYRIGHT}</div>
</div></div>
<script type="text/plain" id="s-{e["id"]}">{_h.escape(full_doc(e))}</script>
</section>'''

g=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Invensis Learning | Lifecycle Email System v3.0</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#e9eaee;color:{INK};font:15px/1.6 {BODY}}}
.shell{{display:grid;grid-template-columns:290px 1fr;min-height:100vh}}
nav{{position:sticky;top:0;height:100vh;overflow-y:auto;background:{INK};padding:26px 0 50px}}
.lg{{font:400 21px/1 {DISP};color:#fff;padding:0 22px 5px}}
.sb{{font:600 9.5px/1.5 {BODY};letter-spacing:.16em;text-transform:uppercase;color:#7c8598;padding:0 22px 24px}}
.ng{{margin-bottom:16px}}
.nh{{font:700 9.5px/1 {BODY};letter-spacing:.14em;text-transform:uppercase;color:#7c8598;padding:0 22px 8px}}
nav a{{display:flex;gap:9px;padding:6px 22px;color:#c3c9d4;text-decoration:none;font-size:12.5px}}
nav a:hover{{background:rgba(255,255,255,.07);color:#fff}}
nav a:focus-visible{{outline:2px solid {VIO};outline-offset:-2px}}
.nid{{font:600 10.5px/1.5 {MONO};color:{VIO};min-width:34px}}
nav a span:last-child{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
main{{padding:44px 40px 120px;max-width:1200px}}
.intro{{max-width:660px;margin:0 0 44px}}
.intro h1{{font:400 44px/1.08 {DISP};letter-spacing:-.02em;margin:0 0 14px}}
.intro p{{color:{MUT};margin:0 0 10px}}
.legend{{display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}}
.lc{{font:600 11px/1 {BODY};padding:9px 12px;border-radius:8px;color:#fff}}
.card{{background:#fff;border-radius:14px;margin:0 0 32px;overflow:hidden;scroll-margin-top:18px;box-shadow:0 1px 2px rgba(15,22,38,.06)}}
.meta{{padding:22px 26px;border-bottom:1px solid {RULE};position:relative}}
.mr{{display:flex;align-items:center;gap:11px;margin-bottom:14px}}
.dot{{width:10px;height:10px;border-radius:50%;flex:none}}
.eid{{font:600 11.5px/1 {MONO};color:{MUT}}}
.mr h2{{font:400 20px/1.25 {DISP};margin:0}}
dl{{margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px 24px}}
dt{{font:700 8.5px/1 {BODY};letter-spacing:.13em;text-transform:uppercase;color:{MUT};margin-bottom:4px}}
dd{{margin:0;font-size:12.5px;color:{SOFT};word-break:break-word}}
.copy{{position:absolute;top:20px;right:22px;font:700 10.5px/1 {BODY};letter-spacing:.08em;text-transform:uppercase;background:{INK};color:#fff;border:0;padding:11px 15px;border-radius:8px;cursor:pointer}}
.copy:hover{{background:{VIO}}}
.copy:focus-visible{{outline:2px solid {VIO};outline-offset:2px}}
.stage{{background:{WASH};padding:32px 20px}}
.env{{max-width:600px;margin:0 auto;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 2px 8px rgba(15,22,38,.08)}}
.tb{{height:4px}}
.br{{display:flex;justify-content:space-between;align-items:center;padding:18px 34px;background:{NAVY}}}
.bd{{font:800 18px/1 {BODY};letter-spacing:.02em;color:#fff}}
.eids{{color:#8f98c0 !important}}
.eids{{font:600 9.5px/1 {BODY};letter-spacing:.15em;text-transform:uppercase;color:{MUT}}}
.eb{{padding:26px 34px 32px}}
.ef{{background:{NAVY};padding:22px 34px 26px;font:400 11px/1.85 {BODY};color:#8f98c0;text-align:center}}
.fb-row{{grid-column:1/-1}}
.fb-wrap{{display:flex;flex-direction:column;gap:8px}}
.fb{{width:100%;min-height:60px;padding:10px 12px;border:1.5px dashed #d1d5db;border-radius:8px;font:13px/1.5 {BODY};color:{INK};background:#fefce8;resize:vertical}}
.fb:focus{{border-color:{BLUE};outline:none;box-shadow:0 0 0 3px rgba(1,139,212,.15)}}
.fb::placeholder{{color:#9ca3af}}
.fb-actions{{display:flex;align-items:center;gap:10px}}
.fb-save{{font:700 11px/1 {BODY};letter-spacing:.06em;text-transform:uppercase;background:{BLUE};color:#fff;border:0;padding:8px 18px;border-radius:6px;cursor:pointer;transition:background .15s}}
.fb-save:hover{{background:{BLUE_D}}}
.fb-save.saved{{background:{GRN}}}
.fb-status{{font:600 12px/1 {BODY};color:{GRN};opacity:0;transition:opacity .3s}}
.fb-status.show{{opacity:1}}
.export-fb{{display:inline-flex;align-items:center;gap:6px;margin-top:14px;font:700 12px/1 {BODY};letter-spacing:.06em;text-transform:uppercase;background:{INK};color:#fff;border:0;padding:12px 20px;border-radius:8px;cursor:pointer}}
.export-fb:hover{{background:{BLUE}}}
@media(max-width:960px){{.shell{{grid-template-columns:1fr}}nav{{position:static;height:auto}}main{{padding:28px 16px 80px}}.copy{{position:static;margin-top:12px}}}}
@media(prefers-reduced-motion:reduce){{*{{transition:none!important;animation:none!important}}}}
</style></head><body>
<div class="shell">
<nav><div class="lg">Invensis Learning</div><div class="sb">Email system v3.0 · {len(E)} templates</div>{nav}</nav>
<main>
<div class="intro">
<h1>Lifecycle email system</h1>
<p>{len(E)} responsive, table-based templates across seven flows, styled to match the official Invensis PMP brochure: navy #101030, brochure blue #018BD4, and the INV=NSIS orange #F8981C on every call to action. Plus Jakarta Sans throughout, numbered timelines, receipt blocks, and CTA sub-captions.</p>
<p>Merge tokens use <code style="font:12px {MONO}">{{{{double_brace}}}}</code>. Each card's <strong>Copy HTML</strong> button gives you the full standalone document with inline styles, hidden preheader, and a 620px mobile breakpoint.</p>
<div class="legend">
<span class="lc" style="background:{BLUE}">Blue · lifecycle</span>
<span class="lc" style="background:{GRN}">Green · success</span>
<span class="lc" style="background:{AMB}">Amber · action needed</span>
<span class="lc" style="background:{RED}">Red · failure or final notice</span>
<span class="lc" style="background:{NAVY}">Navy · internal &amp; sensitive</span>
</div>
<button class="export-fb" id="exportFb">Export All Feedback</button>
</div>
{cards}
</main></div>
<script>
document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{
var t=document.getElementById(b.dataset.t).textContent;
function done(){{var o=b.textContent;b.textContent='Copied';setTimeout(function(){{b.textContent=o}},1400)}}
if(navigator.clipboard){{navigator.clipboard.writeText(t).then(done).catch(fb)}}else{{fb()}}
function fb(){{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove();done()}}
}})}});
document.querySelectorAll('.fb').forEach(function(ta){{
var k='fb_'+ta.dataset.id;
var saved=localStorage.getItem(k);
if(saved!==null)ta.value=saved;
}});
document.querySelectorAll('.fb-save').forEach(function(btn){{
btn.addEventListener('click',function(){{
var id=btn.dataset.id;
var ta=document.querySelector('.fb[data-id="'+id+'"]');
var st=document.querySelector('.fb-status[data-id="'+id+'"]');
localStorage.setItem('fb_'+id,ta.value);
btn.classList.add('saved');btn.textContent='Saved';
st.textContent='Saved!';st.classList.add('show');
setTimeout(function(){{btn.classList.remove('saved');btn.textContent='Save';st.classList.remove('show')}},2000);
}});
}});
document.getElementById('exportFb').addEventListener('click',function(){{
var rows=[['Email ID','Subject','Feedback']];
document.querySelectorAll('.fb').forEach(function(ta){{
var id=ta.dataset.id;
var val=localStorage.getItem('fb_'+id)||ta.value||'';
if(val){{
var subEl=document.getElementById(id);
var sub=subEl?subEl.querySelector('.mr h2'):null;
var subj=sub?sub.textContent:'';
rows.push([id,'"'+subj.replace(/"/g,'""')+'"','"'+val.replace(/"/g,'""')+'"']);
}}
}});
if(rows.length<2){{alert('No feedback saved yet.');return}}
var csv=rows.map(function(r){{return r.join(',')}}).join('\\n');
var blob=new Blob([csv],{{type:'text/csv'}});
var a=document.createElement('a');a.href=URL.createObjectURL(blob);
a.download='email-feedback-'+new Date().toISOString().slice(0,10)+'.csv';
a.click();URL.revokeObjectURL(a.href);
}});
</script></body></html>'''
open("../output/invensis-emails.html","w",encoding="utf-8").write(g)
print("templates:",len(E),"| flows:",len(flows),"| html kb:",round(len(g)/1024))

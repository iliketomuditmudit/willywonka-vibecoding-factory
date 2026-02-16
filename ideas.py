"""
20 B2B SaaS idea slips and their corresponding vibe-coding prompts.

Each idea has:
  - id: unique identifier (matches capsule ball number)
  - name: short catchy name for the idea
  - slip_text: what's printed on the slip inside the gumball capsule
  - keywords: terms used for fuzzy matching when the idea is typed in
  - prompt: the full prompt sent to the code-generation API
"""

IDEAS = [
    {
        "id": 1,
        "name": "MeetingShrink",
        "slip_text": "An AI that summarizes your 1-hour meeting into 3 bullet points",
        "keywords": ["meeting", "summarize", "summary", "bullet", "points", "notes", "recap"],
        "prompt": (
            "Build a single-page web app called 'MeetingShrink'. "
            "It has a large textarea where users paste meeting transcripts. "
            "There's a big purple 'Shrink It!' button. When clicked, simulate an AI processing animation "
            "(progress bar filling up with funny messages like 'Removing awkward silences...' and 'Deleting Dave's tangents...'), "
            "then display 3 concise bullet-point takeaways in a card below. "
            "Use a clean modern UI with a purple/white color scheme. Include the tagline 'Because nobody has time for that.' "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 2,
        "name": "InvoiceNinja",
        "slip_text": "Auto-generate invoices from Slack messages",
        "keywords": ["invoice", "slack", "billing", "payment", "generate", "auto"],
        "prompt": (
            "Build a single-page web app called 'InvoiceNinja'. "
            "It has a textarea labeled 'Paste your Slack conversation' and fields for client name, hourly rate, and currency. "
            "A 'Generate Invoice' button parses the text, extracts mentioned tasks/hours, and renders a professional-looking invoice "
            "with line items, subtotal, tax, and total in a printable card format. "
            "Include a 'Download PDF' button (use window.print). "
            "Use a dark ninja-themed color scheme (dark gray, red accents). "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 3,
        "name": "ChurnOracle",
        "slip_text": "Predict which customers will cancel before they do",
        "keywords": ["churn", "predict", "cancel", "customer", "retention", "oracle"],
        "prompt": (
            "Build a single-page web app called 'ChurnOracle'. "
            "Show a dashboard with a table of 10 fake customers, each with columns: name, signup date, last login, "
            "support tickets, usage trend (sparkline), and a 'Churn Risk' score shown as a colored badge (green/yellow/red). "
            "Include a donut chart at the top showing overall risk distribution. "
            "Add a 'Run Prediction' button with a crystal ball animation. "
            "Use mystical purple/gold color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 4,
        "name": "OnboardBot",
        "slip_text": "Employee onboarding that runs itself",
        "keywords": ["onboard", "employee", "hr", "hiring", "new hire", "orientation", "bot"],
        "prompt": (
            "Build a single-page web app called 'OnboardBot'. "
            "Show a multi-step onboarding wizard for new employees with steps: Welcome, Personal Info, "
            "Equipment Request, Team Introduction, First Week Schedule. "
            "Each step has a form with relevant fields. Include a progress bar at the top, "
            "a friendly robot mascot SVG that changes expression per step, and animated transitions between steps. "
            "Use a warm blue/orange color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 5,
        "name": "PipelinePulse",
        "slip_text": "A sales pipeline that tells you what to do next",
        "keywords": ["sales", "pipeline", "crm", "deals", "leads", "pulse"],
        "prompt": (
            "Build a single-page web app called 'PipelinePulse'. "
            "Show a Kanban-style sales pipeline with columns: Prospect, Contacted, Demo Scheduled, Proposal Sent, Closed Won, Closed Lost. "
            "Pre-populate with 8-10 fake deal cards (company name, value, days in stage). "
            "Cards should be draggable between columns. Include a top banner with total pipeline value and a "
            "'Next Best Action' recommendation card that suggests which deal to focus on. "
            "Use a green/white financial color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 6,
        "name": "FeedbackFunnel",
        "slip_text": "Turn customer feedback into product features automatically",
        "keywords": ["feedback", "feature", "customer", "product", "request", "funnel", "roadmap"],
        "prompt": (
            "Build a single-page web app called 'FeedbackFunnel'. "
            "Show a split-screen: left side has a feed of customer feedback cards (10 pre-populated fake quotes), "
            "right side shows extracted feature requests grouped by theme with vote counts. "
            "Include a 'Process Feedback' button with a funnel animation. "
            "Each feature request card has an urgency badge and an 'Add to Roadmap' button. "
            "Use a teal/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 7,
        "name": "ContractCop",
        "slip_text": "Scan contracts and flag the scary clauses",
        "keywords": ["contract", "legal", "clause", "scan", "flag", "review", "cop"],
        "prompt": (
            "Build a single-page web app called 'ContractCop'. "
            "It has a textarea to paste contract text and a 'Scan Contract' button. "
            "After clicking, show the contract text with highlighted sections: red for risky clauses, "
            "yellow for unusual terms, green for standard clauses. "
            "Show a sidebar with a risk summary, overall risk score (badge), and a list of flagged items with explanations. "
            "Include a police badge icon in the header. "
            "Use a navy/red/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 8,
        "name": "TicketTamer",
        "slip_text": "Support tickets that categorize and prioritize themselves",
        "keywords": ["ticket", "support", "helpdesk", "triage", "prioritize", "tamer", "customer support"],
        "prompt": (
            "Build a single-page web app called 'TicketTamer'. "
            "Show a support ticket dashboard with a submission form (subject, description, customer tier dropdown) "
            "and a live ticket queue below. Pre-populate with 8 fake tickets. "
            "Each ticket auto-gets a category badge (Bug, Feature, Billing, How-To) and priority (P1-P4) with color coding. "
            "Include filter buttons at the top and a 'Tame the Queue' button that sorts/groups everything with an animation. "
            "Use an orange/brown 'circus tamer' theme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 9,
        "name": "ExpenseGhost",
        "slip_text": "Expense reports that write themselves from receipts",
        "keywords": ["expense", "receipt", "report", "reimburse", "ghost", "finance"],
        "prompt": (
            "Build a single-page web app called 'ExpenseGhost'. "
            "Show an expense report builder. Users can add expense entries with: date, vendor, amount, category dropdown "
            "(Travel, Meals, Software, Office, Other), and notes. "
            "Include an 'Add Receipt' button that simulates OCR (pre-fills random realistic data with a ghost animation). "
            "Show a running total, category breakdown bar chart, and a 'Submit Report' button. "
            "Use a translucent ghost-themed UI (light grays, ethereal glows). "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 10,
        "name": "StatusPageForge",
        "slip_text": "A status page for your SaaS that actually looks good",
        "keywords": ["status", "page", "uptime", "monitoring", "incident", "forge"],
        "prompt": (
            "Build a single-page web app called 'StatusPageForge'. "
            "Show a public-facing status page with 6 services (API, Web App, Database, CDN, Auth, Webhooks), "
            "each with a 90-day uptime bar (green/yellow/red segments), current status badge, and response time. "
            "Include an incident timeline at the bottom with 3 past incidents. "
            "Add a 'Subscribe to Updates' email input and a real-time clock showing 'Last checked'. "
            "Use a clean black/green/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 11,
        "name": "ProposalPilot",
        "slip_text": "Generate client proposals in 30 seconds",
        "keywords": ["proposal", "client", "generate", "pitch", "bid", "pilot"],
        "prompt": (
            "Build a single-page web app called 'ProposalPilot'. "
            "Show a form with fields: client name, project type dropdown, scope description textarea, timeline, and budget range. "
            "A 'Generate Proposal' button creates a polished proposal preview with sections: Executive Summary, "
            "Scope of Work, Timeline, Pricing Table, and Terms. "
            "Include a 'flying paper airplane' animation during generation. "
            "The proposal should look print-ready with professional typography. "
            "Use a sky blue/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 12,
        "name": "AnalyticsOwl",
        "slip_text": "A dashboard that explains your metrics in plain English",
        "keywords": ["analytics", "dashboard", "metrics", "data", "insights", "owl", "explain"],
        "prompt": (
            "Build a single-page web app called 'AnalyticsOwl'. "
            "Show a metrics dashboard with: MRR ($45,200), Active Users (12,340), Churn Rate (3.2%), NPS (72). "
            "Each metric card has a sparkline trend, percentage change badge, and an owl icon. "
            "Below each metric, show a plain-English insight (e.g., 'Your MRR grew 12% this month, mainly from Enterprise tier upgrades'). "
            "Include a 'Hoot for Insights' button that refreshes the commentary with a wise owl animation. "
            "Use a dark navy/amber/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 13,
        "name": "ColdMailCraft",
        "slip_text": "Write cold outreach emails that people actually open",
        "keywords": ["cold", "email", "outreach", "mail", "sales email", "craft"],
        "prompt": (
            "Build a single-page web app called 'ColdMailCraft'. "
            "Show a form with: recipient role, company, pain point, your product name, and tone selector (Professional/Casual/Bold). "
            "A 'Craft Email' button generates 3 email variations displayed as actual email previews with subject lines. "
            "Each variation has a predicted open rate badge and a 'Copy' button. "
            "Include A/B testing visuals showing which variant performs better. "
            "Use a red/dark-gray email client aesthetic. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 14,
        "name": "PermissionPretzel",
        "slip_text": "Untangle your team's permissions and access controls",
        "keywords": ["permission", "access", "role", "rbac", "iam", "pretzel", "security"],
        "prompt": (
            "Build a single-page web app called 'PermissionPretzel'. "
            "Show a visual access control matrix: rows are 6 team members (with avatars), columns are 8 resources "
            "(Dashboard, Billing, API Keys, Users, Settings, Reports, Integrations, Logs). "
            "Each cell is a clickable toggle (Read/Write/Admin/None) with color coding. "
            "Include role presets (Admin, Editor, Viewer) that fill the matrix with one click. "
            "Show a 'twisted pretzel' logo and an 'Untangle' button that identifies conflicts. "
            "Use a warm brown/yellow pretzel theme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 15,
        "name": "ChangelogGenie",
        "slip_text": "Auto-generate changelogs from your Git commits",
        "keywords": ["changelog", "git", "release", "notes", "version", "genie"],
        "prompt": (
            "Build a single-page web app called 'ChangelogGenie'. "
            "Show a textarea to paste Git commit messages and a version number input. "
            "A 'Summon Changelog' button (with a lamp/genie animation) generates a formatted changelog grouped by: "
            "Features, Bug Fixes, Improvements, Breaking Changes. "
            "Each entry has a commit hash link, author badge, and date. "
            "Include a toggle between 'Developer' and 'Customer-facing' versions of the changelog. "
            "Use a magical purple/gold color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 16,
        "name": "APIPlayground",
        "slip_text": "Test any API endpoint without writing code",
        "keywords": ["api", "test", "endpoint", "rest", "request", "playground", "postman"],
        "prompt": (
            "Build a single-page web app called 'APIPlayground'. "
            "Show a Postman-style interface with: method selector (GET/POST/PUT/DELETE), URL input, "
            "headers table (key-value pairs with add/remove), body editor (JSON with syntax highlighting), "
            "and a 'Send' button. Display the response in a panel below with status code badge, "
            "response time, formatted JSON body, and response headers. "
            "Include a history sidebar with recent requests. "
            "Use a dark theme with green/blue accents. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 17,
        "name": "WaitlistWizard",
        "slip_text": "A beautiful waitlist page that builds hype before launch",
        "keywords": ["waitlist", "launch", "landing", "signup", "hype", "wizard", "prelaunch"],
        "prompt": (
            "Build a single-page web app called 'WaitlistWizard'. "
            "Show a stunning pre-launch landing page with: big hero headline ('Something magical is coming'), "
            "animated countdown timer, email signup with referral tracking (shows your position: #142 of 2,847), "
            "social sharing buttons that promise queue jumping, a progress bar showing 'spots remaining', "
            "and an animated background with floating sparkles. "
            "Include testimonial-style social proof ('2,847 founders already waiting'). "
            "Use a gradient purple-to-blue color scheme with white text. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 18,
        "name": "TeamPulse",
        "slip_text": "Daily standups without the standing up part",
        "keywords": ["standup", "team", "daily", "async", "pulse", "check-in", "status update"],
        "prompt": (
            "Build a single-page web app called 'TeamPulse'. "
            "Show a daily async standup board. Left side: a form with 'Yesterday', 'Today', 'Blockers' textareas and mood selector (5 emojis). "
            "Right side: a timeline feed showing 6 pre-populated team member updates with avatars, timestamps, and mood indicators. "
            "Include a team mood summary at the top (emoji distribution chart) and a 'Blockers Alert' section highlighting who's stuck. "
            "Use a calming green/white color scheme. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 19,
        "name": "PricingLab",
        "slip_text": "A/B test your SaaS pricing page without a developer",
        "keywords": ["pricing", "ab test", "tier", "plan", "subscription", "lab"],
        "prompt": (
            "Build a single-page web app called 'PricingLab'. "
            "Show a pricing page builder with 3 editable tier cards (Starter, Pro, Enterprise). "
            "Each card has: editable name, price, billing toggle (monthly/yearly), feature list (add/remove), "
            "and a CTA button. Include a 'Variant B' tab to create an alternate version. "
            "Show a simulated A/B test results panel with conversion rates, confidence interval, and a winner badge. "
            "Include a 'Run Experiment' button with a beaker animation. "
            "Use a lab/science theme (white, blue, slight green). "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 20,
        "name": "DocuMentor",
        "slip_text": "Turn your codebase into documentation automatically",
        "keywords": ["documentation", "docs", "code", "generate", "readme", "mentor", "docstring"],
        "prompt": (
            "Build a single-page web app called 'DocuMentor'. "
            "Show a split-screen: left has a code editor (monospace textarea with line numbers) pre-filled with a Python class, "
            "right shows generated documentation in a clean format with: function signatures, parameter tables, "
            "return types, usage examples, and a complexity badge. "
            "Include a 'Generate Docs' button with a book-opening animation. "
            "Add toggles for output format: Markdown, HTML, or Docstring. "
            "Use a warm paper/ink color scheme (cream background, dark text, brown accents). "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
]


def find_best_match(user_input: str) -> dict:
    """
    Find the best matching idea for a given user input string.
    Uses keyword overlap scoring - not a simple vlookup.
    Returns the best matching idea dict.
    """
    user_words = set(user_input.lower().split())
    # Also check for substring matches in the full input
    user_lower = user_input.lower()

    best_score = -1
    best_idea = IDEAS[0]

    for idea in IDEAS:
        score = 0

        # Check keyword matches (weighted heavily)
        for kw in idea["keywords"]:
            if kw in user_lower:
                score += 3
            # Partial word match
            for word in user_words:
                if word in kw or kw in word:
                    score += 1

        # Check name match
        if idea["name"].lower() in user_lower:
            score += 10

        # Check slip text overlap
        slip_words = set(idea["slip_text"].lower().split())
        overlap = user_words & slip_words
        score += len(overlap) * 2

        if score > best_score:
            best_score = score
            best_idea = idea

    return best_idea

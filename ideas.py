"""
20 B2B SaaS idea slips and their corresponding vibe-coding prompts.

Each idea has:
  - id: unique identifier (matches paper slip number)
  - name: short catchy name for the idea
  - slip_text: what's printed on the slip of paper
  - keywords: terms used for fuzzy matching when the idea is typed in
  - prompt: the full prompt sent to the code-generation API
"""

IDEAS = [
    {
        "id": 1,
        "name": "InvoiceTracker",
        "slip_text": "Invoice tracking for freelancers",
        "keywords": ["invoice", "freelancer", "tracking", "billing", "payment", "outstanding", "paid", "overdue"],
        "prompt": (
            "Build a clean, minimal web app for freelancers to track invoices. "
            "Include a dashboard showing total outstanding, total paid, and overdue invoices. "
            "Add a form to create new invoices with fields for client name, amount, due date, and status (draft, sent, paid, overdue). "
            "Use a table view to list all invoices with sorting and filtering. "
            "Keep the color palette professional and muted, like a boring accounting tool. "
            "Add a sidebar nav with sections for Dashboard, Invoices, and Clients. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 2,
        "name": "OnboardingChecklist",
        "slip_text": "Employee onboarding checklist tool",
        "keywords": ["onboarding", "employee", "checklist", "hr", "new hire", "orientation", "hiring"],
        "prompt": (
            "Create a web app for HR teams to manage employee onboarding checklists. "
            "The main view shows a list of new hires with their name, start date, department, and a progress bar showing checklist completion. "
            "Clicking a hire opens their checklist with items like 'Set up email,' 'Order laptop,' 'Schedule orientation,' each with a checkbox and assignee. "
            "Include an admin view to create and edit checklist templates. "
            "Use a corporate blue and gray color scheme. Make it look like enterprise software. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 3,
        "name": "ExpenseApproval",
        "slip_text": "Expense report approval system",
        "keywords": ["expense", "report", "approval", "reimburse", "receipt", "spending", "budget"],
        "prompt": (
            "Build an expense report approval workflow app. "
            "Employees can submit expense reports with line items (date, category, amount, receipt upload placeholder). "
            "Managers see a queue of pending reports to approve or reject with comments. "
            "Include a dashboard with monthly spending by category in a bar chart. "
            "Use a boring corporate design with lots of tables, gray backgrounds, and small text. "
            "Add status badges: Pending (yellow), Approved (green), Rejected (red). "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 4,
        "name": "RoomBooker",
        "slip_text": "Meeting room booking platform",
        "keywords": ["meeting", "room", "booking", "calendar", "reserve", "office", "schedule"],
        "prompt": (
            "Create a meeting room booking system for an office. "
            "Show a weekly calendar grid with rooms as rows and time slots as columns. "
            "Rooms should have names like 'Synergy,' 'Innovation Lab,' and 'The Think Tank.' "
            "Users can click a slot to book it with a meeting title and attendee count. "
            "Include a sidebar showing today's bookings and room availability status. "
            "Use a sterile, corporate design. Make it feel like something installed on every computer at a Fortune 500 company. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 5,
        "name": "VendorCompliance",
        "slip_text": "Vendor compliance tracker",
        "keywords": ["vendor", "compliance", "audit", "risk", "contract", "tracker", "regulatory"],
        "prompt": (
            "Build a vendor compliance management dashboard. "
            "Show a table of vendors with columns for name, compliance status (Compliant, At Risk, Non-Compliant), last audit date, contract expiry, and risk score. "
            "Include filters by status and industry. "
            "Add a detail view for each vendor showing their compliance history as a timeline. "
            "Use a very serious, enterprise aesthetic with dark navy headers and lots of data density. "
            "This should look like software nobody enjoys using. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 6,
        "name": "TicketQueue",
        "slip_text": "Customer support ticket queue",
        "keywords": ["support", "ticket", "customer", "helpdesk", "queue", "priority", "service"],
        "prompt": (
            "Create a customer support ticket management system. "
            "Show an inbox-style list of tickets with subject, customer name, priority (Low, Medium, High, Urgent), "
            "status (Open, In Progress, Resolved), and time since creation. "
            "Include a detail panel that shows the conversation thread. "
            "Add a sidebar with quick filters and a small chart showing tickets by status. "
            "Use a bland, functional design. Make it look like Zendesk's less attractive cousin. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 7,
        "name": "WarehouseInventory",
        "slip_text": "Inventory management for warehouses",
        "keywords": ["inventory", "warehouse", "stock", "sku", "reorder", "supply", "management"],
        "prompt": (
            "Build a warehouse inventory management dashboard. "
            "Show a searchable table of products with SKU, name, quantity in stock, reorder point, "
            "location (Aisle-Shelf format like A3-12), and last restocked date. "
            "Highlight rows where quantity is below reorder point in light red. "
            "Include a summary bar at top showing total SKUs, low stock items, and items to reorder. "
            "Use an industrial, no-nonsense design with monospace fonts for SKU numbers. Maximum boringness. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 8,
        "name": "ConsultantTimesheet",
        "slip_text": "Time tracking for consultants",
        "keywords": ["time", "tracking", "consultant", "timesheet", "hours", "billable", "utilization"],
        "prompt": (
            "Create a time tracking app for consulting firms. "
            "The main view is a weekly timesheet grid where consultants log hours per project per day. "
            "Include a dropdown to select the project and a field for notes. "
            "Show a weekly total and a monthly summary with hours by project in a pie chart. "
            "Add an admin view showing all consultants and their utilization rates. "
            "Use a beige and gray color scheme that makes you want to close the tab immediately. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 9,
        "name": "SalesPipeline",
        "slip_text": "Sales pipeline CRM dashboard",
        "keywords": ["sales", "pipeline", "crm", "deals", "leads", "kanban", "forecast"],
        "prompt": (
            "Build a sales pipeline CRM. "
            "Show a kanban board with columns: Lead, Qualified, Proposal, Negotiation, Closed Won, Closed Lost. "
            "Each card shows company name, deal value, and contact person. "
            "Include a sidebar with pipeline summary (total value per stage) and a forecast number. "
            "Add a list view as an alternative to the kanban. "
            "Use a generic SaaS blue and white design. "
            "Include a motivational sales quote somewhere that no one will ever read. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 10,
        "name": "ProjectStatus",
        "slip_text": "Project status reporting tool",
        "keywords": ["project", "status", "report", "milestone", "gantt", "portfolio", "tracking"],
        "prompt": (
            "Create a project status report generator. "
            "Show a list of active projects with name, owner, status (On Track, At Risk, Delayed), percent complete, and next milestone. "
            "Each project has a detail page with a Gantt-style timeline bar, a list of milestones, and a notes section. "
            "Include a portfolio view that shows all projects as colored status dots on a grid. "
            "Make it look like management consulting software. Gray everywhere. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 11,
        "name": "PTOManager",
        "slip_text": "Employee PTO request system",
        "keywords": ["pto", "vacation", "leave", "time off", "request", "approval", "absence"],
        "prompt": (
            "Build a PTO (paid time off) request and approval system. "
            "Employees see their remaining PTO balance, a calendar showing their approved and pending days, and a form to submit new requests. "
            "Managers see a team calendar and a list of pending requests to approve or deny. "
            "Include a policy section showing accrual rates. "
            "Use the most generic corporate design possible with a teal accent color that was clearly picked by committee. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 12,
        "name": "ContractManager",
        "slip_text": "Contract lifecycle management",
        "keywords": ["contract", "legal", "lifecycle", "expiry", "renewal", "management", "agreement"],
        "prompt": (
            "Create a contract management system. "
            "Show a table of contracts with title, counterparty, value, start date, end date, and status (Draft, In Review, Active, Expired). "
            "Include an alert section for contracts expiring in the next 30 days. "
            "Add a detail view with key terms summary and a timeline of status changes. "
            "Use a legal-profession aesthetic: dark backgrounds, serif fonts for contract titles, "
            "and an overwhelming amount of information density. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 13,
        "name": "ITAssetTracker",
        "slip_text": "IT asset tracking spreadsheet app",
        "keywords": ["asset", "it", "device", "laptop", "tracking", "inventory", "hardware", "warranty"],
        "prompt": (
            "Build an IT asset tracking tool. "
            "Show a table of devices with asset tag, type (Laptop, Monitor, Phone), assigned employee, "
            "purchase date, warranty expiry, and condition (New, Good, Fair, Needs Replacement). "
            "Include filters by type and department. "
            "Add a summary showing total assets by type and a count of warranty expirations this quarter. "
            "Design it to look exactly like someone rebuilt a spreadsheet as a web app because their manager asked them to. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 14,
        "name": "OKRDashboard",
        "slip_text": "Quarterly OKR tracking dashboard",
        "keywords": ["okr", "objectives", "key results", "quarterly", "goals", "tracking", "progress"],
        "prompt": (
            "Create an OKR (Objectives and Key Results) tracking dashboard. "
            "Show objectives as expandable cards, each containing 3-4 key results with progress bars and current vs target values. "
            "Include a team filter and a quarter selector. "
            "Add a summary section showing overall company progress as a percentage. "
            "Use red/yellow/green color coding for progress status. "
            "Make it look like the kind of tool that gets mandated company-wide but only 30% of employees actually update. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 15,
        "name": "ShippingDashboard",
        "slip_text": "Shipping logistics coordinator",
        "keywords": ["shipping", "logistics", "tracking", "delivery", "shipment", "carrier", "transit"],
        "prompt": (
            "Build a shipping logistics dashboard. "
            "Show a table of shipments with tracking number, origin, destination, carrier, "
            "status (Preparing, In Transit, Delivered, Delayed), and ETA. "
            "Include a map placeholder showing shipment routes. "
            "Add filters by status and date range. "
            "Show KPIs at top: shipments this month, on-time delivery rate, average transit time. "
            "Use a utilitarian design with lots of data tables and small fonts. Logistics software energy. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 16,
        "name": "BillingManager",
        "slip_text": "SaaS subscription billing manager",
        "keywords": ["subscription", "billing", "saas", "mrr", "churn", "revenue", "payment"],
        "prompt": (
            "Create a subscription billing management tool. "
            "Show a list of customers with name, plan tier (Starter, Pro, Enterprise), MRR, billing cycle, "
            "and payment status (Current, Past Due, Churned). "
            "Include a revenue dashboard with MRR over time line chart and churn rate. "
            "Add a detail view per customer showing billing history and plan changes. "
            "Use a fintech-adjacent design that tries too hard to look modern but still feels like accounting software. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 17,
        "name": "SurveyBuilder",
        "slip_text": "Employee feedback survey builder",
        "keywords": ["survey", "feedback", "employee", "questionnaire", "poll", "hr", "engagement"],
        "prompt": (
            "Build an employee feedback survey tool. "
            "Include a survey builder where admins drag and drop question types (multiple choice, rating scale, free text). "
            "Show a list of active and past surveys with response rates. "
            "Add a results view with bar charts for each question. "
            "Use the most corporate, inoffensive design possible. "
            "Include a stock photo placeholder of diverse coworkers smiling in a conference room. Peak HR software aesthetics. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 18,
        "name": "PipelineMonitor",
        "slip_text": "Data pipeline monitoring dashboard",
        "keywords": ["pipeline", "data", "monitoring", "etl", "dashboard", "engineering", "jobs"],
        "prompt": (
            "Create a data pipeline monitoring dashboard. "
            "Show a list of pipelines with name, last run time, status (Success, Failed, Running), duration, and records processed. "
            "Include a detail view with a log output section and error messages. "
            "Add a chart showing pipeline success rate over the past 30 days. "
            "Use a dark theme with green for success and red for failure, like a terminal. "
            "Make it feel like software that only the data engineering team understands. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 19,
        "name": "FilingTracker",
        "slip_text": "Regulatory filing deadline tracker",
        "keywords": ["regulatory", "filing", "deadline", "compliance", "government", "legal", "regulation"],
        "prompt": (
            "Build a regulatory compliance filing tracker. "
            "Show a calendar view of upcoming filing deadlines with jurisdiction, filing type, responsible person, and days until due. "
            "Include a table view with filters by regulation type and status (Not Started, In Progress, Filed, Overdue). "
            "Add email reminder settings. "
            "Use an extremely serious design with government-website energy. "
            "Dark blue headers, Times New Roman vibes, zero personality. "
            "Make it fully functional with HTML, CSS, and JavaScript in a single file."
        ),
    },
    {
        "id": 20,
        "name": "InvoiceReconciler",
        "slip_text": "Vendor invoice reconciliation tool",
        "keywords": ["reconciliation", "invoice", "vendor", "purchase order", "matching", "accounting", "discrepancy"],
        "prompt": (
            "Create a vendor invoice reconciliation app. "
            "Show a split view: purchase orders on the left, invoices on the right. "
            "Users match invoices to POs and flag discrepancies. "
            "Include a summary showing total matched, unmatched, and discrepancy value. "
            "Add filters by vendor and date range. "
            "Use the driest possible accounting aesthetic: light gray everything, thin borders, "
            "and number formats with two decimal places. The kind of tool that makes you question your career choices. "
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
    user_lower = user_input.lower()

    best_score = -1
    best_idea = IDEAS[0]

    for idea in IDEAS:
        score = 0

        # Check keyword matches (weighted heavily)
        for kw in idea["keywords"]:
            if kw in user_lower:
                score += 3
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

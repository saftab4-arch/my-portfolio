from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Syed Aftab",
    "title": "IT Specialist | Cloud & DevOps Enthusiast",
    "location": "New Jersey, United States",
    "email": "syed.aftab198@gmail.com",
    "linkedin": "https://www.linkedin.com/in/syed-b-9078141a8/",
    "credly": "https://www.credly.com/users/syed-aftab.5fff51e0",
    "about": (
        "Dedicated IT specialist with over 3 years of hands-on experience supporting enterprise, "
        "education, and healthcare environments through end-user support, system administration, "
        "and infrastructure troubleshooting. Currently upskilling in AWS, Terraform, Python, and "
        "PowerShell with a long-term goal of transitioning into Cloud Engineering, DevOps, or "
        "Cybersecurity Operations."
    ),
    "currently_focused": [
        "Learning AWS & Terraform",
        "Scripting in Python & PowerShell",
        "Building DevOps & automation projects for GitHub",
        "Preparing for AWS Certified Solutions Architect",
        "Transitioning into Cloud, DevOps, or Cybersecurity roles",
    ],
    "experience": [
        {
            "title": "Information Technology Specialist",
            "company": "South River Public Schools",
            "type": "Full-time",
            "period": "Jul 2025 – Present",
            "location": "New Jersey, United States",
            "highlights": [
                "Configured, deployed, and maintained Windows laptops for staff and students",
                "Managed Active Directory: user accounts, group policies, and organizational units",
                "Administered Chromebook fleet via Google Admin Console with policy enforcement",
                "Diagnosed Wi-Fi, Ethernet, DNS, and connectivity issues across campus",
                "Installed and supported local and network printers across campus",
                "Provided in-person and remote technical assistance to teachers and staff",
                "Logged and resolved support tickets using the school's helpdesk system",
            ],
        },
        {
            "title": "Help Desk Technician",
            "company": "ASG",
            "type": "Full-time",
            "period": "Dec 2022 – Jun 2025",
            "location": "New Jersey, United States (Hybrid)",
            "highlights": [
                "Provided Tier 1 technical support managing tickets through Zendesk with SLA compliance",
                "Administered Active Directory and Microsoft 365 including onboarding/offboarding workflows",
                "Managed Google Workspace for user provisioning, email configuration, and device management",
                "Performed remote desktop support via TeamViewer for hardware, software, and connectivity issues",
                "Diagnosed LAN/WAN, DNS, DHCP, and Wi-Fi issues across the organization",
                "Performed hardware repair including component replacement and Windows 11 imaging",
            ],
        },
        {
            "title": "NOC Technician – Tier 1",
            "company": "MDS (Micro-Data Systems)",
            "type": "Full-time",
            "period": "Jun 2022 – Aug 2022",
            "location": "New Jersey, United States",
            "highlights": [
                "Desktop support and N-Central remote administration",
                "Office 365 administrator, Exchange, Active Directory and Duo user administration",
            ],
        },
        {
            "title": "IT Support Technician – Tier 2",
            "company": "Hackensack Meridian Health",
            "type": "Full-time",
            "period": "Jan 2022 – Jun 2022",
            "location": "Neptune, New Jersey, United States",
            "highlights": [
                "Supported 2500+ devices across a hospital and 20 affiliate sites",
                "Deployed and configured Chrome devices with Google Admin Console and Imprivata",
                "Windows 10 imaging using PXE boot with inventory and security scans",
                "Active Directory user administration and Citrix workspace management",
                "Used ServiceNow ticketing system for logging, resolving, and escalating issues",
                "Printer configurations, EPIC TDR verification, and secure print registration",
            ],
        },
    ],
    "education": [
        {
            "school": "Western Governors University",
            "degree": "Bachelor of Science – Cybersecurity & Information Assurance",
            "period": "Jan 2020 – Dec 2024",
            "details": (
                "Focused on network security, ethical hacking, threat analysis, and incident response. "
                "Achieved industry-recognized certifications and hands-on experience in securing IT systems, "
                "managing risks, and mitigating vulnerabilities."
            ),
        },
        {
            "school": "Sir Syed University of Engineering & Technology (SSUET)",
            "degree": "Bachelor's Degree – Computer Software Engineering",
            "period": "",
            "details": "",
        },
    ],
    "certifications": [
        {"name": "CompTIA PenTest+ ce", "issuer": "CompTIA", "year": "2024", "expires": "2027"},
        {"name": "CompTIA Network Security Professional (CNSP)", "issuer": "CompTIA", "year": "2024", "expires": "2027"},
        {"name": "CompTIA Network Vulnerability Assessment Professional (CNVP)", "issuer": "CompTIA", "year": "2024", "expires": "2027"},
        {"name": "CompTIA Project+", "issuer": "CompTIA", "year": "2024", "expires": ""},
        {"name": "Associate of ISC2 (SSCP)", "issuer": "ISC2", "year": "2024", "expires": ""},
        {"name": "CompTIA CySA+ ce", "issuer": "CompTIA", "year": "2024", "expires": "2027"},
        {"name": "CompTIA Security Analytics Professional (CSAP)", "issuer": "CompTIA", "year": "2024", "expires": "2027"},
        {"name": "Microsoft Certified: Azure Fundamentals", "issuer": "Microsoft", "year": "2023", "expires": ""},
        {"name": "CompTIA Security+ ce", "issuer": "CompTIA", "year": "2023", "expires": "2026"},
        {"name": "AWS Certified Solutions Architect – Associate", "issuer": "AWS", "year": "2022", "expires": "2025"},
        {"name": "CompTIA Network+ ce", "issuer": "CompTIA", "year": "2022", "expires": "2025"},
        {"name": "EC-Council Certified Encryption Specialist (ECES)", "issuer": "EC-Council", "year": "2022", "expires": ""},
        {"name": "Microsoft Identity and Access Administrator", "issuer": "Microsoft", "year": "2022", "expires": ""},
        {"name": "Microsoft Certified: Security, Compliance, and Identity Fundamentals", "issuer": "Microsoft", "year": "2022", "expires": ""},
        {"name": "Linux Professional Institute Linux Essentials", "issuer": "LPI", "year": "2022", "expires": ""},
        {"name": "AWS Certified Cloud Practitioner", "issuer": "AWS", "year": "2020", "expires": ""},
        {"name": "CompTIA A+ ce", "issuer": "CompTIA", "year": "2020", "expires": ""},
        {"name": "CompTIA IT Fundamentals+", "issuer": "CompTIA", "year": "2020", "expires": ""},
        {"name": "ITIL Foundations (ITIL)", "issuer": "PeopleCert", "year": "2021", "expires": ""},
        {"name": "Microsoft 365 Certified: Fundamentals", "issuer": "Microsoft", "year": "2021", "expires": ""},
    ],
    "skills": {
        "Systems & OS": ["Windows OS", "ChromeOS", "Linux (Essentials)", "MacOS"],
        "Identity & Access": ["Active Directory", "Group Policy", "Microsoft 365 Admin", "Azure AD"],
        "Cloud & DevOps": ["AWS", "Terraform (Learning)", "Python (Learning)", "PowerShell (Learning)"],
        "Networking": ["LAN/WAN", "DNS", "DHCP", "Wi-Fi Troubleshooting", "VPN"],
        "Tools & Platforms": ["Google Admin Console", "N-Central", "TeamViewer", "Zendesk", "ServiceNow", "Citrix"],
        "Security": ["Endpoint Security", "Patch Management", "Antivirus", "PenTest", "Threat Analysis"],
    },
}


@app.route("/")
def index():
    return render_template("index.html", p=profile)


if __name__ == "__main__":
    app.run(debug=True)

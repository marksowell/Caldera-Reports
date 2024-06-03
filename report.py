import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load JSON data from the file
with open('/mnt/data/test_report.json', 'r') as file:
    data = json.load(file)

# Create a PDF report
c = canvas.Canvas("caldera_report.pdf", pagesize=letter)
width, height = letter  # Default letter size

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(30, height - 50, "Caldera Operation Report")
c.setFont("Helvetica", 12)
c.drawString(30, height - 80, f"Operation Name: {data['name']}")

# Details from host_group
y = height - 120
c.setFont("Helvetica-Bold", 14)
c.drawString(30, y, "Host Details:")
y -= 20

# Iterate through host groups
for host in data['host_group']:
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Host Name: {host['host']}")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Username: {host['username']}")
    y -= 20
    c.drawString(50, y, f"PID: {host['pid']}")
    y -= 20
    c.drawString(50, y, f"IP Address: {', '.join(host['host_ip_addrs'])}")
    y -= 40

# Links executed
c.setFont("Helvetica-Bold", 14)
c.drawString(30, y, "Executed Links:")
y -= 20

for link in host['links']:
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Command: {link['plaintext_command']}")
    y -= 20
    c.drawString(50, y, f"Status: {'Success' if link['status'] == 0 else 'Failed'}")
    y -= 20
    c.drawString(50, y, f"Technique: {link['ability']['technique_name']}")
    y -= 20
    c.drawString(50, y, f"Start: {link['collect']}")
    y -= 20
    c.drawString(50, y, f"Finish: {link['finish']}")
    y -= 30

# Check for spacing to add new page if needed
if y < 100:
    c.showPage()
    y = height - 50  # Reset y coordinate after a page

# Finalize the PDF
c.save()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Service offerings and local pricing context for Nairobi
    services = [
        {
            "title": "Regular House Cleaning",
            "desc": "Weekly or bi-weekly deep tidying, dusting, mopping, vacuuming, and kitchen & bathroom sanitisation.",
            "price": "KES 1,500 – 5,000 / visit",
            "badge": "Residential",
            "image": "image/Regular_House_Cleaning.jpg"
        },
        {
            "title": "Deep Cleaning",
            "desc": "Quarterly or move-in/out detail cleaning: inside cabinets, light fixtures, window tracks, appliance rear, and grout.",
            "price": "KES 5,000 – 20,000 / session",
            "badge": "Popular",
            "image": "image/Deep_Cleaning.jpg"
        },
        {
            "title": "Commercial Office Cleaning",
            "desc": "Scheduled maintenance for workstations, reception areas, meeting rooms, and washrooms. Includes consumables supply.",
            "price": "KES 30,000 – 100,000 / month",
            "badge": "Commercial",
            "image": "image/Commercial_Office_Cleaning.jpg"
        },
        {
            "title": "Carpet & Upholstery Cleaning",
            "desc": "Extraction cleaning for carpets, sofas, mattresses, and curtains using professional chemical solutions.",
            "price": "KES 50–100/sqm | Sofa: KES 2k–8k",
            "badge": "Specialised",
            "image": "image/Carpet_Upholstery_Cleaning.jpg"
        },
        {
            "title": "Post-Construction Cleaning",
            "desc": "Removal of construction dust, cement residue, paint splatters, and heavy debris from new or renovated builds.",
            "price": "KES 10,000 – 50,000 / project",
            "badge": "High Margin",
            "image": "image/Post_Construction_Cleaning.jpg"
        },
        {
            "title": "Fumigation & Premium Services",
            "desc": "Pest control, water tank cleaning, exterior pressure washing, pool maintenance, and industrial scrubbing.",
            "price": "Custom Quote",
            "badge": "Premium",
            "image": "image/Fumigation_Premium_Services.jpg"
        }
    ]
    return render_template('index.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
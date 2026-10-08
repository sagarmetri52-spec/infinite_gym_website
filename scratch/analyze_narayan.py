import re

with open('narayan_extracted.css', 'r', encoding='utf-8') as f:
    css = f.read()

print(f"Total CSS chars: {len(css)}")

with open('narayan_bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

print(f"Total JS chars: {len(js)}")

# Search for section components or text
sections = [
    'trust-strip',
    'brand-bar',
    'hero-banner-section',
    'how-it-works-section',
    'quick-help-section',
    'services-grid-section',
    'stats-bar',
    'trending-section',
    'why-choose-section',
    'projects-section',
    'hero-booking-section',
    'testimonials-section',
    'floating-contact-bar',
    'bottom-nav',
    'footer-layout'
]

for s in sections:
    found_css = s in css
    found_js = s in js
    print(f"Section {s}: CSS={found_css}, JS={found_js}")

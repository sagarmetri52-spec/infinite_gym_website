# -*- coding: utf-8 -*-
import re

# 1. Read existing files
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 2. Build the ultra-sleek, perfectly proportioned packages section
packages_html_block = '''    <!-- ==========================================================
         12. OFFICIAL MEMBERSHIP PACKAGES
         ========================================================== -->
    <section class="projects-section" id="packages" style="background: #fffbf5; border-top: 1px solid #fed7aa;">
      <div class="projects-container">
        <div class="projects-header">
          <div class="projects-kicker">🏷️ OFFICIAL MEMBERSHIP TIERS & OFFERS</div>
          <h2 class="projects-title">TRANSPARENT TRAINING PACKAGES</h2>
          <p class="projects-sub">Zero hidden charges. Choose your discipline below to review tenure options and instant WhatsApp discounts.</p>

          <!-- Admission Fee Notice Banner -->
          <div class="admission-fee-banner">
            <span class="admission-fee-icon">🏷️</span>
            <div class="admission-fee-text">
              <strong>NEW JOINER ADMISSION FEE: ₹500/- ONLY</strong>
              <span>(One-time registration fee applicable on new enrollments)</span>
            </div>
          </div>

          <!-- Plan Switcher Tabs -->
          <div class="package-plan-switcher" role="tablist">
            <button type="button" class="package-tab-btn active" id="tabBtnStrength" data-package-tab="strength">
              💪 STRENGTH WORKOUT
            </button>
            <button type="button" class="package-tab-btn" id="tabBtnCardio" data-package-tab="cardio">
              ⚡ CARDIO + STRENGTH COMBO
            </button>
          </div>
        </div>

        <!-- =====================================================
             DESKTOP 5-COLUMN BALANCED GRID (Visible on >= 960px)
             ===================================================== -->
        <!-- TAB 1: STRENGTH PACKAGES -->
        <div class="packages-desktop-view package-tab-content active" id="packageGridStrength">
          <div class="packages-grid">
            <!-- 1 Month -->
            <div class="package-card">
              <div class="package-card-top">
                <span class="package-duration">1 MONTH</span>
                <h3 class="package-name">STARTER</h3>
                <div class="package-price-wrap">
                  <div class="price-final-row">
                    <span class="package-price">₹1,000</span>
                    <span class="package-period">/ month</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Free Weights & Dumbbells</span></li>
                <li><span class="chk">✓</span><span>Olympic Barbells & Racks</span></li>
                <li><span class="chk">✓</span><span>Selectorized Stack Machines</span></li>
                <li><span class="chk">✓</span><span>Floor Guidance & Lockers</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%201-Month%20Strength%20Plan%20(Rs.1000)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN 1-MO (₹1,000)
              </a>
            </div>

            <!-- 3 Months Popular -->
            <div class="package-card highlight-popular">
              <span class="package-popular-badge">★ POPULAR CHOICE</span>
              <div class="package-card-top">
                <span class="package-duration">3 MONTHS</span>
                <h3 class="package-name">POWER PACK</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹3,000</span>
                    <span class="package-discount-pill">SAVE ₹500</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹2,500</span>
                    <span class="package-period">/ 3 mo</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Complete Strength Equipment</span></li>
                <li><span class="chk">✓</span><span>Custom Workout Split</span></li>
                <li><span class="chk">✓</span><span>Form Checks & Overload</span></li>
                <li><span class="chk">✓</span><span>Lockers & Amenities</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%203-Months%20Strength%20Plan%20(Rs.2500)." target="_blank" rel="noopener noreferrer" class="package-btn primary">
                JOIN 3-MO (₹2,500)
              </a>
            </div>

            <!-- 6 Months -->
            <div class="package-card">
              <div class="package-card-top">
                <span class="package-duration">6 MONTHS</span>
                <h3 class="package-name">TRANSFORM</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹6,000</span>
                    <span class="package-discount-pill">SAVE ₹1,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹5,000</span>
                    <span class="package-period">/ 6 mo</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Unrestricted Machine Access</span></li>
                <li><span class="chk">✓</span><span>Hypertrophy Nutrition Guide</span></li>
                <li><span class="chk">✓</span><span>Bi-Weekly Progress Reviews</span></li>
                <li><span class="chk">✓</span><span>Priority Coach Guidance</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%206-Months%20Strength%20Plan%20(Rs.5000)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN 6-MO (₹5,000)
              </a>
            </div>

            <!-- 12 Months Best Value -->
            <div class="package-card highlight-gold">
              <span class="package-popular-badge gold">★ BEST VALUE</span>
              <div class="package-card-top">
                <span class="package-duration">12 MONTHS</span>
                <h3 class="package-name">ANNUAL ELITE</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹12,000</span>
                    <span class="package-discount-pill">SAVE ₹2,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹10,000</span>
                    <span class="package-period">/ year (~₹833/mo)</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Dual Branch Reciprocal Access</span></li>
                <li><span class="chk">✓</span><span>Full Year Progression Plan</span></li>
                <li><span class="chk">✓</span><span>Free Guest Passes Included</span></li>
                <li><span class="chk">✓</span><span>Maximum Annual Savings</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%2012-Months%20Strength%20Plan%20(Rs.10000)." target="_blank" rel="noopener noreferrer" class="package-btn primary">
                JOIN ANNUAL (₹10,000)
              </a>
            </div>

            <!-- Couple 12 Months -->
            <div class="package-card package-card-couple">
              <span class="package-popular-badge couple">👥 COUPLE PASS (12 MO)</span>
              <div class="package-card-top">
                <span class="package-duration">12 MONTHS COUPLE</span>
                <h3 class="package-name">COUPLE PASS</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹24,000</span>
                    <span class="package-discount-pill couple">SAVE ₹6,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹18,000</span>
                    <span class="package-period">/ 2 persons (1 yr)</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Full Year for 2 Persons</span></li>
                <li><span class="chk">✓</span><span>Dual Branch Access Included</span></li>
                <li><span class="chk">✓</span><span>Joint Workout Split Routines</span></li>
                <li><span class="chk">✓</span><span>Huge ₹6,000 Direct Savings</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%2012-Months%20Couple%20Package%20for%20Strength%20(Rs.18000)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN COUPLE (₹18,000)
              </a>
            </div>
          </div>
        </div>

        <!-- TAB 2: CARDIO + STRENGTH PACKAGES -->
        <div class="packages-desktop-view package-tab-content" id="packageGridCardio" style="display: none;">
          <div class="packages-grid">
            <!-- 1 Month Cardio -->
            <div class="package-card">
              <div class="package-card-top">
                <span class="package-duration">1 MONTH</span>
                <h3 class="package-name">STARTER COMBO</h3>
                <div class="package-price-wrap">
                  <div class="price-final-row">
                    <span class="package-price">₹1,500</span>
                    <span class="package-period">/ month</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Free Weights & Strength Area</span></li>
                <li><span class="chk">✓</span><span>Cardio Zone & Treadmills</span></li>
                <li><span class="chk">✓</span><span>Spin Bikes & Ellipticals</span></li>
                <li><span class="chk">✓</span><span>Floor Guidance & Lockers</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%201-Month%20Cardio%20%2B%20Strength%20Plan%20(Rs.1500)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN 1-MO (₹1,500)
              </a>
            </div>

            <!-- 3 Months Cardio Popular -->
            <div class="package-card highlight-popular">
              <span class="package-popular-badge">★ POPULAR COMBO</span>
              <div class="package-card-top">
                <span class="package-duration">3 MONTHS</span>
                <h3 class="package-name">POWER COMBO</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹4,500</span>
                    <span class="package-discount-pill">SAVE ₹500</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹4,000</span>
                    <span class="package-period">/ 3 mo</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Full Cardio Floor + Iron Zone</span></li>
                <li><span class="chk">✓</span><span>Fat Loss + Hypertrophy Split</span></li>
                <li><span class="chk">✓</span><span>Stamina & Conditioning</span></li>
                <li><span class="chk">✓</span><span>Form Checks & Diet Framework</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%203-Months%20Cardio%20%2B%20Strength%20Plan%20(Rs.4000)." target="_blank" rel="noopener noreferrer" class="package-btn primary">
                JOIN 3-MO (₹4,000)
              </a>
            </div>

            <!-- 6 Months Cardio -->
            <div class="package-card">
              <div class="package-card-top">
                <span class="package-duration">6 MONTHS</span>
                <h3 class="package-name">BURN & BUILD</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹9,000</span>
                    <span class="package-discount-pill">SAVE ₹1,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹8,000</span>
                    <span class="package-period">/ 6 mo</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Unrestricted Access to All Floors</span></li>
                <li><span class="chk">✓</span><span>Comprehensive Fat Loss Plan</span></li>
                <li><span class="chk">✓</span><span>Bi-Weekly Measurement Audits</span></li>
                <li><span class="chk">✓</span><span>Dedicated Locker & Guidance</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%206-Months%20Cardio%20%2B%20Strength%20Plan%20(Rs.8000)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN 6-MO (₹8,000)
              </a>
            </div>

            <!-- 12 Months Cardio Best Value -->
            <div class="package-card highlight-gold">
              <span class="package-popular-badge gold">★ BEST VALUE</span>
              <div class="package-card-top">
                <span class="package-duration">12 MONTHS</span>
                <h3 class="package-name">TOTAL ELITE</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹18,000</span>
                    <span class="package-discount-pill">SAVE ₹3,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹15,000</span>
                    <span class="package-period">/ year (~₹1,250/mo)</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Dual Branch Reciprocal Access</span></li>
                <li><span class="chk">✓</span><span>Full Cardio + Hypertrophy Roadmap</span></li>
                <li><span class="chk">✓</span><span>Free Guest Passes & Priority</span></li>
                <li><span class="chk">✓</span><span>Maximum Total Transformation</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%2012-Months%20Cardio%20%2B%20Strength%20Plan%20(Rs.15000)." target="_blank" rel="noopener noreferrer" class="package-btn primary">
                JOIN ANNUAL (₹15,000)
              </a>
            </div>

            <!-- Couple 12 Months Cardio -->
            <div class="package-card package-card-couple">
              <span class="package-popular-badge couple">👥 COUPLE COMBO (12 MO)</span>
              <div class="package-card-top">
                <span class="package-duration">12 MONTHS COUPLE</span>
                <h3 class="package-name">COUPLE COMBO</h3>
                <div class="package-price-wrap">
                  <div class="price-strikethrough-group">
                    <span class="price-strikethrough">₹36,000</span>
                    <span class="package-discount-pill couple">SAVE ₹8,000</span>
                  </div>
                  <div class="price-final-row">
                    <span class="package-price">₹28,000</span>
                    <span class="package-period">/ 2 persons (1 yr)</span>
                  </div>
                </div>
              </div>
              <ul class="package-features">
                <li><span class="chk">✓</span><span>Full Cardio + Strength for 2 Persons</span></li>
                <li><span class="chk">✓</span><span>Access to Both Karnataka Hubs</span></li>
                <li><span class="chk">✓</span><span>Dual Custom Workout Routines</span></li>
                <li><span class="chk">✓</span><span>Huge ₹8,000 Direct Bundle Savings</span></li>
              </ul>
              <a href="https://wa.me/918618932114?text=Hello%20Intense%20World%2C%20I%20want%20to%20join%20the%2012-Months%20Couple%20Package%20for%20Cardio%20%2B%20Strength%20(Rs.28000)." target="_blank" rel="noopener noreferrer" class="package-btn outline">
                JOIN COUPLE (₹28,000)
              </a>
            </div>
          </div>
        </div>

        <!-- =====================================================
             MOBILE INTERACTIVE PLAN SPOTLIGHT (< 960px)
             Zero vertical scrolling! Tap or swipe between tenures.
             ===================================================== -->
        <div class="packages-mobile-spotlight" id="mobilePackageSpotlight">
          <!-- Tenure Selection Row -->
          <div class="spotlight-tenure-header">
            <span class="spotlight-label">SELECT DURATION:</span>
            <div class="spotlight-pills-bar" id="mobileTenurePills">
              <button type="button" class="s-pill-btn active" data-index="0">1M</button>
              <button type="button" class="s-pill-btn" data-index="1">3M ★</button>
              <button type="button" class="s-pill-btn" data-index="2">6M</button>
              <button type="button" class="s-pill-btn gold" data-index="3">12M 👑</button>
              <button type="button" class="s-pill-btn couple" data-index="4">Couple 👥</button>
            </div>
          </div>

          <!-- Dynamic Spotlight Card with Side Controls -->
          <div class="spotlight-card-stage">
            <button type="button" class="s-arrow-btn prev" id="sPrevBtn" aria-label="Previous Plan">❮</button>

            <div class="spotlight-card-container" id="spotlightCardTarget">
              <!-- Injected by JS with smooth fade & slide -->
            </div>

            <button type="button" class="s-arrow-btn next" id="sNextBtn" aria-label="Next Plan">❯</button>
          </div>

          <!-- Indicator Dots -->
          <div class="spotlight-dots-row" id="spotlightDots">
            <button type="button" class="s-dot active" data-index="0" aria-label="1 Month Plan"></button>
            <button type="button" class="s-dot" data-index="1" aria-label="3 Months Plan"></button>
            <button type="button" class="s-dot" data-index="2" aria-label="6 Months Plan"></button>
            <button type="button" class="s-dot" data-index="3" aria-label="12 Months Plan"></button>
            <button type="button" class="s-dot" data-index="4" aria-label="Couple Plan"></button>
          </div>
        </div>
      </div>
    </section>'''

# Replace the packages section in index.html
packages_pattern = re.compile(r'<!-- =+\s*12\.\s*OFFICIAL MEMBERSHIP PACKAGES\s*=+\s*-->.*?<!-- =+\s*13\.\s*OUR 2 BRANCHES', re.DOTALL)
replacement = packages_html_block + '\n\n    <!-- ==========================================================\n         13. OUR 2 BRANCHES'

new_html = packages_pattern.sub(replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Updated index.html packages markup successfully!')

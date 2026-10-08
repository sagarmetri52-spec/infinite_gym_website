# -*- coding: utf-8 -*-

# 1. Update app.js
app_js_content = '''/**
 * Intense World Gym — Core Interactive Engine
 * High-performance, zero-bloat vanilla JavaScript
 */

const packagesData = {
  strength: [
    {
      id: "strength-1m",
      duration: "1 MONTH PLAN",
      name: "STARTER",
      price: "₹1,000",
      period: "/ month",
      originalPrice: "",
      discount: "",
      badge: "",
      badgeClass: "",
      features: [
        "Free Weights & Dumbbells",
        "Olympic Barbells & Power Racks",
        "Selectorized Stack Machines",
        "Floor Guidance & Lockers"
      ],
      btnText: "JOIN 1-MONTH (₹1,000)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 1-Month Strength Plan (Rs.1000)."
    },
    {
      id: "strength-3m",
      duration: "3 MONTHS PLAN",
      name: "POWER PACK",
      price: "₹2,500",
      period: "/ 3 months",
      originalPrice: "₹3,000",
      discount: "SAVE ₹500",
      badge: "★ POPULAR CHOICE",
      badgeClass: "popular",
      features: [
        "Complete Strength Equipment Access",
        "Custom Workout Split Routine",
        "Form Checks & Overload Tracking",
        "Lockers & Full Changing Amenities"
      ],
      btnText: "JOIN 3-MONTHS (₹2,500)",
      btnClass: "primary",
      waText: "Hello Intense World, I want to join the 3-Months Strength Plan (Rs.2500)."
    },
    {
      id: "strength-6m",
      duration: "6 MONTHS PLAN",
      name: "TRANSFORM",
      price: "₹5,000",
      period: "/ 6 months",
      originalPrice: "₹6,000",
      discount: "SAVE ₹1,000",
      badge: "",
      badgeClass: "",
      features: [
        "Unrestricted Machine Access",
        "Hypertrophy Nutrition Blueprint",
        "Bi-Weekly Progress Reviews",
        "Priority Floor Coach Guidance"
      ],
      btnText: "JOIN 6-MONTHS (₹5,000)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 6-Months Strength Plan (Rs.5000)."
    },
    {
      id: "strength-12m",
      duration: "12 MONTHS PLAN",
      name: "ANNUAL ELITE",
      price: "₹10,000",
      period: "/ year (~₹833/mo)",
      originalPrice: "₹12,000",
      discount: "SAVE ₹2,000",
      badge: "★ BEST VALUE",
      badgeClass: "gold",
      features: [
        "Dual Branch Reciprocal Access",
        "Full Year Progression Roadmap",
        "Free Guest Passes Included",
        "Maximum Annual Cost Savings"
      ],
      btnText: "JOIN ANNUAL (₹10,000)",
      btnClass: "primary",
      waText: "Hello Intense World, I want to join the 12-Months Strength Plan (Rs.10000)."
    },
    {
      id: "strength-couple",
      duration: "12 MONTHS COUPLE",
      name: "COUPLE PASS",
      price: "₹18,000",
      period: "/ 2 persons (1 yr)",
      originalPrice: "₹24,000",
      discount: "SAVE ₹6,000",
      badge: "👥 COUPLE PASS (12 MO)",
      badgeClass: "couple",
      features: [
        "Full Year Membership for 2 Persons",
        "Reciprocal Dual Branch Access",
        "Joint Workout Split Routines",
        "Direct ₹6,000 Bundle Savings"
      ],
      btnText: "JOIN COUPLE (₹18,000)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 12-Months Couple Package for Strength (Rs.18000)."
    }
  ],
  cardio: [
    {
      id: "cardio-1m",
      duration: "1 MONTH PLAN",
      name: "STARTER COMBO",
      price: "₹1,500",
      period: "/ month",
      originalPrice: "",
      discount: "",
      badge: "",
      badgeClass: "",
      features: [
        "Free Weights & Strength Area",
        "Dedicated Cardio & Treadmills",
        "Spin Bikes & Ellipticals",
        "Floor Guidance & Lockers"
      ],
      btnText: "JOIN 1-MONTH (₹1,500)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 1-Month Cardio + Strength Plan (Rs.1500)."
    },
    {
      id: "cardio-3m",
      duration: "3 MONTHS PLAN",
      name: "POWER COMBO",
      price: "₹4,000",
      period: "/ 3 months",
      originalPrice: "₹4,500",
      discount: "SAVE ₹500",
      badge: "★ POPULAR COMBO",
      badgeClass: "popular",
      features: [
        "Full Cardio Floor + Iron Zone",
        "Fat Loss + Hypertrophy Hybrid Split",
        "Conditioning & Stamina Tracking",
        "Form Checks & Diet Framework"
      ],
      btnText: "JOIN 3-MONTHS (₹4,000)",
      btnClass: "primary",
      waText: "Hello Intense World, I want to join the 3-Months Cardio + Strength Plan (Rs.4000)."
    },
    {
      id: "cardio-6m",
      duration: "6 MONTHS PLAN",
      name: "BURN & BUILD",
      price: "₹8,000",
      period: "/ 6 months",
      originalPrice: "₹9,000",
      discount: "SAVE ₹1,000",
      badge: "",
      badgeClass: "",
      features: [
        "Unrestricted Access to All Floors",
        "Comprehensive Fat Loss Plan",
        "Bi-Weekly Measurement Audits",
        "Dedicated Locker & Priority Support"
      ],
      btnText: "JOIN 6-MONTHS (₹8,000)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 6-Months Cardio + Strength Plan (Rs.8000)."
    },
    {
      id: "cardio-12m",
      duration: "12 MONTHS PLAN",
      name: "TOTAL ELITE",
      price: "₹15,000",
      period: "/ year (~₹1,250/mo)",
      originalPrice: "₹18,000",
      discount: "SAVE ₹3,000",
      badge: "★ BEST VALUE",
      badgeClass: "gold",
      features: [
        "Dual Branch Reciprocal Access",
        "Full Cardio + Hypertrophy Plan",
        "Free Guest Passes & Priority",
        "Maximum Total Value Savings"
      ],
      btnText: "JOIN ANNUAL (₹15,000)",
      btnClass: "primary",
      waText: "Hello Intense World, I want to join the 12-Months Cardio + Strength Plan (Rs.15000)."
    },
    {
      id: "cardio-couple",
      duration: "12 MONTHS COUPLE",
      name: "COUPLE COMBO",
      price: "₹28,000",
      period: "/ 2 persons (1 yr)",
      originalPrice: "₹36,000",
      discount: "SAVE ₹8,000",
      badge: "👥 COUPLE COMBO (12 MO)",
      badgeClass: "couple",
      features: [
        "Full Cardio + Strength for 2 Persons",
        "Access to Both Karnataka Hubs",
        "Dual Custom Workout Routines",
        "Direct ₹8,000 Direct Bundle Savings"
      ],
      btnText: "JOIN COUPLE COMBO (₹28,000)",
      btnClass: "outline",
      waText: "Hello Intense World, I want to join the 12-Months Couple Package for Cardio + Strength (Rs.28000)."
    }
  ]
};

let currentCategory = 'strength';
let currentTenureIndex = 0;

document.addEventListener('DOMContentLoaded', () => {
  initLiveBranchStatus();
  initPackageEngine();
  initBranchGalleries();
  initLightbox();
  initGoalFinder();
  initMobileMenu();
  initStatCounters();
});

/* 1. Live Branch Status Engine (IST UTC+5:30) */
function initLiveBranchStatus() {
  const updateStatus = () => {
    const now = new Date();
    const utcTime = now.getTime() + now.getTimezoneOffset() * 60000;
    const istTime = new Date(utcTime + 3600000 * 5.5);
    
    const day = istTime.getDay();
    const hours = istTime.getHours();
    const minutes = istTime.getMinutes();
    const currentDecimalTime = hours + minutes / 60;

    // Chikkaballapur (Mon-Sat 4:00 AM - 10:00 PM)
    const chikkaStatusEl = document.getElementById('chikkaLiveStatus');
    if (chikkaStatusEl) {
      const dot = chikkaStatusEl.querySelector('.status-indicator');
      const text = chikkaStatusEl.querySelector('.status-text');

      if (day === 0) {
        if (dot) dot.className = 'status-indicator closed';
        if (text) text.textContent = 'CLOSED TODAY (SUNDAY)';
      } else if (currentDecimalTime >= 4.0 && currentDecimalTime < 22.0) {
        if (dot) dot.className = 'status-indicator';
        if (text) text.textContent = 'OPEN NOW • 4:00 AM – 10:00 PM';
      } else {
        if (dot) dot.className = 'status-indicator closed';
        if (text) text.textContent = 'CLOSED NOW • OPENS 4:00 AM';
      }
    }

    // Shidlaghatta (Mon-Sat 5AM-10AM & 5PM-10PM)
    const shidStatusEl = document.getElementById('shidLiveStatus');
    if (shidStatusEl) {
      const dot = shidStatusEl.querySelector('.status-indicator');
      const text = shidStatusEl.querySelector('.status-text');

      if (day === 0) {
        if (dot) dot.className = 'status-indicator closed';
        if (text) text.textContent = 'CLOSED TODAY (SUNDAY)';
      } else if (currentDecimalTime >= 5.0 && currentDecimalTime < 10.0) {
        if (dot) dot.className = 'status-indicator';
        if (text) text.textContent = 'OPEN NOW (MORNING: 5AM–10AM)';
      } else if (currentDecimalTime >= 17.0 && currentDecimalTime < 22.0) {
        if (dot) dot.className = 'status-indicator';
        if (text) text.textContent = 'OPEN NOW (EVENING: 5PM–10PM)';
      } else if (currentDecimalTime >= 10.0 && currentDecimalTime < 17.0) {
        if (dot) dot.className = 'status-indicator closed';
        if (text) text.textContent = 'CLOSED NOW • OPENS 5:00 PM TODAY';
      } else {
        if (dot) dot.className = 'status-indicator closed';
        if (text) text.textContent = 'CLOSED NOW • OPENS 5:00 AM TOMORROW';
      }
    }
  };

  updateStatus();
  setInterval(updateStatus, 60000);
}

/* 2. Unified Package Engine (Desktop 5-Grid & Mobile Spotlight Card) */
function initPackageEngine() {
  const tabStrength = document.getElementById('tabBtnStrength');
  const tabCardio = document.getElementById('tabBtnCardio');
  const deskStrength = document.getElementById('packageGridStrength');
  const deskCardio = document.getElementById('packageGridCardio');

  const sPills = document.querySelectorAll('.s-pill-btn');
  const sDots = document.querySelectorAll('.s-dot');
  const sPrev = document.getElementById('sPrevBtn');
  const sNext = document.getElementById('sNextBtn');
  const targetCard = document.getElementById('spotlightCardTarget');

  const renderMobileSpotlightCard = () => {
    if (!targetCard) return;
    const plan = packagesData[currentCategory][currentTenureIndex];
    if (!plan) return;

    let badgeHtml = '';
    if (plan.badge) {
      const cls = plan.badgeClass ? ` ${plan.badgeClass}` : '';
      badgeHtml = `<span class="spotlight-badge${cls}">${plan.badge}</span>`;
    }

    let strikeHtml = '';
    if (plan.originalPrice) {
      strikeHtml = `
        <div class="price-strikethrough-group">
          <span class="price-strikethrough">${plan.originalPrice}</span>
          <span class="package-discount-pill ${plan.badgeClass}">${plan.discount}</span>
        </div>
      `;
    }

    const featuresList = plan.features.map(f => `<li><span class="chk">✓</span><span>${f}</span></li>`).join('');
    const waUrl = `https://wa.me/918618932114?text=${encodeURIComponent(plan.waText)}`;

    targetCard.innerHTML = `
      <div class="spotlight-inner-card ${plan.badgeClass ? 'highlight-' + plan.badgeClass : ''}">
        ${badgeHtml}
        <div class="spotlight-card-top">
          <span class="package-duration">${plan.duration}</span>
          <h3 class="package-name">${plan.name}</h3>
          <div class="package-price-wrap">
            ${strikeHtml}
            <div class="price-final-row">
              <span class="package-price">${plan.price}</span>
              <span class="package-period">${plan.period}</span>
            </div>
          </div>
        </div>

        <ul class="package-features">
          ${featuresList}
        </ul>

        <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="package-btn ${plan.btnClass}">
          ${plan.btnText} ↗
        </a>
      </div>
    `;

    // Sync pills and dots
    sPills.forEach((p, i) => p.classList.toggle('active', i === currentTenureIndex));
    sDots.forEach((d, i) => d.classList.toggle('active', i === currentTenureIndex));
  };

  // Discipline Category Tabs
  if (tabStrength && tabCardio) {
    tabStrength.addEventListener('click', () => {
      currentCategory = 'strength';
      tabStrength.classList.add('active');
      tabCardio.classList.remove('active');
      if (deskStrength) deskStrength.style.display = '';
      if (deskCardio) deskCardio.style.display = 'none';
      renderMobileSpotlightCard();
    });

    tabCardio.addEventListener('click', () => {
      currentCategory = 'cardio';
      tabCardio.classList.add('active');
      tabStrength.classList.remove('active');
      if (deskStrength) deskStrength.style.display = 'none';
      if (deskCardio) deskCardio.style.display = '';
      renderMobileSpotlightCard();
    });
  }

  // Mobile Tenure Pill Buttons
  sPills.forEach(pill => {
    pill.addEventListener('click', () => {
      currentTenureIndex = parseInt(pill.getAttribute('data-index') || '0', 10);
      renderMobileSpotlightCard();
    });
  });

  // Mobile Dots
  sDots.forEach(dot => {
    dot.addEventListener('click', () => {
      currentTenureIndex = parseInt(dot.getAttribute('data-index') || '0', 10);
      renderMobileSpotlightCard();
    });
  });

  // Mobile Previous / Next Arrows
  if (sPrev) {
    sPrev.addEventListener('click', () => {
      currentTenureIndex = (currentTenureIndex - 1 + 5) % 5;
      renderMobileSpotlightCard();
    });
  }

  if (sNext) {
    sNext.addEventListener('click', () => {
      currentTenureIndex = (currentTenureIndex + 1) % 5;
      renderMobileSpotlightCard();
    });
  }

  // Swipe support on Mobile Spotlight Card
  if (targetCard) {
    let touchStartX = 0;
    let touchEndX = 0;

    targetCard.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    targetCard.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchEndX < touchStartX - 40) {
        // Swipe left -> next
        currentTenureIndex = (currentTenureIndex + 1) % 5;
        renderMobileSpotlightCard();
      } else if (touchEndX > touchStartX + 40) {
        // Swipe right -> prev
        currentTenureIndex = (currentTenureIndex - 1 + 5) % 5;
        renderMobileSpotlightCard();
      }
    }, { passive: true });
  }

  // Render initial card
  renderMobileSpotlightCard();
}

/* 3. Branch Interactive Photo Galleries (Both Locations) */
function initBranchGalleries() {
  const galleries = document.querySelectorAll('.branch-gallery');
  galleries.forEach(gallery => {
    const mainImg = gallery.querySelector('.branch-gallery-main img');
    const mainTrigger = gallery.querySelector('.branch-gallery-main');
    const thumbBtns = gallery.querySelectorAll('.branch-thumb-btn');

    if (!mainImg || !mainTrigger || !thumbBtns.length) return;

    thumbBtns.forEach(thumb => {
      thumb.addEventListener('click', () => {
        thumbBtns.forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');

        const newSrc = thumb.getAttribute('data-img');
        const caption = thumb.getAttribute('data-caption');

        mainImg.src = newSrc;
        mainTrigger.setAttribute('data-img', newSrc);
        mainTrigger.setAttribute('data-caption', caption);
      });
    });
  });
}

/* 4. Lightbox Modal */
function initLightbox() {
  const modal = document.getElementById('lightboxModal');
  const img = document.getElementById('lightboxImg');
  const caption = document.getElementById('lightboxCaption');
  const closeBtn = document.getElementById('lightboxClose');
  const backdrop = document.getElementById('lightboxBackdrop');
  const triggers = document.querySelectorAll('.lightbox-trigger');

  if (!modal || !img || !caption) return;

  const openLightbox = (src, text) => {
    img.src = src;
    caption.textContent = text || 'Intense World Gym Facility';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    modal.classList.remove('active');
    img.src = '';
    document.body.style.overflow = '';
  };

  triggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      if (e.target.closest('a') || e.target.closest('button.package-btn')) return;
      const src = trigger.getAttribute('data-img');
      const cap = trigger.getAttribute('data-caption');
      if (src) openLightbox(src, cap);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (backdrop) backdrop.addEventListener('click', closeLightbox);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeLightbox();
    }
  });
}

/* 5. Goal Finder WhatsApp Engine */
function initGoalFinder() {
  const form = document.getElementById('goalFinderForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('userNameInput')?.value.trim() || 'Athlete';
    const goal = document.getElementById('userGoal')?.value || 'Strength & Muscle Hypertrophy';
    const branch = document.getElementById('preferredBranch')?.value || '1st Branch — Chikkaballapur';
    const exp = document.getElementById('trainingExperience')?.value || 'Beginner';
    const timing = document.getElementById('preferredTiming')?.value || 'Morning';

    const isShidlaghatta = branch.toLowerCase().includes('shidlaghatta');
    const targetPhone = isShidlaghatta ? '917019474149' : '918618932114';

    const message = `Hello Intense World Gym! 👋%0A%0AMy Name: *${encodeURIComponent(name)}*%0A🎯 Primary Goal: *${encodeURIComponent(goal)}*%0A📍 Preferred Branch: *${encodeURIComponent(branch)}*%0A💪 Experience Level: *${encodeURIComponent(exp)}*%0A⏰ Preferred Shift: *${encodeURIComponent(timing)}*%0A%0AI would like to get a tailored starter workout breakdown and know about current membership offers. Thank you!`;

    const waUrl = `https://wa.me/${targetPhone}?text=${message}`;
    window.open(waUrl, '_blank');
  });
}

/* 6. Mobile Dropdown Menu */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileToggle');
  const drop = document.getElementById('mobileDrop');

  if (!toggleBtn || !drop) return;

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    drop.style.display = (drop.style.display === 'flex') ? 'none' : 'flex';
  });

  document.addEventListener('click', (e) => {
    if (!drop.contains(e.target) && e.target !== toggleBtn) {
      drop.style.display = 'none';
    }
  });

  drop.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      drop.style.display = 'none';
    });
  });
}

/* 7. Stat Counters */
function initStatCounters() {
  const counters = document.querySelectorAll('.counter-num');
  if (!counters.length) return;

  let animated = false;

  const animateCounters = () => {
    counters.forEach(counter => {
      const target = parseFloat(counter.getAttribute('data-target'));
      const decimals = parseInt(counter.getAttribute('data-decimals') || '0', 10);
      const duration = 1500;
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentVal = (1 - Math.pow(1 - progress, 3)) * target;

        counter.textContent = currentVal.toFixed(decimals);

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          counter.textContent = target.toFixed(decimals);
        }
      };

      requestAnimationFrame(updateCount);
    });
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        animateCounters();
      }
    });
  }, { threshold: 0.2 });

  counters.forEach(c => observer.observe(c));
}
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_content)

# 2. Append pristine styles to styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    existing_css = f.read()

spotlight_styles = '''

/* ==========================================================
   PACKAGE SPOTLIGHT & BALANCED GRID (PROPORTION PERFECTION)
   ========================================================== */

/* 1. Desktop 5-Column Grid */
.packages-desktop-view {
  width: 100% !important;
  max-width: 1260px !important;
  margin: 0 auto !important;
}
.packages-grid {
  display: grid !important;
  grid-template-columns: repeat(5, 1fr) !important;
  gap: 16px !important;
  align-items: stretch !important;
}

.package-card {
  background: #ffffff !important;
  border: 1.5px solid var(--border) !important;
  border-radius: 18px !important;
  padding: 20px 14px 18px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  position: relative !important;
  box-shadow: 0 4px 16px rgba(6, 20, 67, 0.05) !important;
  transition: all 0.25s ease !important;
  min-width: 0 !important;
}
.package-card:hover {
  transform: translateY(-4px) !important;
  border-color: var(--orange) !important;
  box-shadow: 0 12px 30px rgba(249, 115, 22, 0.16) !important;
}

.package-card.highlight-popular {
  border: 2px solid var(--orange) !important;
  box-shadow: 0 8px 24px rgba(249, 115, 22, 0.2) !important;
}
.package-card.highlight-gold {
  border: 2px solid #eab308 !important;
  background: linear-gradient(180deg, #fffdf2 0%, #ffffff 100%) !important;
}
.package-card.package-card-couple {
  border: 2px solid #e11d48 !important;
  background: linear-gradient(180deg, #fff5f7 0%, #ffffff 100%) !important;
}

.package-popular-badge, .spotlight-badge {
  position: absolute !important;
  top: -11px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: var(--orange) !important;
  color: #ffffff !important;
  font-size: 0.62rem !important;
  font-weight: 900 !important;
  letter-spacing: 0.04em !important;
  padding: 3px 10px !important;
  border-radius: 999px !important;
  white-space: nowrap !important;
  box-shadow: 0 3px 8px rgba(249, 115, 22, 0.35) !important;
  z-index: 2 !important;
}
.package-popular-badge.gold, .spotlight-badge.gold {
  background: #eab308 !important;
  color: #061443 !important;
  box-shadow: 0 3px 8px rgba(234, 179, 8, 0.35) !important;
}
.package-popular-badge.couple, .spotlight-badge.couple {
  background: #e11d48 !important;
  color: #ffffff !important;
  box-shadow: 0 3px 8px rgba(225, 29, 72, 0.35) !important;
}

.package-duration {
  font-size: 0.66rem !important;
  font-weight: 900 !important;
  color: #64748b !important;
  letter-spacing: 0.04em !important;
  display: block !important;
  margin-bottom: 2px !important;
}
.package-name {
  font-size: 1.12rem !important;
  font-weight: 900 !important;
  color: var(--navy) !important;
  margin-bottom: 6px !important;
  letter-spacing: -0.01em !important;
}

.price-strikethrough-group {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  margin-bottom: 2px !important;
}
.price-strikethrough {
  font-size: 0.76rem !important;
  color: #94a3b8 !important;
  text-decoration: line-through !important;
  font-weight: 700 !important;
}
.package-discount-pill {
  font-size: 0.6rem !important;
  font-weight: 900 !important;
  background: #fff7ed !important;
  color: #c2410c !important;
  padding: 1px 6px !important;
  border-radius: 999px !important;
  border: 1px solid #fed7aa !important;
}
.package-discount-pill.couple {
  background: #ffe4e6 !important;
  color: #e11d48 !important;
  border-color: #fecdd3 !important;
}

.price-final-row {
  display: flex !important;
  align-items: baseline !important;
  gap: 4px !important;
}
.package-price {
  font-size: 1.55rem !important;
  font-weight: 900 !important;
  color: var(--navy) !important;
  line-height: 1 !important;
  letter-spacing: -0.02em !important;
}
.package-period {
  font-size: 0.68rem !important;
  color: #64748b !important;
  font-weight: 700 !important;
}

.package-features {
  display: flex !important;
  flex-direction: column !important;
  gap: 7px !important;
  margin: 14px 0 16px !important;
  flex: 1 !important;
  padding: 0 !important;
  list-style: none !important;
}
.package-features li {
  display: flex !important;
  align-items: flex-start !important;
  gap: 6px !important;
  font-size: 0.74rem !important;
  color: #334155 !important;
  line-height: 1.3 !important;
}
.package-features .chk {
  color: var(--orange) !important;
  font-weight: 900 !important;
  font-size: 0.8rem !important;
  flex-shrink: 0 !important;
}

.package-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  padding: 10px 6px !important;
  font-size: 0.74rem !important;
  font-weight: 900 !important;
  border-radius: 8px !important;
  transition: all 0.2s ease !important;
  text-align: center !important;
  text-decoration: none !important;
}
.package-btn.primary {
  background: var(--orange) !important;
  color: #ffffff !important;
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3) !important;
}
.package-btn.primary:hover {
  background: var(--orange-dark) !important;
}
.package-btn.outline {
  background: #ffffff !important;
  color: var(--navy) !important;
  border: 1.5px solid var(--border) !important;
}
.package-btn.outline:hover {
  border-color: var(--orange) !important;
  color: var(--orange) !important;
  background: #fff7ed !important;
}

/* 2. Mobile Interactive Spotlight (< 960px) */
.packages-mobile-spotlight {
  display: none;
  width: 100%;
  max-width: 440px;
  margin: 0 auto;
  flex-direction: column;
  gap: 14px;
}

.spotlight-tenure-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.spotlight-label {
  font-size: 0.7rem;
  font-weight: 900;
  color: #64748b;
  letter-spacing: 0.05em;
}
.spotlight-pills-bar {
  display: flex;
  background: #e2e8f0;
  padding: 4px;
  border-radius: 999px;
  border: 1.5px solid #cbd5e1;
  gap: 4px;
  width: 100%;
  justify-content: space-between;
}
.s-pill-btn {
  flex: 1;
  padding: 8px 4px;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 800;
  color: #475569;
  background: transparent;
  border: none;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  text-align: center;
}
.s-pill-btn.active {
  background: var(--navy);
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(6, 20, 67, 0.25);
}
.s-pill-btn.gold.active {
  background: #eab308;
  color: #061443;
}
.s-pill-btn.couple.active {
  background: #e11d48;
  color: #ffffff;
}

.spotlight-card-stage {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
  width: 100%;
}
.s-arrow-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #ffffff;
  border: 1.5px solid var(--border);
  color: var(--navy);
  font-size: 1rem;
  font-weight: 900;
  display: grid;
  place-items: center;
  cursor: pointer;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: all 0.2s ease;
}
.s-arrow-btn:hover {
  border-color: var(--orange);
  color: var(--orange);
}

.spotlight-card-container {
  flex: 1;
  min-width: 0;
}
.spotlight-inner-card {
  background: #ffffff;
  border: 2px solid var(--border);
  border-radius: 18px;
  padding: 22px 18px 18px;
  box-shadow: 0 8px 24px rgba(6, 20, 67, 0.08);
  position: relative;
  transition: all 0.25s ease;
  animation: fadeIn 0.25s ease-out;
}
.spotlight-inner-card.highlight-popular {
  border-color: var(--orange);
  box-shadow: 0 10px 28px rgba(249, 115, 22, 0.2);
}
.spotlight-inner-card.highlight-gold {
  border-color: #eab308;
  background: linear-gradient(180deg, #fffdf2 0%, #ffffff 100%);
}
.spotlight-inner-card.highlight-couple {
  border-color: #e11d48;
  background: linear-gradient(180deg, #fff5f7 0%, #ffffff 100%);
}

.spotlight-dots-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 4px;
}
.s-dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: #cbd5e1;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  padding: 0;
}
.s-dot.active {
  width: 22px;
  background: var(--orange);
}

@keyframes fadeIn {
  from { opacity: 0.6; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 960px) {
  .packages-desktop-view {
    display: none !important;
  }
  .packages-mobile-spotlight {
    display: flex !important;
  }
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(existing_css + spotlight_styles)

print('Updated app.js and styles.css with pristine spotlight packages engine!')

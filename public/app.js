/**
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

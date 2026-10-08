# -*- coding: utf-8 -*-

with open('styles.css', 'r', encoding='utf-8') as f:
    narayan_base_css = f.read()

# Enhanced, polished CSS with perfect image aspect-ratios, crisp borders, and clean packages
enhanced_css = narayan_base_css + """

/* ==========================================================
   IMAGE ASPECT-RATIOS, CRISP BORDERS & PROPORTION FIXES
   Prevents any vertical enlargement/stretching across all screens
   ========================================================== */

/* 1. Global Image & Media Discipline */
img {
  max-width: 100%;
  height: auto;
  object-fit: cover;
  display: block;
}

/* 2. Hero Image Container */
.hero-image-container {
  aspect-ratio: 4 / 3 !important;
  max-height: 380px !important;
  width: 100% !important;
  border-radius: 20px !important;
  border: 3px solid var(--orange) !important;
  position: relative !important;
  overflow: hidden !important;
  box-shadow: 0 14px 34px rgba(6, 20, 67, 0.16) !important;
  background: var(--navy) !important;
}
.hero-slide-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  display: block !important;
}

/* 3. Why Choose / Manifesto Banner Image */
.why-choose-image-stack {
  max-width: 1000px;
  margin: 0 auto;
}
.why-choose-banner-img {
  aspect-ratio: 16 / 9 !important;
  max-height: 440px !important;
  width: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  border: 3px solid var(--orange) !important;
  border-radius: 20px !important;
  display: block !important;
  box-shadow: 0 14px 36px rgba(6, 20, 67, 0.16) !important;
}

/* 4. Trending Featured Carousel Box */
.trending-carousel-box {
  max-width: 1000px !important;
  border: 3px solid var(--orange) !important;
  border-radius: 20px !important;
  overflow: hidden !important;
  box-shadow: var(--shadow-lg) !important;
}
.trending-carousel-track {
  aspect-ratio: 16 / 9 !important;
  max-height: 440px !important;
  width: 100% !important;
  position: relative !important;
  overflow: hidden !important;
  background: #000 !important;
}
.trending-carousel-slide img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
}

/* 5. Framed Facility Cards */
.services-framed-container {
  display: grid !important;
  grid-template-columns: repeat(3, 1fr) !important;
  gap: 24px !important;
  max-width: 1200px !important;
  margin: 0 auto !important;
}
.service-framed-card {
  border: 3px solid var(--border) !important;
  border-radius: 20px !important;
  overflow: hidden !important;
  background: #fff !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 8px 24px rgba(6, 20, 67, 0.08) !important;
  display: flex !important;
  flex-direction: column !important;
}
.service-framed-card:hover {
  border-color: var(--orange) !important;
  transform: translateY(-6px) !important;
  box-shadow: 0 18px 40px rgba(249, 115, 22, 0.2) !important;
}
.service-framed-image-box {
  aspect-ratio: 16 / 10 !important;
  max-height: 240px !important;
  width: 100% !important;
  overflow: hidden !important;
  position: relative !important;
  background: var(--navy) !important;
  border-bottom: 2px solid var(--border) !important;
}
.service-framed-image-box img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  transition: transform 0.5s ease !important;
}
.service-framed-card:hover .service-framed-image-box img {
  transform: scale(1.08) !important;
}

/* 6. Structured Program Cards */
.projects-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 20px !important;
  max-width: 1200px !important;
  margin: 0 auto !important;
}
.project-card {
  border: 2px solid var(--border) !important;
  border-radius: 18px !important;
  overflow: hidden !important;
  background: #fff !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 6px 20px rgba(6, 20, 67, 0.06) !important;
  display: flex !important;
  flex-direction: column !important;
  position: relative !important;
}
.project-card::before {
  content: "" !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 4px !important;
  background: linear-gradient(90deg, #f97316, #fb923c) !important;
  z-index: 2 !important;
}
.project-card:hover {
  border-color: var(--orange) !important;
  transform: translateY(-6px) !important;
  box-shadow: 0 16px 36px rgba(249, 115, 22, 0.2) !important;
}
.project-photo-box {
  aspect-ratio: 16 / 10 !important;
  max-height: 200px !important;
  width: 100% !important;
  overflow: hidden !important;
  background: var(--navy) !important;
  border-bottom: 2px solid var(--orange) !important;
}
.project-photo-box img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  transition: transform 0.5s ease !important;
}
.project-card:hover .project-photo-box img {
  transform: scale(1.08) !important;
}

/* 7. Quick Help Carousel Images */
.quick-help-image-wrapper {
  aspect-ratio: 1 / 1 !important;
  border-radius: 16px !important;
  border: 2px solid var(--border) !important;
  overflow: hidden !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
}
.quick-help-image-wrapper img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
}

/* 8. Branch Gallery Main & Thumbnails */
.branch-gallery-main {
  aspect-ratio: 16 / 9 !important;
  max-height: 280px !important;
  width: 100% !important;
  border-radius: 14px !important;
  border: 2px solid var(--border) !important;
  overflow: hidden !important;
  cursor: pointer !important;
  background: var(--navy) !important;
}
.branch-gallery-main img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
}
.branch-thumb-btn {
  width: 68px !important;
  height: 50px !important;
  border-radius: 8px !important;
  border: 2px solid var(--border) !important;
  overflow: hidden !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}
.branch-thumb-btn img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
}
.branch-thumb-btn.active, .branch-thumb-btn:hover {
  border-color: var(--orange) !important;
  transform: translateY(-2px) !important;
}

/* ==========================================================
   PACKAGES SECTION PERFECTION (CLEAN 5-COLUMN & RESPONSIVE)
   ========================================================== */
.packages-grid {
  display: grid !important;
  grid-template-columns: repeat(5, 1fr) !important;
  gap: 16px !important;
  max-width: 1240px !important;
  margin: 0 auto !important;
  align-items: stretch !important;
}

@media (max-width: 1180px) {
  .packages-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 14px !important;
  }
}
@media (max-width: 768px) {
  .packages-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
  }
  .package-card.package-card-couple {
    grid-column: 1 / -1 !important;
  }
}

.package-card {
  background: #fff !important;
  border: 2px solid var(--border) !important;
  border-radius: 18px !important;
  padding: 20px 14px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  position: relative !important;
  box-shadow: 0 4px 16px rgba(6, 20, 67, 0.05) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  min-width: 0 !important;
}
.package-card:hover {
  transform: translateY(-5px) !important;
  border-color: var(--orange) !important;
  box-shadow: 0 14px 32px rgba(249, 115, 22, 0.16) !important;
}

.package-card.highlight-popular {
  border: 2.5px solid var(--orange) !important;
  box-shadow: 0 8px 24px rgba(249, 115, 22, 0.22) !important;
}
.package-card.highlight-gold {
  border: 2.5px solid #eab308 !important;
  background: linear-gradient(180deg, #fffef5 0%, #ffffff 100%) !important;
}
.package-card.package-card-couple {
  border: 2.5px solid #e11d48 !important;
  background: linear-gradient(180deg, #fff5f7 0%, #ffffff 100%) !important;
}

.package-popular-badge {
  position: absolute !important;
  top: -11px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: var(--orange) !important;
  color: #fff !important;
  font-size: 0.62rem !important;
  font-weight: 900 !important;
  letter-spacing: 0.04em !important;
  padding: 3px 10px !important;
  border-radius: 999px !important;
  white-space: nowrap !important;
  box-shadow: 0 3px 8px rgba(249, 115, 22, 0.35) !important;
  z-index: 2 !important;
}
.package-popular-badge.gold {
  background: #eab308 !important;
  color: #061443 !important;
  box-shadow: 0 3px 8px rgba(234, 179, 8, 0.35) !important;
}
.package-popular-badge.couple {
  background: #e11d48 !important;
  color: #fff !important;
  box-shadow: 0 3px 8px rgba(225, 29, 72, 0.35) !important;
}

.package-card-top {
  margin-bottom: 12px !important;
}
.package-duration {
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  color: var(--muted) !important;
  letter-spacing: 0.04em !important;
  display: block !important;
  margin-bottom: 3px !important;
}
.package-name {
  font-size: 1.15rem !important;
  font-weight: 900 !important;
  color: var(--navy) !important;
  margin-bottom: 6px !important;
  letter-spacing: -0.01em !important;
}
.package-price-wrap {
  display: flex !important;
  flex-direction: column !important;
}
.price-strikethrough-group {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  margin-bottom: 2px !important;
}
.price-strikethrough {
  font-size: 0.78rem !important;
  color: var(--muted) !important;
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
}
.package-period {
  font-size: 0.7rem !important;
  color: var(--muted) !important;
  font-weight: 700 !important;
}
.package-features {
  display: flex !important;
  flex-direction: column !important;
  gap: 8px !important;
  margin: 14px 0 18px !important;
  flex: 1 !important;
}
.package-features li {
  display: flex !important;
  align-items: flex-start !important;
  gap: 6px !important;
  font-size: 0.75rem !important;
  color: #334155 !important;
  line-height: 1.3 !important;
}
.package-features .chk {
  color: var(--orange) !important;
  font-weight: 900 !important;
  flex-shrink: 0 !important;
}
.package-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  padding: 10px !important;
  font-size: 0.75rem !important;
  font-weight: 900 !important;
  border-radius: 8px !important;
  transition: all 0.2s ease !important;
  text-align: center !important;
  text-decoration: none !important;
}
.package-btn.primary {
  background: var(--orange) !important;
  color: #fff !important;
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.35) !important;
}
.package-btn.primary:hover {
  background: var(--orange-dark) !important;
}
.package-btn.outline {
  background: #fff !important;
  color: var(--navy) !important;
  border: 1.5px solid var(--border) !important;
}
.package-btn.outline:hover {
  border-color: var(--orange) !important;
  color: var(--orange) !important;
  background: #fff7ed !important;
}

/* ==========================================================
   MOBILE SIZING OVERRIDES (< 768px)
   ========================================================== */
@media (max-width: 768px) {
  .hero-image-container {
    aspect-ratio: 3 / 4 !important;
    max-height: 220px !important;
    border-radius: 12px !important;
    border-width: 2px !important;
  }
  .why-choose-banner-img {
    aspect-ratio: 16 / 10 !important;
    max-height: 240px !important;
    border-radius: 14px !important;
    border-width: 2px !important;
  }
  .trending-carousel-box {
    border-radius: 14px !important;
    border-width: 2px !important;
  }
  .trending-carousel-track {
    aspect-ratio: 16 / 10 !important;
    max-height: 240px !important;
  }
  .service-framed-card {
    border-width: 2px !important;
    border-radius: 12px !important;
  }
  .service-framed-image-box {
    aspect-ratio: 7 / 10 !important;
    max-height: 160px !important;
  }
  .project-card {
    border-radius: 12px !important;
  }
  .project-photo-box {
    aspect-ratio: 1 / 1 !important;
    max-height: 140px !important;
  }
  .package-card {
    padding: 12px 10px !important;
    border-radius: 12px !important;
  }
  .package-name {
    font-size: 0.95rem !important;
  }
  .package-price {
    font-size: 1.25rem !important;
  }
  .package-period {
    font-size: 0.6rem !important;
  }
  .package-features {
    gap: 5px !important;
    margin: 8px 0 12px !important;
  }
  .package-features li {
    font-size: 0.65rem !important;
    line-height: 1.2 !important;
  }
  .package-btn {
    padding: 7px 4px !important;
    font-size: 0.62rem !important;
  }
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(enhanced_css)

print('Generated enhanced styles.css with perfect borders and aspect-ratios!')

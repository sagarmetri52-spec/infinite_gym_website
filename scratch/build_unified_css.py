import re

with open('narayan_extracted.css', 'r', encoding='utf-8') as f:
    narayan_css = f.read()

# Additional custom styling for gym-specific elements (Package switcher tabs, branch live clock & photo switcher, FAQ accordion, lightbox, and modals)
gym_css_extension = """
/* ==========================================================
   INTENSE WORLD GYM — COMPONENT EXTENSIONS
   Styled to 100% match the Narayan Plumbing Design System
   ========================================================== */

/* 1. Admission Fee Alert & Package Switcher */
.admission-fee-banner {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--white);
  border: 2px dashed var(--orange);
  border-radius: 999px;
  padding: 8px 20px;
  margin: 12px auto 20px;
  box-shadow: 0 4px 14px rgba(249, 115, 22, 0.1);
  text-align: left;
}
.admission-fee-icon {
  font-size: 1.2rem;
}
.admission-fee-text strong {
  font-size: 0.82rem;
  font-weight: 900;
  color: var(--orange-dark);
  display: block;
}
.admission-fee-text span {
  font-size: 0.68rem;
  color: var(--muted);
  display: block;
}

.package-plan-switcher {
  display: inline-flex;
  background: #f1f5f9;
  padding: 4px;
  border-radius: 999px;
  border: 1px solid var(--border);
  gap: 4px;
  margin-bottom: 24px;
}
.package-tab-btn {
  padding: 10px 22px;
  border-radius: 999px;
  font-size: 0.82rem;
  font-weight: 900;
  color: var(--text);
  background: transparent;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}
.package-tab-btn.active {
  background: var(--orange);
  color: #fff;
  box-shadow: 0 4px 14px rgba(249, 115, 22, 0.35);
}

/* 2. Packages 5-Column Grid */
.packages-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  max-width: 1200px;
  margin: 0 auto;
}
.package-card {
  background: #fff;
  border: 2px solid var(--border);
  border-radius: 18px;
  padding: 22px 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  box-shadow: 0 6px 20px rgba(6, 20, 67, 0.06);
  transition: all 0.3s ease;
}
.package-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange);
  box-shadow: 0 16px 36px rgba(249, 115, 22, 0.18);
}
.package-popular-badge {
  position: absolute;
  top: -11px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--orange);
  color: #fff;
  font-size: 0.62rem;
  font-weight: 900;
  letter-spacing: 0.05em;
  padding: 3px 10px;
  border-radius: 999px;
  white-space: nowrap;
  box-shadow: 0 3px 8px rgba(249, 115, 22, 0.4);
}
.package-popular-badge.gold {
  background: #eab308;
  color: #061443;
}
.package-popular-badge.couple {
  background: #e11d48;
  color: #fff;
}
.package-card.highlight-popular {
  border-color: var(--orange);
  box-shadow: 0 8px 24px rgba(249, 115, 22, 0.25);
}
.package-card.highlight-gold {
  border-color: #eab308;
  background: linear-gradient(180deg, #fffdf0 0%, #ffffff 100%);
}
.package-card.package-card-couple {
  border-color: #e11d48;
  background: linear-gradient(180deg, #fff5f7 0%, #ffffff 100%);
}
.package-card-top {
  margin-bottom: 14px;
}
.package-duration {
  font-size: 0.68rem;
  font-weight: 900;
  color: var(--muted);
  letter-spacing: 0.04em;
  display: block;
  margin-bottom: 4px;
}
.package-name {
  font-size: 1.15rem;
  font-weight: 900;
  color: var(--navy);
  margin-bottom: 8px;
}
.package-price-wrap {
  display: flex;
  flex-direction: column;
}
.price-strikethrough-group {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 2px;
}
.price-strikethrough {
  font-size: 0.8rem;
  color: var(--muted);
  text-decoration: line-through;
  font-weight: 700;
}
.package-discount-pill {
  font-size: 0.62rem;
  font-weight: 900;
  background: #fff7ed;
  color: #c2410c;
  padding: 1px 6px;
  border-radius: 999px;
  border: 1px solid #fed7aa;
}
.package-discount-pill.couple {
  background: #ffe4e6;
  color: #e11d48;
  border-color: #fecdd3;
}
.price-final-row {
  display: flex;
  align-items: baseline;
  gap: 4px;
}
.package-price {
  font-size: 1.55rem;
  font-weight: 900;
  color: var(--navy);
  line-height: 1;
}
.package-period {
  font-size: 0.72rem;
  color: var(--muted);
  font-weight: 700;
}
.package-features {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 14px 0 20px;
  flex: 1;
}
.package-features li {
  display: flex;
  align-items: flex-start;
  gap: 6px;
  font-size: 0.76rem;
  color: #334155;
  line-height: 1.35;
}
.package-features .chk {
  color: var(--orange);
  font-weight: 900;
  flex-shrink: 0;
}
.package-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 11px;
  font-size: 0.76rem;
  font-weight: 900;
  border-radius: 8px;
  transition: all 0.2s ease;
  text-align: center;
  text-decoration: none;
}
.package-btn.primary {
  background: var(--orange);
  color: #fff;
  box-shadow: 0 4px 12px rgba(249, 115, 22, 0.35);
}
.package-btn.primary:hover {
  background: var(--orange-dark);
}
.package-btn.outline {
  background: #fff;
  color: var(--navy);
  border: 1.5px solid var(--border);
}
.package-btn.outline:hover {
  border-color: var(--orange);
  color: var(--orange);
  background: #fff7ed;
}

/* 3. Branches 2-Column Showcase */
.branches-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  max-width: 1200px;
  margin: 0 auto;
}
.branch-card {
  background: #fff;
  border: 2px solid var(--border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(6, 20, 67, 0.08);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}
.branch-card:hover {
  border-color: var(--orange);
  box-shadow: 0 16px 40px rgba(249, 115, 22, 0.16);
}
.branch-card-header {
  padding: 20px 22px 14px;
  background: #f8fafc;
  border-bottom: 1px solid var(--border);
}
.branch-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}
.branch-pill {
  font-size: 0.68rem;
  font-weight: 900;
  letter-spacing: 0.04em;
  padding: 4px 10px;
  border-radius: 999px;
}
.branch-pill.main {
  background: #fff7ed;
  color: #c2410c;
  border: 1px solid #fed7aa;
}
.branch-pill.second {
  background: #fef9c3;
  color: #854d0e;
  border: 1px solid #fde047;
}
.branch-live-status {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 999px;
  background: #fff;
  border: 1px solid var(--border);
}
.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 6px #22c55e;
}
.status-indicator.closed {
  background: #ef4444;
  box-shadow: 0 0 6px #ef4444;
}
.branch-card-title {
  font-size: 1.15rem;
  font-weight: 900;
  color: var(--navy);
  margin-bottom: 2px;
}
.branch-card-category {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--muted);
}
.branch-gallery {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.branch-gallery-main {
  position: relative;
  aspect-ratio: 16/9;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  background: var(--navy);
}
.branch-gallery-main img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.branch-gallery-main:hover img {
  transform: scale(1.05);
}
.branch-gallery-overlay-hint {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(6, 20, 67, 0.85);
  backdrop-filter: blur(4px);
  color: #fff;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 6px;
}
.branch-gallery-thumbs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}
.branch-gallery-thumbs::-webkit-scrollbar {
  display: none;
}
.branch-thumb-btn {
  width: 64px;
  height: 48px;
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid var(--border);
  flex-shrink: 0;
  opacity: 0.7;
  cursor: pointer;
  transition: all 0.2s ease;
}
.branch-thumb-btn.active, .branch-thumb-btn:hover {
  opacity: 1;
  border-color: var(--orange);
  transform: translateY(-2px);
}
.branch-thumb-btn img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.branch-card-body {
  padding: 16px 22px 22px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.branch-info-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.branch-info-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: #fff7ed;
  border: 1px solid #ffedd5;
  color: var(--orange);
  display: grid;
  place-items: center;
  flex-shrink: 0;
}
.branch-info-icon.wa {
  background: rgba(37, 211, 102, 0.12);
  border-color: rgba(37, 211, 102, 0.3);
  color: #25d366;
}
.branch-info-content h5 {
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 2px;
}
.branch-info-content address {
  font-style: normal;
  font-size: 0.82rem;
  color: #334155;
  line-height: 1.4;
}
.plus-code {
  font-size: 0.75rem;
  color: #c2410c;
  font-weight: 700;
  margin-top: 2px;
}
.plus-code.gold {
  color: #854d0e;
}
.phone-link {
  font-size: 0.88rem;
  font-weight: 800;
  color: var(--navy);
  text-decoration: none;
}
.phone-link:hover {
  color: var(--orange);
}
.branch-hours-list {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin-top: 2px;
}
.branch-hours-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.76rem;
  color: #334155;
}
.hours-open {
  color: #15803d;
  font-weight: 800;
}
.branch-hours-item.closed strong {
  color: #b91c1c;
}
.branch-map-embed {
  position: relative;
  width: 100%;
  height: 160px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border);
  margin: 4px 0;
}
.branch-map-embed iframe {
  width: 100%;
  height: 100%;
  border: 0;
}
.branch-actions-wrap {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 6px;
}
.branch-btn-subgroup {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

/* 4. FAQ Accordion */
.faq-accordion-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 900px;
  margin: 0 auto;
}
.faq-item {
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 16px 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  transition: all 0.2s ease;
}
.faq-item[open] {
  border-color: var(--orange);
  box-shadow: 0 6px 20px rgba(249, 115, 22, 0.12);
}
.faq-question {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--navy);
  cursor: pointer;
  list-style: none;
}
.faq-question::-webkit-details-marker {
  display: none;
}
.faq-icon {
  font-size: 1.3rem;
  color: var(--orange);
  font-weight: 900;
  transition: transform 0.2s ease;
}
.faq-item[open] .faq-icon {
  transform: rotate(45deg);
}
.faq-answer {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  font-size: 0.88rem;
  color: #334155;
  line-height: 1.6;
}

/* 5. Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  z-index: 10000;
  display: none;
  place-items: center;
  padding: 16px;
}
.lightbox-modal.active {
  display: grid;
}
.lightbox-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(6, 20, 67, 0.88);
  backdrop-filter: blur(8px);
}
.lightbox-content {
  position: relative;
  z-index: 2;
  max-width: 900px;
  width: 100%;
  background: var(--navy);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
  border: 2px solid rgba(255, 255, 255, 0.15);
}
.lightbox-close {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.6);
  color: #fff;
  font-size: 1.2rem;
  display: grid;
  place-items: center;
  border: none;
  cursor: pointer;
  z-index: 3;
}
.lightbox-content img {
  width: 100%;
  max-height: 75vh;
  object-fit: contain;
  background: #000;
}
.lightbox-caption {
  padding: 12px 18px;
  background: #030a24;
  color: #fff;
  font-size: 0.85rem;
  font-weight: 700;
  text-align: center;
}

/* 6. Legal Modal */
.legal-overlay {
  z-index: 10000;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(6px);
  place-items: center;
  padding: 16px;
  position: fixed;
  inset: 0;
}
.legal-dialog {
  border: 2px solid var(--orange);
  background: #fff;
  border-radius: 16px;
  width: min(520px, 100%);
  padding: 28px 24px;
  position: relative;
  box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}
.legal-close {
  background: #1f2937;
  color: #fff;
  border: 0;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  font-size: 1.2rem;
  position: absolute;
  top: 12px;
  right: 12px;
  cursor: pointer;
}

/* 7. Button Styles */
.btn-cult {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 12px 18px;
  border-radius: 10px;
  font-size: 0.82rem;
  font-weight: 800;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
}
.btn-cult-primary {
  background: var(--navy);
  color: #fff;
}
.btn-cult-primary:hover {
  background: var(--orange);
}
.btn-cult-outline {
  background: #fff;
  color: var(--navy);
  border: 1.5px solid var(--border);
}
.btn-cult-outline:hover {
  border-color: var(--orange);
  color: var(--orange);
  background: #fff7ed;
}
.btn-cult-whatsapp {
  background: #25d366;
  color: #fff;
}
.btn-cult-whatsapp:hover {
  background: #1eb85a;
}
"""

unified_css = narayan_css + "\n\n" + gym_css_extension

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(unified_css)

print('Successfully generated unified styles.css with full Narayan core + gym extensions!')

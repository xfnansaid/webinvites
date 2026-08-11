const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf-8');

// Replace filter chips
const filterPattern = /<!-- CATEGORY FILTER CHIPS -->[\s\S]*?<!-- TEMPLATES GRID -->/;
const newFilters = `<!-- CATEGORY FILTER CHIPS -->
            <div class="filter-bar-wrap" style="justify-content: center; margin-bottom: 40px;">
                <div class="filter-chips-container" id="filterChips" style="justify-content: center;">
                    <button class="filter-chip active" data-filter="premium" style="font-size: 0.9rem; padding: 12px 24px;">
                        <span class="material-symbols-outlined" style="font-size: 18px;">workspace_premium</span> Premium (₹499)
                    </button>
                    <button class="filter-chip" data-filter="standard" style="font-size: 0.9rem; padding: 12px 24px;">
                        <span class="material-symbols-outlined" style="font-size: 18px;">star_border</span> Standard (₹249)
                    </button>
                </div>
            </div>

            <!-- TEMPLATES GRID -->`;
html = html.replace(filterPattern, newFilters);

// Features section replacement
const featuresPattern = /<!-- FEATURES SECTION -->[\s\S]*?<!-- FAQ ACCORDION SECTION -->/;
const newFeatures = `<!-- FEATURES SECTION -->
        <section id="features" class="features-section">
            <div class="section-header">
                <span class="eyebrow-tag">03 · Packages</span>
                <h2 class="section-heading">Compare our <span style="font-style: italic; font-family: var(--font-serif); color: var(--champagne-600);">options</span></h2>
                <p style="color: var(--ink-muted); margin-top: 8px;">Everything you need to invite your guests beautifully.</p>
            </div>

            <div style="max-width: 1000px; margin: 40px auto 0; padding: 0 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
                
                <!-- Standard Features -->
                <div style="background: var(--bg-card); border-radius: 20px; padding: 40px 32px; border: 1.5px solid var(--border-subtle); box-shadow: var(--shadow-soft);">
                    <div style="text-align: center; margin-bottom: 24px;">
                        <h3 style="font-family: var(--font-serif); font-size: 1.8rem; color: var(--ink);">Standard</h3>
                        <div style="font-size: 2rem; font-weight: 700; color: var(--emerald-primary); margin-top: 8px;">₹249</div>
                        <p style="font-size: 0.88rem; color: var(--ink-muted); margin-top: 8px;">Perfect for simple, elegant invitations.</p>
                    </div>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 16px;">
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--sage-600); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Beautiful Event Details</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Display date, time, and venue clearly.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--sage-600); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Host & Family Info</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Include names of bride, groom, and parents.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--sage-600); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">WhatsApp Friendly</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Easily shareable via WhatsApp link.</span>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Premium Features -->
                <div style="background: var(--bg-card); border-radius: 20px; padding: 40px 32px; border: 2px solid var(--emerald-primary); box-shadow: var(--shadow-md); position: relative;">
                    <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: var(--emerald-primary); color: #FFF; padding: 4px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">Most Popular</div>
                    <div style="text-align: center; margin-bottom: 24px;">
                        <h3 style="font-family: var(--font-serif); font-size: 1.8rem; color: var(--emerald-primary);">Premium</h3>
                        <div style="font-size: 2rem; font-weight: 700; color: var(--emerald-primary); margin-top: 8px;">₹499</div>
                        <p style="font-size: 0.88rem; color: var(--ink-muted); margin-top: 8px;">The ultimate digital invitation experience.</p>
                    </div>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 16px;">
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Everything in Standard</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">All the essential details.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Interactive Countdown Timer</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Build excitement for the big day.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Google Maps Navigation</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">One-click directions to the venue.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Live RSVP Tracking</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Guests can confirm attendance easily.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Couple Stories & Photos</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Share your journey and photo gallery.</span>
                            </div>
                        </li>
                        <li style="display: flex; align-items: flex-start; gap: 12px;">
                            <span class="material-symbols-outlined" style="color: var(--emerald-primary); font-size: 20px; margin-top: 2px;">check_circle</span>
                            <div>
                                <strong style="display: block; font-size: 0.95rem; color: var(--ink);">Save to Calendar</strong>
                                <span style="font-size: 0.85rem; color: var(--ink-muted);">Guests can instantly add to Google Calendar.</span>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- FAQ ACCORDION SECTION -->`;
html = html.replace(featuresPattern, newFeatures);

// Replace cards
const cardPattern = /<div class="tp-card"[\s\S]*?<div class="tp-actions">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/g;

html = html.replace(cardPattern, (match) => {
    const isStandard = match.includes('299') || match.includes('199') || match.includes('249');
    const tier = isStandard ? 'standard' : 'premium';
    const price = tier === 'standard' ? '₹249' : '₹499';
    const bgColor = tier === 'standard' ? 'var(--ink-soft)' : 'var(--emerald-primary)';

    let newCard = match;
    
    // Remove categories & price attrs
    newCard = newCard.replace(/ data-categories="[^"]*"/g, '');
    newCard = newCard.replace(/ data-price="[^"]*"/g, '');
    
    // Add data-tier
    newCard = newCard.replace(/<div class="tp-card"( selected-active)? data-id="([^"]+)" data-title="([^"]+)"/g, 
        \`<div class="tp-card"$1 data-id="$2" data-title="$3" data-tier="\${tier}"\`);

    if (tier === 'standard' && !newCard.includes('style="display: none;"')) {
        newCard = newCard.replace(/<div class="tp-card"/, '<div class="tp-card" style="display: none;"');
    }

    newCard = newCard.replace(/<span class="tp-badge-price">.*?<\/span>/, 
        \`<span class="tp-badge-price" style="background: \${bgColor};">\${price}</span>\`);

    newCard = newCard.replace(/<span class="tp-category-tag">.*?<\/span>/, 
        \`<span class="tp-category-tag">\${tier.charAt(0).toUpperCase() + tier.slice(1)}</span>\`);

    const urlMatch = newCard.match(/openPreviewModal\('([^']+)',\s*'([^']+)'\)/);
    if (urlMatch) {
        const url = urlMatch[1];
        const title = urlMatch[2];
        const idMatch = newCard.match(/data-id="([^"]+)"/);
        const cardId = idMatch ? idMatch[1] : 'template';
        
        const newActions = \`<div class="tp-actions">
                            <button class="btn-card-preview" style="width: 100%; border-color: var(--emerald-primary); color: var(--emerald-primary); font-size: 0.95rem; padding: 12px;" onclick="openPreviewModal('\${url}', '\${title}', '\${cardId}')">Preview Design</button>
                        </div>\`;
        newCard = newCard.replace(/<div class="tp-actions">[\s\S]*?<\/div>\s*<\/div>/, newActions + '\\n                    </div>');
    }
    return newCard;
});

fs.writeFileSync('index.html', html, 'utf-8');
console.log('Update complete.');

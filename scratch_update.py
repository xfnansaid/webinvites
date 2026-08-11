import re

with open('c:/Users/moham/Documents/Default Project/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace filter chips
filter_pattern = r'<!-- CATEGORY FILTER CHIPS -->.*?<!-- TEMPLATES GRID -->'
new_filters = '''<!-- CATEGORY FILTER CHIPS -->
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

            <!-- TEMPLATES GRID -->'''
html = re.sub(filter_pattern, new_filters, html, flags=re.DOTALL)

# Now loop through all tp-cards and update them
# Pattern to find each card
def replace_card(match):
    card_content = match.group(0)
    
    # Randomly assign standard or premium for the demo if not specified
    is_standard = '299' in card_content or '199' in card_content or '249' in card_content
    tier = 'standard' if is_standard else 'premium'
    price = '₹249' if tier == 'standard' else '₹499'
    
    # 1. Update data attributes
    # Remove data-categories and data-price
    card_content = re.sub(r' data-categories="[^"]*"', '', card_content)
    card_content = re.sub(r' data-price="[^"]*"', '', card_content)
    
    # Replace data-id="xyz" data-title="xyz" with ... data-tier="..."
    card_content = re.sub(r'<div class="tp-card"( selected-active)? data-id="([^"]+)" data-title="([^"]+)"', 
                          rf'<div class="tp-card"\1 data-id="\2" data-title="\3" data-tier="{tier}"', card_content)

    # If it's a standard card, let's hide it initially if it doesn't match the active filter (Premium is active by default)
    if tier == 'standard' and 'style="display: none;"' not in card_content:
        card_content = re.sub(r'<div class="tp-card"', r'<div class="tp-card" style="display: none;"', card_content)

    # 2. Update price badge
    bg_color = "var(--ink-soft)" if tier == "standard" else "var(--emerald-primary)"
    card_content = re.sub(r'<span class="tp-badge-price">.*?</span>', rf'<span class="tp-badge-price" style="background: {bg_color};">{price}</span>', card_content)

    # 3. Update category tag to show tier
    card_content = re.sub(r'<span class="tp-category-tag">.*?</span>', rf'<span class="tp-category-tag">{tier.title()}</span>', card_content)

    # 4. Replace tp-actions to remove 'Use ->' button and update Preview button
    # Get the title and url to use in the new onclick
    m = re.search(r'openPreviewModal\(\'([^\']+)\',\s*\'([^\']+)\'\)', card_content)
    if m:
        url = m.group(1)
        title = m.group(2)
        id_m = re.search(r'data-id="([^"]+)"', card_content)
        card_id = id_m.group(1) if id_m else 'template'
        
        new_actions = f'''<div class="tp-actions">
                            <button class="btn-card-preview" style="width: 100%; border-color: var(--emerald-primary); color: var(--emerald-primary); font-size: 0.95rem; padding: 12px;" onclick="openPreviewModal('{url}', '{title}', '{card_id}')">Preview Design</button>
                        </div>'''
        card_content = re.sub(r'<div class="tp-actions">.*?</div>\s*</div>', new_actions + '\n                    </div>', card_content, flags=re.DOTALL)
        
    return card_content

html = re.sub(r'<div class="tp-card".*?<div class="tp-actions">.*?</div>\s*</div>\s*</div>', replace_card, html, flags=re.DOTALL)


# Update the Features section block 
features_pattern = r'<!-- FEATURES SECTION -->.*?<!-- FAQ ACCORDION SECTION -->'
new_features = '''<!-- FEATURES SECTION -->
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

        <!-- FAQ ACCORDION SECTION -->'''
html = re.sub(features_pattern, new_features, html, flags=re.DOTALL)


with open('c:/Users/moham/Documents/Default Project/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

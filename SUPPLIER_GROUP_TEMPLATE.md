# Multi-Supplier Group Template

## Goal

Keep the config stable as suppliers grow from 5 to more vendors.

Use fixed layers:

1. `Supplier-Country`
2. `Country-Aggregation`
3. `Use-Case-Country`
4. `Use-Case`

Current suppliers:

- `BESTBINGLU`
- `NIUBI`
- `CF`
- `MOJIE`
- `BESTVPN`

## Naming Rules

Use one naming format everywhere:

- Supplier country auto group: `<SUPPLIER>-<COUNTRY>-自动`
- Country aggregation group: `<COUNTRY>-自动`
- AI safe country group: `AI-<COUNTRY>-自动`
- Business group: `🤖 AI`, `🤖 ChatGPT`, `📘 GitHub`, `🌍 国外`

Recommended country codes in this project:

- `HK`
- `TW`
- `JP`
- `SG`
- `KR`
- `US`
- `DE`
- `UK`

If you prefer Chinese names in visible groups, keep supplier-country groups in English and only expose Chinese in the top business groups.

## Layer Design

### 1. Supplier-Country

Each group only selects nodes from one supplier in one country.

Examples:

- `BESTVPN-US-自动`
- `BESTVPN-JP-自动`
- `MOJIE-SG-自动`
- `CF-US-自动`
- `NIUBI-US-自动`
- `BESTBINGLU-HK-自动`

This layer answers:

"How is this supplier performing in this country?"

### 2. Country Aggregation

Each group selects from all supplier-country groups in the same country.

Examples:

- `US-自动`
- `JP-自动`
- `SG-自动`

This layer answers:

"What is the best US exit among all suppliers?"

### 3. Use-Case Country

For risky services like AI, do not reuse the generic country group directly.

Examples:

- `AI-US-自动`
- `AI-JP-自动`
- `AI-SG-自动`

This layer answers:

"Which suppliers are trusted for AI in this country?"

### 4. Use-Case

Rulesets should point here.

Examples:

- `🤖 ChatGPT`
- `🤖 AI`
- `📘 GitHub`
- `👯‍♂️ TikTok`
- `🙋 Telegram`
- `🌍 国外`

## Recommended Trust Split

Use different supplier sets for different use cases.

### High trust

For `ChatGPT`, `AI`, `Google`, `Perplexity`, `Meta AI`

Prefer:

- `BESTVPN`
- `MOJIE`
- `NIUBI`

Use `CF` only if you have verified the IP quality.

Use `BESTBINGLU` only after manual verification.

### Medium trust

For `GitHub`, `Telegram`, `Twitter(X)`, `Facebook`

Prefer:

- `BESTVPN`
- `MOJIE`
- `CF`
- `NIUBI`

### Unlock / traffic oriented

For `YouTube`, `Netflix`, `Disney`, `Spotify`, `TikTok`

Can include:

- `CF`
- `BESTVPN`
- `MOJIE`
- `NIUBI`
- `BESTBINGLU`

## Template Snippets

### Supplier-Country Layer

Replace the regex with your real node keywords.

```ini
custom_proxy_group=BESTVPN-US-自动`url-test`(BESTVPN.*美国|BESTVPN.*US|bestvpn.*美国|bestvpn.*us)`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=BESTVPN-JP-自动`url-test`(BESTVPN.*日本|BESTVPN.*JP|bestvpn.*日本|bestvpn.*jp)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=BESTVPN-SG-自动`url-test`(BESTVPN.*新加坡|BESTVPN.*SG|bestvpn.*新加坡|bestvpn.*sg)`http://www.gstatic.com/generate_204`180,5,100

custom_proxy_group=MOJIE-US-自动`url-test`(MOJIE.*美国|MOJIE.*US|mojie.*美国|mojie.*us)`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=MOJIE-JP-自动`url-test`(MOJIE.*日本|MOJIE.*JP|mojie.*日本|mojie.*jp)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=MOJIE-SG-自动`url-test`(MOJIE.*新加坡|MOJIE.*SG|mojie.*新加坡|mojie.*sg)`http://www.gstatic.com/generate_204`180,5,100

custom_proxy_group=CF-US-自动`url-test`(CF.*美国|CF.*US|Cloudflare.*美国|Cloudflare.*US|cloudflare.*美国|cloudflare.*us)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=CF-JP-自动`url-test`(CF.*日本|CF.*JP|Cloudflare.*日本|Cloudflare.*JP|cloudflare.*日本|cloudflare.*jp)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=CF-SG-自动`url-test`(CF.*新加坡|CF.*SG|Cloudflare.*新加坡|Cloudflare.*SG|cloudflare.*新加坡|cloudflare.*sg)`http://www.gstatic.com/generate_204`180,5,100

custom_proxy_group=NIUBI-US-自动`url-test`(NIUBI.*美国|NIUBI.*US|niubi.*美国|niubi.*us)`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=NIUBI-JP-自动`url-test`(NIUBI.*日本|NIUBI.*JP|niubi.*日本|niubi.*jp)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=NIUBI-SG-自动`url-test`(NIUBI.*新加坡|NIUBI.*SG|niubi.*新加坡|niubi.*sg)`http://www.gstatic.com/generate_204`180,5,100

custom_proxy_group=BESTBINGLU-US-自动`url-test`(BESTBINGLU.*美国|BESTBINGLU.*US|bestbinglu.*美国|bestbinglu.*us)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=BESTBINGLU-JP-自动`url-test`(BESTBINGLU.*日本|BESTBINGLU.*JP|bestbinglu.*日本|bestbinglu.*jp)`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=BESTBINGLU-SG-自动`url-test`(BESTBINGLU.*新加坡|BESTBINGLU.*SG|bestbinglu.*新加坡|bestbinglu.*sg)`http://www.gstatic.com/generate_204`180,5,100
```

### Country Aggregation Layer

```ini
custom_proxy_group=US-自动`url-test`[]BESTVPN-US-自动`[]MOJIE-US-自动`[]NIUBI-US-自动`[]CF-US-自动`[]BESTBINGLU-US-自动`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=JP-自动`url-test`[]BESTVPN-JP-自动`[]MOJIE-JP-自动`[]NIUBI-JP-自动`[]CF-JP-自动`[]BESTBINGLU-JP-自动`http://www.gstatic.com/generate_204`180,5,100
custom_proxy_group=SG-自动`url-test`[]BESTVPN-SG-自动`[]MOJIE-SG-自动`[]NIUBI-SG-自动`[]CF-SG-自动`[]BESTBINGLU-SG-自动`http://www.gstatic.com/generate_204`180,5,100
```

### AI Safe Country Layer

Only include trusted suppliers here.

```ini
custom_proxy_group=AI-US-自动`url-test`[]BESTVPN-US-自动`[]MOJIE-US-自动`[]NIUBI-US-自动`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=AI-JP-自动`url-test`[]BESTVPN-JP-自动`[]MOJIE-JP-自动`[]NIUBI-JP-自动`https://chat.openai.com/favicon.ico`180,5,100
custom_proxy_group=AI-SG-自动`url-test`[]BESTVPN-SG-自动`[]MOJIE-SG-自动`[]NIUBI-SG-自动`https://chat.openai.com/favicon.ico`180,5,100
```

### Business Layer

```ini
custom_proxy_group=🤖 ChatGPT`select`[]AI-US-自动`[]AI-JP-自动`[]AI-SG-自动`[]BESTVPN-US-自动`[]所有-手动`[]REJECT
custom_proxy_group=🤖 AI`select`[]AI-US-自动`[]AI-JP-自动`[]AI-SG-自动`[]US-自动`[]JP-自动`[]SG-自动`[]所有-手动`[]REJECT
custom_proxy_group=📘 GitHub`select`[]US-自动`[]JP-自动`[]SG-自动`[]所有-自动`[]所有-手动`[]REJECT
custom_proxy_group=👯‍♂️ TikTok`select`[]US-自动`[]JP-自动`[]SG-自动`[]所有-自动`[]所有-手动`[]REJECT
custom_proxy_group=🙋 Telegram`select`[]SG-自动`[]JP-自动`[]US-自动`[]所有-自动`[]所有-手动`[]REJECT
custom_proxy_group=🌍 国外`select`[]US-自动`[]JP-自动`[]SG-自动`[]所有-自动`[]所有-手动`[]REJECT
```

## Migration Advice For This Repo

Your current config already has these partial concepts:

- `BESTVPN-自动`
- `BESTVPN-US-自动`
- `MOJIE-自动`
- `CF-自动`
- `NIUBI-US-自动`

But it is still mixing:

- supplier groups
- country groups
- business groups

### Recommended next step

Refactor in this order:

1. Add supplier-country groups for `BESTVPN / MOJIE / CF / NIUBI / BESTBINGLU`
2. Replace current `美国-自动 / 日本-自动 / 新加坡-自动` references in risky services with `AI-US-自动 / AI-JP-自动 / AI-SG-自动`
3. Keep `GitHub / Telegram / 国外` on country aggregation groups
4. Keep `DIRECT` out of all AI groups

### Minimum viable version

If you do not want to build every country at once, start with:

- `US`
- `JP`
- `SG`

That gives the biggest benefit with the least complexity.

## Simple Rule Of Thumb

- New supplier added: only add supplier-country groups
- AI risk increased: only adjust `AI-<COUNTRY>-自动`
- A country quality dropped: only adjust `<COUNTRY>-自动`
- A ruleset changed: only adjust the top business group

That is the structure that scales cleanly.

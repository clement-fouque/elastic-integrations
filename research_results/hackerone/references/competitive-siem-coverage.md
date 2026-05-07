# Competitive SIEM coverage: HackerOne (Research Track E)

This document compares IBM QRadar SIEM, Splunk, and Sumo Logic marketplace/catalog coverage for **HackerOne** (bug bounty / vulnerability disclosure platform) and documents how data is collected when an integration path exists. Primary sources: official SIEM integration hubs, Splunkbase search, Sumo Logic integrations documentation index, HackerOne Help Center, HackerOne Integration Partners page, and HackerOne webhooks API reference.

---

## 1. Summary table (section 1.5 / research brief)

| Competitor | Marketplace / catalog match for “HackerOne” | Integration available? | Effective product | Dominant collection mechanism (as documented) |
|------------|---------------------------------------------|-------------------------|-------------------|-----------------------------------------------|
| **IBM QRadar** | **No** HackerOne listing found on the [QRadar SIEM integrations hub](https://www.ibm.com/products/qradar-siem/integrations); **no** `HackerOne` string in fetched HTML for the [QRadar supported DSMs](https://www.ibm.com/docs/en/dsm?topic=configuration-qradar-supported-dsms) topic page (see caveats below). | **SOAR-only** ([IBM Security QRadar SOAR](https://docs.hackerone.com/organizations/ibm-security-soar.html) via HackerOne; not QRadar SIEM log ingestion). | QRadar **SOAR** (incident orchestration / escalation), **not** QRadar SIEM DSM | **Vendor-side workflow**: user escalates from HackerOne to pre-populated SOAR incident; **not** described as syslog/API bulk log feed to SIEM. |
| **Splunk** | **No** apps returned for **`hackerone`** in [Splunkbase app search](https://splunkbase.splunk.com/apps/#/search/query/hackerone) (UI showed **0 Results** at time of retrieval). Technology Add-ons: none found via same catalog search. | **Yes**, as a **native HackerOne → Splunk** integration (Enterprise programs), **not** as a Splunkbase-published Splunk TA/app. | HackerOne “Splunk” connector + customer Splunk HEC | **HTTP Event Collector (HEC)** ingest: HTTPS POST from HackerOne to Splunk collector endpoints; example payload is JSON ([Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html)). |
| **Sumo Logic** | **No** dedicated **HackerOne** product page found in the [Sumo Logic integrations index](https://www.sumologic.com/help/docs/integrations/) category listing; **[UNVERIFIED]** whether a separate in-product App Catalog entry exists (not inspected in-product). | **Yes**, documented as **HackerOne webhooks → Sumo HTTP ingestion** ([Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html)). | Customer-hosted HTTP Source on a Hosted Collector (per Sumo’s HTTP Source docs pattern) | **Webhook HTTP POST** from HackerOne to the Sumo-generated HTTP Source URL ([HTTP Source overview](https://www.sumologic.com/help/docs/send-data/hosted-collectors/http-source/)); event subscription matches [webhook event catalog](https://api.hackerone.com/webhooks/). |

### Caveats

- **Splunkbase** is heavily client-rendered; the **0 Results** observation is from the official search URL at retrieval time. No independent Splunkbase JSON API was available without authentication at time of check; if a community app exists under a non-obvious name, it would be **[UNVERIFIED]** here.
- **IBM DSM** full device matrix may be distributed across PDFs or dynamic assets not present in the single HTML page snippet; absence of `HackerOne` in the fetched DSM topic HTML is **not** a proof of global non-existence—only that it was **not found** via that listing path (**[UNVERIFIED]** if a DSM exists elsewhere).

---

## 2. IBM QRadar SIEM vs SOAR

### Integration identity

| Field | Detail |
|--------|--------|
| **Name** | **IBM Security QRadar SOAR** (listed under HackerOne “Security Workflow” on [Integration Partners](https://www.hackerone.com/partners/integrations)). |
| **Publisher / maintainer** | **HackerOne-documented** integration with IBM Security SOAR; configuration is **assisted by HackerOne** (contact HackerOne with base URL and fields) ([IBM Security QRadar SOAR](https://docs.hackerone.com/organizations/ibm-security-soar.html)). |
| **Catalog page URL (SIEM)** | **No QRadar SIEM–specific HackerOne app** identified on [QRadar SIEM integrations](https://www.ibm.com/products/qradar-siem/integrations) (no HackerOne in page content reviewed). |
| **Version / last updated** | HackerOne doc page shows **June 4, 2025** (help center article date). |
| **Compatibility** | **[UNVERIFIED]** for specific QRadar SOAR versions—not stated in the HackerOne article summary. |

### Data coverage (SOAR path)

- **Stated scope**: “Push all of your HackerOne **submissions** to QRadar SOAR” and track vulnerability reports; workflow is **escalation** from a report (triaged → add reference → **Generate escalation** → pre-populated SOAR issue) ([IBM Security QRadar SOAR](https://docs.hackerone.com/organizations/ibm-security-soar.html)).
- **Event types / log types**: **Not** a SIEM “log source” integration—**case/incident** creation and **reference linking** (Reference ID) between HackerOne and SOAR.
- **Coverage gaps vs bug-bounty SIEM analytics**: No documentation found for **continuous** export of full **activity timelines**, **all comments**, or **program-level** event streams into **QRadar SIEM** as a native DSM; customers would need **custom** forwarding (e.g., syslog from an intermediary) **[UNVERIFIED]** if implemented ad hoc.

### Collection method (SOAR)

| Aspect | Detail |
|--------|--------|
| **Mechanism** | **Vendor-native UI workflow** (issue tracker / escalation), not API pull by QRadar SIEM. |
| **Protocol / format** | **[UNVERIFIED]** wire format between HackerOne and SOAR—article describes user-facing steps, not payloads. |
| **Authentication** | **[UNVERIFIED]**—integration setup via HackerOne support with “base URL” and “fields.” |
| **Configuration** | Customer contacts [HackerOne support](https://support.hackerone.com/); 1–2 business days setup notification per article. |

### Quality signals (SIEM marketplace)

| Signal | Observation |
|--------|-------------|
| **IBM App Exchange listing** | **Not confirmed** via SPA-only exchange pages in this research run; reliance on HackerOne + IBM marketing integration page instead. **[UNVERIFIED]** for starred IBM listing. |
| **Documentation** | HackerOne article is procedural for analysts; shallow on SOAR endpoint/auth details. |

### QRadar SIEM–specific conclusion

**No integration found** for **HackerOne as a QRadar SIEM log source** in the pathways checked above. Competitive positioning for SIEM ingestion is effectively **empty** vs HackerOne; only **SOAR** is officially documented.

---

## 3. Splunk

### Integration identity

| Field | Detail |
|--------|--------|
| **Name** | **Splunk Integration** (HackerOne Help Center) ([Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html)). |
| **Splunkbase app / TA** | **No** listing found under search query **`hackerone`** — [Splunkbase search](https://splunkbase.splunk.com/apps/#/search/query/hackerone) returned **0 Results** at retrieval time. |
| **Publisher / maintainer** | **Vendor (HackerOne)** connector documented on HackerOne; Splunk-side configuration uses standard **Splunk HEC** (Splunk administrator creates token). |
| **Catalog URL** | N/A for Splunkbase; authoritative doc: [Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html). |
| **Version / last updated** | Article dated **January 14, 2025**. |
| **Compatibility** | Splunk Cloud vs on-prem HEC URI patterns documented (hosts, ports `8088` / `443`, paths `/services/collector/event` or `.../raw`); Splunk Enterprise **[UNVERIFIED]** beyond HEC generality. |

### Data coverage

Per HackerOne, configurable **event triggers** include:

- Report submissions  
- Report state changes (triaged, retesting, resolved, etc.)  
- Report assigned  
- Report comments  
- Report disclosures  
- Report rewards  

Source: [Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html).

**Entitlement**: **Enterprise programs only** (same article).

**Gaps**: Anything **not** exposed as one of those triggers will not ship via this connector. Exact parity with full [webhook event list](https://api.hackerone.com/webhooks/) is **[UNVERIFIED]**—the Splunk article lists categories, not the full `report_*` matrix.

### Collection method

| Aspect | Detail |
|--------|--------|
| **Mechanism** | **Vendor push to Splunk HTTP Event Collector** (HTTPS). |
| **Protocol / format** | **JSON** example payload with nested `data` / `relationships` (e.g. `activity-comment` type) ([Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html)). |
| **Authentication** | **HEC token** configured in HackerOne “New authentication”; Event Collector URL + token. |
| **Configuration** | Splunk: **Settings → Data Inputs → HTTP Event Collector → New Token**. HackerOne: **Engagements → Program → Settings → Automation → Integrations → Connect to Splunk** (same doc). |

### Quality signals

| Signal | Observation |
|--------|-------------|
| **Splunkbase rating / downloads** | N/A (**no Splunkbase app** located). |
| **Support tier** | **HackerOne + Splunk standard HEC**; not “Splunk Supported” app in marketplace sense. |
| **Documentation quality** | **Good operational detail** for HEC URL construction and setup screenshots in HackerOne doc. |

---

## 4. Sumo Logic

### Integration identity

| Field | Detail |
|--------|--------|
| **Name** | **Sumo Logic Integration** (HackerOne Help Center) ([Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html)). |
| **Sumo App Catalog** | **No** “HackerOne” integration identified in public [integrations documentation index](https://www.sumologic.com/help/docs/integrations/) listings; ingestion pattern is generic **HTTP Source**. **[UNVERIFIED]** for proprietary App Catalog entries only visible in-product. |
| **Publisher / maintainer** | **HackerOne-documented** use of Sumo via **webhooks + HTTP collector URL**; Sumo docs describe HTTP Sources generally ([HTTP Source](https://www.sumologic.com/help/docs/send-data/hosted-collectors/http-source/)). |
| **Catalog URL** | HackerOne: [Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html). |
| **Version / last updated** | Article dated **March 16, 2026**. |

### Data coverage

- **Configurable** via webhook subscription: either **“Send me everything”** or pick individual events ([Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html)).
- **Event enumeration** aligns with **[HackerOne webhook catalog](https://api.hackerone.com/webhooks/)** (examples: `report_created`, `report_bounty_awarded`, `report_swag_awarded`, `report_triaged`, `report_comment_created`, disclosures, duplicates, spam, Hai prioritisation, retest lifecycle, program hacker join/leave for private programs, etc.).
- **Entitlement**: **Not all product/platform editions** (see [HackerOne Product and Platform Entitlement Overview](https://docs.hackerone.com/en/articles/12975245-hackerone-product-and-platform-entitlement-overview) — **login required** per article).

**Gaps**: Same as Splunk-style push integrations—anything not emitted as webhook events requires **polling API or custom ETL**.

### Collection method

| Aspect | Detail |
|--------|--------|
| **Mechanism** | **HackerOne HTTP webhook POST** → **Sumo HTTP Source URL** ([Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html)). |
| **Protocol / format** | **HTTPS POST**, JSON payloads consistent with webhook documentation (headers `X-H1-Event`, `X-H1-Delivery`, `X-H1-Signature` per [Webhooks API](https://api.hackerone.com/webhooks/)). |
| **Authentication** | HMAC **`X-H1-Signature`** with optional webhook secret (**[UNVERIFIED]** whether Sumo validates this natively vs requiring a middleware). |
| **Configuration** | Sumo: create HTTP collector/source per [HTTP Source](https://www.sumologic.com/help/docs/send-data/hosted-collectors/http-source/). HackerOne: **Engagements → Program → Settings → Automation → Webhooks → New webhook**; paste Payload URL ([Sumo Logic Integration](https://docs.hackerone.com/organizations/sumo-logic-integration.html)). |

*[Note: HackerOne Sumo article links to `help.sumologic.com/...Collect_Streaming_Data_from_HTTP`; a direct fetch timed out—use Sumo HTTP Source docs linked above as stable reference.]*  

### Quality signals

| Signal | Observation |
|--------|-------------|
| **Marketplace popularity** | N/A (**no dedicated Sumo “HackerOne app” doc** identified). |
| **Documentation** | HackerOne + Sumo generic HTTP docs; customers likely build **parsers/rules** themselves. |

---

## 5. Comparison notes (landscape assessment)

### Coverage breadth

- **Broadest event surface (documented)**: **Sumo path** via **generic webhooks** can subscribe to **all** catalogued webhook events—including **bounty**, **swag**, **severity-related lifecycle**, disclosures, duplicates, Hai prioritisation, retest lifecycle, etc.—because the webhook reference is exhaustive ([Events table](https://api.hackerone.com/webhooks/)).
- **Splunk connector** exposes a **subset** of categories (submissions, state changes, assignment, comments, disclosures, rewards) per HackerOne’s Splunk page—**may be narrower** than full webhook taxonomy unless **[UNVERIFIED]** additional mapping exists internally.
- **IBM QRadar SOAR**: **narrowest** relative to SIEM observability—**case management / escalation**, not a general telemetry pipeline into **SIEM**.
- **QRadar SIEM**: **no verified native path** found.

### Collection method alignment

- **Dominant competitor pattern observed**: **event-driven vendor push over HTTPS** (**HEC** for Splunk; **HTTP Source** + webhooks for Sumo) keyed off **reports/program lifecycle**, **not** continuous scheduled **REST/API pull**.
- **Elastic (recommended in research context)**: **REST API pull via CEL** is **different**—better for **backfill**, **pagination**, unified scheduling in **Elastic Agent**, and consistent **ECS** normalization, at the cost of not being “instant push” unless combined with webhooks.

### Maintenance status

- HackerOne documentation shows **recent article dates** (2025–2026 for Splunk and Sumo; 2025 for SOAR), suggesting ongoing editorial maintenance.
- **Splunkbase** absence implies **no** Splunk-published version cadence as a downloadable artifact.

### Gaps Elastic could address

| Gap | Competitor posture |
|-----|---------------------|
| **Native QRadar SIEM DSM / App Exchange appliance** | **Not found** for HackerOne. |
| **Prebuilt Splunk TA with CIM/correlation dashboards** | **Not found** on Splunkbase under `hackerone`. |
| **Prebuilt Sumo app (parsed fields, dashboards)** | **Public docs**: generic HTTP ingest only. |
| **Historical completeness** | Push models may **miss events** if consumer is down or webhook queue fails (**[UNVERIFIED]** SLA); pull models can reconcile with API cursors/state. |

### Elastic differentiators (illustrative, not exhaustive)

| Area | Leverage vs competitors |
|------|---------------------------|
| **ECS normalization** | Consistent taxonomy across bounty, actor, vulnerability, bounty award fields vs ad hoc JSON in each SIEM. |
| **Agent / Fleet** | Central rollout of collectors and API credentials vs point-in-time HEC/token sprawl documentation. |
| **Pull + optional push** | CEL/API for completeness; optionally combine with Elastic-supported HTTP input for webhook-style delivery if desired. |

---

## 6. Sources (URLs)

| Resource | URL |
|----------|-----|
| IBM QRadar SIEM integrations overview | https://www.ibm.com/products/qradar-siem/integrations |
| IBM QRadar supported DSMs (documentation entry point) | https://www.ibm.com/docs/en/dsm?topic=configuration-qradar-supported-dsms |
| Splunkbase app search (`hackerone`) | https://splunkbase.splunk.com/apps/#/search/query/hackerone |
| Sumo Logic integrations index | https://www.sumologic.com/help/docs/integrations/ |
| Sumo Logic HTTP Source | https://www.sumologic.com/help/docs/send-data/hosted-collectors/http-source/ |
| HackerOne Integration Partners | https://www.hackerone.com/partners/integrations |
| HackerOne — Splunk Integration | https://docs.hackerone.com/organizations/splunk-integration.html |
| HackerOne — IBM Security QRadar SOAR | https://docs.hackerone.com/organizations/ibm-security-soar.html |
| HackerOne — Sumo Logic Integration | https://docs.hackerone.com/organizations/sumo-logic-integration.html |
| HackerOne — Webhooks & events reference | https://api.hackerone.com/webhooks/ |

---

## 7. Research gaps / follow-ups **[UNVERIFIED]**

1. Splunkbase: confirm **zero** TA/apps under alternate names (**“Hacker One”**, **bug bounty**, vendor author filters).  
2. IBM Application Exchange SPA: scripted or manual search for “HackerOne” (client-rendered hub).  
3. Sumo in-product App Catalog keyword search for “HackerOne” or “Bug Bounty”.  
4. Whether HackerOne’s Splunk connector maps to **exactly** the same events as selectable webhooks, or only the listed trigger categories—confirm with HackerOne support or changelog.

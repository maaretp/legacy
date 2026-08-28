---
title: "Platform Product Testing"
date: 2025-11-25
theme: testing-craft-and-skills
labels: []
source: https://visible-quality.blogspot.com/2025/11/platform-product-testing.html
---

# Platform Product Testing

*Published 2025-11-25*  
*Source: <https://visible-quality.blogspot.com/2025/11/platform-product-testing.html>*

---

In the lovely world of consulting, I find myself classifying the types of engagements I work with. While **Product / System Testing** holds a special place in my heart with the close collaboration with teams building the product together, I come often to a table where the Product is platform product, the building is configuring and specially constrained programming, and the purpose of the platform product is to enable reuse for similar kinds of IT system needs. I often call this **IT Testing**.

With IT Testing, a firm belief on previous experience on the platform product at hand runs strong. That makes me particularly fascinated in modeling the similarities and differences, and insisting I can learn to test across platform products. So today I decided to take moment to explain what I have gathered so far on Platform Product Testing for Dynamics 365, SAP S4/Hana, Salesforce and Guidewire. The listing of platform products is more than these four, and I very intentionally excluded some of my lovely friends from work such as Infor and ServiceNow.

What makes *testing* of a platform product based system different is the experience of inability to tell what is a platform product problem (or feature), what is something you had control over in changing, and what comes from your rules combined with your data. For it to work for the business purpose it was acquired, the culprit does not seem like a priority. If it does not run your business the way your business needs running, there is a problem. Recognizing a problem starts then figuring out what to do with such problems. *Acceptance testing* with business experts is essential and critical, but also very disruptive to business as usual if it needs repeating regularly.

Since most of the functionality comes from the Platform Product, your integration project costs are usually optimized by focusing their testing on the things your contractor is changing and thus responsible for. This may mean that Acceptance testing sees an integrated end to end system, while other testing has been more isolated. Automation, if it exists, is the customers choice in investing in essentially multivendor feedback where some of the parts are the product that, theoretically, was tested before given to you - just not with your configurations, integrations and data that run your business.

Let's talk a bit about the platform products.

**Dynamics 365**, Power Platform, is a set of Microsoft Platform Products giving you ERP and CRM types of functionalities with lots of low-code promises.

**Salesforce** is primarily CRM-types of functionalities, and it's a cloud-based multi-tenant platform.

**SAP S/4HANA** is with ERP-types of functionalities and enough history so that the new and old mix.

**Guidewire** is insurance-focused platform product.

My curiosity with these started with noting vocabulary. A thing we know well in testing is a concept of a **test environment**. They come in two forms: long-running (production-like) and ephemeral. For Salesforce  the environments are called *sandbox* and *scratch org.* For SAP matching concepts to get are testing environments, development environments and the supporting tooling of *transport/ChaRM*. For Dynamics 365 we talk about *solution packages* and expect understanding of containers. And for Guidewire we talk of bundles, patches and upgrades. While I recognize the dynamics of how things work in each, I get corrected a lot on use of wrong words.

Each of these lovely platform products comes with its own *programming language.*  Salesforce gives us Apex. Guidewire introduces us to Gosu. Dynamics drives us to low code power apps components configurations. SAP gives us ABAB and configurations. For someone who holds dear the belief that sufficiently complex configuration is programming, I find these just fascinating.

My highlights so far are:

Dynamics 365

- Got to love containers as an approach and Azure DevOps makes this feel to me more like modern product development for deployment tooling side.
- UI automation requires understanding of user-specific settings, and I hear UI can be fragile. Locators for test automation aren't straightforward.
- Test from APIs and a bit from end to end in UI.
- Pay attention to solution layering discipline, and automate deployment and data seeding.
- Get started:

- store solutions in source control, build import/export pipelines via Power Platform Build Tools, prefer API tests and small UI smoke suites

SAP S/4HANA

- Automated change impact analysis relying on the structure of Transports/ChaRM is kind of cool given your tools of test management match the support. It is also generally not optional and trying other things can be trouble.
- Config changes have impacts across modules and business process chain testing is essential
- Get started:

- map transports to test suites, automate test runs on transport promotion, use S/4 HANA test automation tool where available and treat integration flows as first-class tests.

Salesforce

- Multi-tenant means quota limits. Stay within the limits. Testing too big is trouble.
- CI/CD and scratch orgs allow for lovely change-based test automation practice. Use mocks for integrations.
- Smart scoping of data for test purposes helps, plan for data subsetting and refresh cadence.
- Locators for test automation can be next level difficult for Shadow DOM and dynamic components.
- Get started:

- enforce Apex test coverage, minimize data creation in tests, use scratch orgs + CI for PR validation, monitor governor limits during pipeline runs.

Guidewire

- Product model–driven testing: insurance product model serves as testing anchor
- Collected open source toolset as 'Guidewire Test Framework' and enforced rules around sufficient use of them guide the ecosystem towards good practices like test automation and coverage.
- Limitations on *some contracts* on use of AI can significantly limit hopes for use of AI
- Get started:

- create a policy lifecycle regression pack; adopt Guidewire Testing Framework; run regression against each product model drop; negotiate test environment refresh cadence with vendor/ops.

For all *reuse of test artifacts across clients is theoretically possible.* For all, *test data management* is necessary but execution of its practice differs: Salesforce and D365 drive synthetic data and subsetting approaches, and SAP and Guidewire require larger production-like data sets; fast refresh capability and data masking is universal. All come with a *CI/CD pipeline* but each have a platform specific recommended one: Salesforce DX for Salesforce, Power Platform build tools + Azure Devops for Dynamics365, transport/ChaRM automation for SAP.

Universal truths, maybe:

- Need for **strong regression testing** due to vendor-driven releases
- Presence of **custom code + configuration layer** you must retest
- Requirement for **representative test data**
- Complexity of **cross-module / cross-app business processes**
- **Integration-heavy** test design (APIs, services, middleware)
- Organizational **constraints around AI-generated artifacts**
- **Upgrade regression risk** as a consistent pain point

Decided this could be helpful - Platform testing capabilities and constraints comparison. At least it helps me with learning coverage as I venture further into these.

| Capability / Constraint | **Guidewire** | **Salesforce** | **Dynamics 365 / Power Platform** | **SAP (S/4HANA)** |
| --- | --- | --- | --- | --- |
| **Metadata-driven development** | (✔️) Config layers, product model | ✔️ Core concept | ✔️ Solutions + Dataverse | (✔️) Mostly configuration, less metadata-portable |
| **Proprietary programming language** | ✔️ Gosu | ✔️ Apex | — (PowerFx only for Canvas, but not core platform) | ✔️ ABAP |
| **Strict platform resource limits** | (✔️) Some internal limits | ✔️ Governor limits | (✔️) API limits & throttling | (✔️) Performance constraints by module |
| **Vendor-controlled releases with required regression** | ✔️ Product model upgrades & patches | ✔️ Seasonal releases | ✔️ Wave updates | ✔️ Transport-based releases & upgrade cycles |
| **Automated test impact analysis supported** | — | (✔️) Through metadata diffs + DX | (✔️) Via solution diffs & pipelines | ✔️ Transport-level impact analysis |
| **Native test automation tooling** | ✔️ Guidewire Testing Framework | (✔️) Apex tests + UI Test Builder (limited) | (✔️) EasyRepro / Playwright guidance but not “native” | ✔️ SAP S/4HANA Test Automation Tool |
| **UI layer highly changeable / automation fragile** | (✔️) Angular-based UI, moderate | ✔️ Lightning DOM changes often | ✔️ Model-driven apps update frequently | (✔️) Fiori stable but customizable |
| **Complex cross-module business processes** | ✔️ Policy ↔ Billing ↔ Claims | (✔️) Depends on org complexity | (✔️) Depends on app footprint | ✔️ Core ERP complexity across modules |
| **Strong CI/CD support from vendor** | (✔️) Limited compared to others | ✔️ Salesforce DX | ✔️ Azure DevOps + Build Tools | (✔️) SAP CI/CD + ChaRM |
| **Easy ephemeral environment creation** | — | ✔️ Scratch orgs | ✔️ Dev/Test environments via Admin Center | — (environments heavy, transports rely on fixed landscapes) |
| **Heavy dependency on realistic test data** | ✔️ Policy & claims data | (✔️) For integration flows | (✔️) For model-driven logic | ✔️ Mandatory for end-to-end flows |
| **Contractual constraints on AI-generated code/config** | (✔️) Vendor & client contracts commonly restrictive | (✔️) Org policies vary | (✔️) Varies by tenant/governance | (✔️) Strong compliance usually restricts |
| **Complex upgrade regression risk** | ✔️ High | (✔️) Medium | (✔️) Medium | ✔️ Very high |
| **Platform-driven integration patterns (APIs, services)** | ✔️ SOAP/REST internal services | ✔️ REST/Bulk/Messaging | ✔️ Dataverse APIs + Azure | ✔️ BAPIs/IDocs/OData |
| **Stable API layer for automation** | (✔️) Good internal APIs | ✔️ Strong API surface | ✔️ Dataverse APIs stable | ✔️ Strong API layer but complex |

Out of all the difference, this one is the most defining: ephemeral test environments: Salesforce, Dynamics 365 AND vendor-native automation tooling: SAP, Guidewire.

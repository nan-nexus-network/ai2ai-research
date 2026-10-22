# Abstract / 摘要: Vietnam as a Bridge in the AI2AI Economy

*One page. The full paper (Vietnamese) is in [`WHITEPAPER_VN_AI_BRIDGE.md`](WHITEPAPER_VN_AI_BRIDGE.md).*

---

## English

**The question.** If a country does not compete to build billion-dollar foundation models, what role could it play that is genuinely valuable and sustainable in the global AI value chain? This paper proposes testing one: a **neutral AI reference bridge layer** between AI ecosystems that currently cannot talk to each other.

**Finding 1: the gap is real, and official documents say so.** MCP (Anthropic) connects AI to tools and data. A2A (Google) defines how agents talk to agents. But A2A still carries the architectural assumptions of one ecosystem, and Chinese standards work on the same problem, with the GB/Z 185-2026 suite published in May 2026. When an agent in one ecosystem must transact with an agent in another, three barriers appear: mismatched packet structure and session handling; no mechanism to translate and check cross-border compliance rules; and no neutral verification receipt when the two sides disagree about what actually happened. A working implementation of the standards, together with Chinese official documents, is the acknowledgement that MCP and A2A are not sufficient on their own.

**Finding 2: Vietnam has four concrete advantages, but they are not independent.** A young population with high AI adoption and a fast-developing engineering base; diverse export markets that force enterprises to work across many AI ecosystems at once; the Hanoi Digital Declaration and the "Connected Intelligence" direction adopted by ASEAN digital ministers in January 2026; and a set of bilateral and multilateral AI commitments. Each of these is useful on its own. Connected by an open interoperability layer, they reinforce each other: young engineers get a real field to work in, enterprises get a shared layer instead of N adapters, and the country gets a reason to be trusted as a neutral meeting point.

**Finding 3: this is a proposal, not a manifesto.** The paper closes with **twelve open questions** for the community and domain experts, and publishes a **stopping criterion**: if in twelve months this proposal is neither adopted by the community nor shown to have practical value, we will publicly end the project rather than waste social effort.

**What is not claimed.** No standardised protocol is proposed. No production system exists. The accompanying proof of concept in [`ai2ai-core`](https://github.com/nan-nexus-network/ai2ai-core) runs a local, single-process simulation with a static string blocklist that is explicitly *not* a security measure, and a SHA-256 receipt that establishes data integrity but **not** identity or non-repudiation. Those gaps are tracked as open issues, published in advance.

**Companion dataset.** [`STANDARDS/`](../STANDARDS/) collects 23 international AI interoperability, AI-governance, trade and cooperation instruments in a machine-readable form, every row traceable to a numbered source. Use it to check, extend, or contradict this analysis.

---

## 中文摘要

**核心问题。** 如果一个国家不参与竞赛去打造价值千亿美元的基础模型，它还能在全球 AI 价值链中扮演什么真正有价值、可持续的角色？本文提议尝试一种：**在中立 AI 生态系统之间架设一层中立的"参考桥接层"**。

**结论一：缺口是真实存在的，而且官方文件自己就承认了。** MCP（Anthropic）解决 AI 与工具/数据的连接问题，A2A（Google）定义了智能体之间的通信方式。但 A2A 仍带有单一生态的架构烙印，中国方面也在解决同一问题，并于 2026 年 5 月发布 GB/Z 185-2026 系列。当一个生态中的智能体要与另一个生态中的智能体交易时，会遇到三道障碍：**数据包结构与会话管理不一致**；**缺少跨法域合规规则的转换与校验机制**；**双方对执行结果产生争议时缺少中立验证回执**。中国官方文件本身承认 MCP 与 A2A 尚不充分，这是最强的客观佐证。

**结论二：越南有四项具体优势，但它们并不彼此独立。** 年轻人口与 AI 接受度高、工程人才成长快；出口市场多元，迫使企业同时面对多个 AI 生态系统；2026 年 1 月东盟数字部长会议通过的《河内数字合作宣言》与"Connected Intelligence"方向；以及一系列双边与多边 AI 承诺。单独看每一项都有用；由一个开放互操作层连接起来后，它们会形成合力。

**结论三：这是提议，不是宣言。** 文档以**十二个开放问题**结尾，并公布**停止条件**：若 12 个月内该提议既未被社区接受、也未证明实际价值，我们将公开结束项目，而不是浪费社会资源。

**本文不主张什么。** 不提出标准化协议，不存在生产系统。配套 PoC 见 [`ai2ai-core`](https://github.com/nan-nexus-network/ai2ai-core)：仅本地单进程模拟，静态字符串黑名单**明确不是**安全措施，SHA-256 回执只保证数据完整性，**不**保证身份与不可抵赖。这些缺口已作为公开 issue 提前列出。

**配套数据集。** [`STANDARDS/`](../STANDARDS/) 以机器可读形式收录 23 项国际 AI 互操作、AI 治理、贸易与合作文书，每一行都可追溯到具体来源编号。欢迎据此核查、补充或反驳本文分析。

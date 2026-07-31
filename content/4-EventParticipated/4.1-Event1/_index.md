---
title: "Event 1"
date: 2026-07-27
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Summary Report: "AI Agentic Build Week"

### Event Objectives

- Give hackathon teams a stage to present the AI-agentic products they built during the competition
- Share real, hands-on experience of designing and shipping an agentic AI solution on AWS under strict time pressure
- Expose attendees to different problem domains, architecture choices, and cost-estimation approaches for agentic systems
- Encourage knowledge exchange between teams, mentors, and the audience

### Presenting Teams

- **Team 3KA – S.H.E.P.H.E.R.D.**: a crowd-monitoring and hazard-detection system for event venues, combining computer vision (YOLO + ByteTrack) with an agentic layer (Amazon SageMaker, Amazon Bedrock AgentCore, Strands Agent) and a React operator dashboard
- **Team Plan V – SA Professional Native App**: an AI assistant that helps Solution Architects turn natural-language requirements into draft architectures, editable AWS diagrams, and directional AWS cost estimates
- **Team 9slide.vn – Signal Scout**: a platform that detects early signals of corporate strategy or restructuring changes, built on Amazon Bedrock, AgentCore, LangFuse, and web-monitoring tools such as Apify/TinyFish

### Key Highlights

#### From idea to working prototype under 24 hours

Each team walked through their journey: choosing a track, forming a team, building non-stop for 24 hours, and pitching to judges on demo day. The teams were candid about the chaos behind the scenes — sleepless nights, last-minute debugging, and the pressure of shipping something that actually works.

#### Designing an "agentic layer," not just a model call

A recurring theme across the presentations was separating an **autonomous monitoring/analysis agent** (constantly watching data and raising proactive alerts) from an **operator/user-facing copilot** (answering natural-language questions grounded in live data). This pattern showed up in both the crowd-monitoring system and the corporate-signal platform.

#### Architecture and cost trade-offs are part of the deliverable

Beyond the demo, teams were expected to show a real AWS architecture and a cost breakdown (e.g. Bedrock token usage, AgentCore runtime, hosting, monitoring). One team even presented an alternative, more cost-efficient architecture — a reminder that a working prototype and a *sustainable* one are not the same thing.

#### Tooling accelerates architecture work itself

One team built a meta-product: an AI assistant for Solution Architects that reads requirements, drafts architecture options, and auto-generates AWS diagrams and cost estimates — turning a task that used to take days into something produced in minutes.

### Key Takeaways

#### Team & process

- Preparation (clear scope, ready toolkit, defined roles, a rehearsed demo story) is what actually frees a team to focus on building, not "cheating."
- Small, finished features consistently beat big, unfinished ideas when it comes to judging and to shipping in general.

#### Technical

- Agentic AI systems benefit from splitting **monitoring/prediction** responsibilities from **conversational/operator-facing** responsibilities.
- Cost estimation and architecture trade-offs should be considered from day one, not bolted on afterward.
- Combining computer vision, cloud inference, and agentic orchestration is achievable in a short hackathon timeframe if scope is kept tight.

#### Soft skills

- Pitching a technical product clearly to a non-technical audience is its own skill, separate from building it.
- The people and connections made during the event matter as much as the result of the competition.

### Applying to Work

- Consider the "autonomous monitor + copilot" pattern when designing agentic features for my own project
- Include a rough AWS cost estimate alongside any architecture proposal, instead of treating it as an afterthought
- Apply the "scope it small, finish it well" lesson when planning my own project milestones
- Look into AWS Bedrock AgentCore / Strands Agent as building blocks for agent-based features

### Event Experience

Attending **AI Agentic Build Week** gave me a close-up look at how different teams tackle the same broad theme — agentic AI on AWS — with very different products, from crowd safety to corporate intelligence to developer tooling. Seeing the full journey, not just the polished final demo, made the trade-offs and effort behind each product much more tangible than reading about them would have been.

#### Event photos
![AI Agentic Build Week event]({{< relURL "images/event1.jpg" >}})

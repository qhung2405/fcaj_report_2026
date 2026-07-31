---
title : "Blog 3"
date : "2026-07-27"
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

# Should Services Call Each Other Directly, or Move to an Event-Driven Architecture with EventBridge?

If your system has multiple services that need to "know" about events happening elsewhere, you traditionally only had two approaches — and both leave you with operational baggage:

1. **Calling services directly via API (tight coupling):**
   - Every time you add a new service that needs certain information, you have to update the calling logic everywhere that's affected.
   - If a destination service fails or responds slowly, the calling service is affected too, easily causing a chain reaction across the whole system.
2. **Writing your own cron jobs or periodic sync scripts:**
   - This reduces direct dependency between services...
   - ... But you still have to manage the schedules yourself, logic often ends up duplicated, and it becomes hard to track the full event flow across the system as the number of services grows.

---

## The AWS Turning Point: Amazon EventBridge

To solve this problem, AWS provides Amazon EventBridge — a serverless service built for event-driven architecture, offering the following benefits:

1. **With EventBridge you can:**
   - Fully decouple services from one another: a service simply publishes an event, and any interested services register their own rules to receive exactly the event types they need, with no direct calls required.
   - Add or remove a service from the system without affecting the rest of it.
2. **EventBridge provides two main mechanisms, each solving a different problem:**
   - Event bus acts as a central router, receiving events from multiple sources (custom-built applications, AWS services, third-party software) and delivering them to multiple destinations, optionally transforming the data before delivery.
   - Pipes are suited for point-to-point integration: each pipe receives events from a single source and delivers them to a single destination, but supports more advanced data transformation and enrichment.
   - The two are often used together: a pipe can receive data from a DynamoDB Stream and send it to an event bus, which then distributes it to multiple destinations according to configured rules.
3. **No More Manual Cron Jobs:**
   - EventBridge Scheduler is a serverless scheduler that lets you create, run, and manage tasks on a schedule (cron or rate expression) or as one-time tasks, with configurable flexible time windows and retry limits — fully replacing the need to manage cron jobs manually.


![Blog 3]({{< relURL "images/image3.png" >}})

<p style="font-size: 1rem; font-weight: normal;">
  <a href="https://www.facebook.com/share/p/18qszRmJAL/">View post on AWS Study Group</a>
</p>
---

### References

- [What Is Amazon EventBridge? – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon EventBridge Event Buses – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html)
- [Amazon EventBridge Pipes – AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)
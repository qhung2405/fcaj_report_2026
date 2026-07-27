---
title: "Week 2 Worklog"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---


### Week 2 Objectives:

* Design the network architecture for the web application: VPC, subnets, route tables, Internet Gateway, NAT Gateway.
* Configure Security Groups to control traffic between the web tier and the database tier.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Learn Amazon VPC concepts (VPC, subnet, Availability Zone, route table). | 06/22/2026 | 06/22/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Create a custom VPC with public and private subnets across multiple Availability Zones. | 06/23/2026 | 06/23/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Configure Internet Gateway and route table for the public subnet. | 06/24/2026 | 06/24/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Configure NAT Gateway and route table for the private subnet. | 06/25/2026 | 06/25/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Create Security Groups for the web tier and the database tier following least-privilege rules. | 06/26/2026 | 06/26/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Week 2 Achievements:

* Designed and provisioned a custom VPC with public subnets (for the web/app server) and private subnets (for the database).
* Configured Internet Gateway and NAT Gateway so private resources can access the internet without being publicly exposed.
* Created Security Groups following least-privilege rules (e.g., only allow port 80/443 from the internet, only allow the database port from the app server's Security Group).

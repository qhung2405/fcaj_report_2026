---
title: "Week 3 Worklog"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---


### Week 3 Objectives:

* Launch an EC2 instance inside the VPC created in Week 2 to host the web application.
* Deploy the application code written locally in VSCode to the EC2 instance and verify it runs correctly.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Learn EC2 concepts (instance types, AMI, EBS, Elastic IP). | 06/29/2026 | 06/29/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Launch an EC2 instance in the public subnet, attach the web-tier Security Group. | 06/30/2026 | 06/30/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Connect via SSH and install the runtime environment (Python/Node.js) and reverse proxy (Nginx). | 07/01/2026 | 07/01/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Deploy application code from local VSCode to the EC2 instance (via Git or `scp`). | 07/02/2026 | 07/02/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Test the running application by accessing the instance's public IP/domain. | 07/03/2026 | 07/03/2026 | <https://cloudjourney.awsstudygroup.com/> |


### Week 3 Achievements:

* Successfully launched and configured an EC2 instance running Amazon Linux/Ubuntu in the public subnet.
* Installed the application runtime and reverse proxy, configured the instance to serve the application on port 80/443.
* Deployed the application from the local VSCode environment to EC2 and confirmed it is accessible from a browser.

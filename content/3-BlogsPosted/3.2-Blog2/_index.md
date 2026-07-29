---
title : "Blog 2"
date : "2026-07-27"
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

# Should You Keep Managing NAT Gateway Security and Scaling Manually, or Let RNAT Automate It?

If you're running NAT Gateway the traditional (zonal) way, you're probably already used to handling a set of recurring issues yourself — and each one adds extra operational work:

1. **NAT Gateway must live in a public subnet:**
   - This creates a security concern. Since NAT Gateway is required to sit in a public subnet, security-conscious organizations always need to be careful not to accidentally deploy sensitive resources into that same subnet.
2. **Manually managing port exhaustion and IP provisioning:**
   - As traffic grows, you have to monitor concurrent connections yourself and manually add Elastic IPs before hitting the limit — leaving you reactive rather than proactive during traffic spikes.
   - Integrating with VPC IPAM for controlled IP allocation also requires its own manual configuration and monitoring.

---

## The AWS Turning Point: Regional NAT Gateway (RNAT) Automates It All

With RNAT, most of the manual work above is now handled by AWS at the infrastructure level, delivering the following benefits:

1. **Improved Security:**
   - Since no public subnet is needed to host the NAT Gateway, security-conscious organizations can completely eliminate the risk of accidentally deploying sensitive resources into a public subnet.
2. **Automatic Protection Against Port Exhaustion:**
   - Each IP address assigned to RNAT supports up to 55,000 concurrent connections to a single destination; as it approaches this threshold, RNAT automatically provisions additional IPs (up to 32 per AZ) with no manual intervention needed.
   - IP scaling is fairly elastic: adding more IPs takes about 5 minutes and starts once concurrent connections exceed roughly 40,000; conversely, the system only scales back down once connections drop below 20,000 for about an hour — a "scale up fast, scale down slow" design.
3. **Built-In VPC IPAM Integration, With Manual Control Still Available:**
   - RNAT can automatically draw IP addresses from an IPAM pool when expanding into a new AZ or scaling due to increased traffic, making IP allocation more controlled and predictable.
   - If preferred, users can still choose manual mode to manage AZs and Elastic IPs themselves instead of relying fully on RNAT automation.
4. **Flexible Monitoring and Routing:**
   - RNAT emits CloudWatch metrics similar to zonal NAT Gateway for each AZ, along with additional log fields such as resource-id and az-id for easier tracking.
   - RNAT's route table allows inserting AWS Network Firewall or Gateway Load Balancer between the private subnet and the NAT Gateway to inspect traffic before it reaches the internet.


![Blog 2]({{< relURL "images/image2.png" >}})
---

### References

- [Introducing Amazon VPC Regional NAT Gateway – AWS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-vpc-regional-nat-gateway)
- [Amazon VPC IP Address Manager (IPAM) Documentation](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html)
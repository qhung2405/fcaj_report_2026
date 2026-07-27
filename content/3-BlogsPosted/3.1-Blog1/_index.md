---
title : "Blog 1"
date : "2026-07-27"
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

# INTRODUCING AMAZON VPC REGIONAL NAT GATEWAY

AWS NAT Gateway is a fully managed, highly available Network Address Translation (NAT) service that lets resources in a private subnet initiate outbound connections without needing their own public IP address. In November 2025, AWS announced a new operating mode for NAT Gateway: Regional NAT Gateway (RNAT) — allowing a single NAT Gateway to automatically expand and contract across multiple Availability Zones (AZs) within the same VPC, instead of requiring a separate deployment per AZ as before.

![Blog 1]({{< relURL "images/image1.png" >}})

### Key points to know

- Previously, each AZ required its own NAT Gateway placed in its own public subnet, and the process had to be repeated every time you expanded into a new AZ.
- Regional NAT Gateway operates at the VPC level rather than the subnet/AZ level, significantly reducing the number of components to manage.
- RNAT does not require a public subnet in every AZ to reside in.
- When expanding to a new AZ, you can reuse the same route table and the same NAT Gateway ID instead of creating a new one.
- RNAT automatically maintains "zonal affinity" (preferring same-AZ routing) to ensure high availability while simplifying the architecture.

In essence, Regional NAT Gateway solves a common operational problem: duplicating NAT infrastructure per AZ, which is time-consuming to configure and complicates route tables. With RNAT, infrastructure teams only need to manage a single NAT Gateway entity for the entire VPC, making it simpler and more consistent to scale applications across multiple AZs.

---

### References

- [Introducing Amazon VPC Regional NAT Gateway – AWS Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-vpc-regional-nat-gateway)
- [Amazon VPC NAT Gateway Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
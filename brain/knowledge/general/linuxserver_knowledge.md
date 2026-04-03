---
id: linuxserver-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:04.663140
---

# KNOWLEDGE EXTRACT: linuxserver
> **Extracted on:** 2026-03-30 17:40:21
> **Source:** linuxserver

---

## File: `reverse-proxy-confs.md`
```markdown
# 📦 linuxserver/reverse-proxy-confs [🔖 PENDING/APPROVE]
🔗 https://github.com/linuxserver/reverse-proxy-confs


## Meta
- **Stars:** ⭐ 1606 | **Forks:** 🍴 329
- **Language:** N/A | **License:** GPL-3.0
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
These confs are pulled into our SWAG image: https://github.com/linuxserver/docker-swag

## README (trích đầu)
```
![](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_small.png)

# How to use these Reverse Proxy Configs

This folder contains sample reverse proxy configs for various docker images linuxserver provides and other commonly used applications.

NOTE: We avoid providing samples that publicly expose server management software (ex: syno, qnap, unraid, proxmox, esxi, etc). Pull requests to add samples for this category of applications will not be accepted.

They are grouped in two:

1. `subfolder` these will allow accessing services at https://yourdomain.com/servicename
2. `subdomain` these will allow accessing services at https://servicename.yourdomain.com

It is recommended that users deploy subdomain reverse proxying and not subfolder.

Whilst subfolder reverse proxying appears easier to implement the inherent nature of this technique requires that each application developer make accommodations to support it. This is not always the case and it is common to see applications with no or partial support resulting in an unreliable experience.

Conversely subdomain reverse proxying does not require special accommodation by application developers and will invariably work (or can be made to work) seamlessly without upstream changes.

## To enable the reverse proxy configs:

### Configure your default site config

Make sure that your default site config contains the following lines in the appropriate spots as seen in the default version:

1. For subfolder methods: `include /config/nginx/proxy-confs/*.subfolder.conf;`
2. For subdomain methods: `include /config/nginx/proxy-confs/*.subdomain.conf;`

### Ensure you have a custom docker network

These confs assume that the swag container can reach other containers via their dns hostnames (defaults to container name) resolved via docker's internal dns. This is achieved through having the containers attached to the same user defined docker bridge network.

- If you are using docker-compose and the containers are managed through the same yaml file, docker-compose will automatically create a custom network and attach all containers to it. Nothing extra is required.

- If you are starting the containers via command line, first create a bridge network with the command `docker network create [networkname]` Then define that network in the container run/create command via `--network [networkname]`.

- If you are using a gui manager like portainer, you can create a custom bridge network in the gui, and select it when creating a new container.

- If you are using unraid, create a custom network in command line via `docker network create [networkname]`, then go to docker service settings (under advanced) and set the option `Preserve user defined networks:` to `Yes`. Then in each container setting, including the swag container, in the network type dropdown, select `Custom : [networkname]`. This is a necessary step as the bridge network that unraid uses by default does not al
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


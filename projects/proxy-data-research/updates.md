---
layout: single
title: Weekly Updates
description: "Weekly progress updates from the proxy data research project on algorithmic bias and the socioeconomic impacts of data use."
permalink: /projects/proxy-data-research/updates/
author_profile: true
---

**Navigation:** [Overview](index.md) · [Updates](updates.md) · [Research](research.md)

---

Weekly Updates:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">
        {{ post.date | date: "%Y-%m-%d" }} - {{ post.title }}
      </a>
    </li>
  {% endfor %}
</ul>

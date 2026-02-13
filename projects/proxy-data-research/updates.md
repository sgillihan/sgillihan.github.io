---
layout: default
title: Weekly Updates
permalink: /projects/proxy-data-research/updates/
---

[Home](/) > [Projects](/) > [Proxy Data Research](index.md) > Updates

---

**Navigation:** [Updates](updates.md) · [Research](research.md) · [Overview](overview.md)

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

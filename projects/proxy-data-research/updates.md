---
layout: default
title: Weekly Updates
permalink: /projects/proxy-data-research/updates/
---

[Home](/) > [Projects](/projects/) > [Proxy Data Research](index.md) > Updates

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

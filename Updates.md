---
layout: default
title: Weekly Updates
permalink: /updates/
---

[Home](/) · [Updates](/updates/) · [Research](/research/) · [Project](/project/)

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

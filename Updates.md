---
layout: page
title: Updates
permalink: /updates/
---

Weekly Updates:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%m-%d-%Y }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

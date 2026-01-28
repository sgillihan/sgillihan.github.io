---
layout: page
title: Updates
permalink: /updates/
---

Weekly Updates:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%d-%m-%Y }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

---
title: "{{ replace .Name "-" " " | title }}"
subtitle: ""
date: {{ .Date }}
lastmod: {{ .Date }}
draft: true

description: ""
images: []
resources:
- name: "featured-image"
  src: "books.png"

hiddenFromHomePage: false
hiddenFromSearch: false

tags: []
categories: []

lightgallery: true
twemoji: false
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false
toc:
  enable: true
  auto: true

code:
  copy: true
  maxShownLines: 50
math:
  enable: false
  # ...
mapbox:
  # ...
share:
  enable: true

comment:
  enable: true
---
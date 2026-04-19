# sgillihan.github.io

Personal portfolio website for Stephanie Gillihan — data analyst and pipeline integrity specialist transitioning into software engineering and data science.

Live site: https://sgillihan.github.io

## Projects

- **[Pburst Pressure Calculation Checker](/projects/pburst-pressure-calculation-checker/)** — Burst pressure calculation app that validates ILI vendor-reported pressures against calculated values using reported parameters.
- **[Proxy Data Research: Socioeconomic Impacts](/projects/proxy-data-research/)** — Research project exploring the technical and societal impacts of proxy data use in algorithms and AI/ML systems, with weekly updates and Jupyter notebooks.
- **[Fenwick Tree Sports Tracker](/projects/fenwick-tree-sports-tracker/)** — C++ data structures project demonstrating the Fenwick Tree (Binary Indexed Tree).
- **[One Handy Katie](/projects/one-handy-katie/)** — Client website built with Astro, Sanity CMS, and deployed on Netlify.

## Site Structure

```
sgillihan.github.io/
├── index.md                          # Portfolio homepage / about me
├── _config.yml                       # Jekyll configuration (Minimal Mistakes theme)
├── _data/
│   └── navigation.yml               # Site navigation
├── assets/                          # CSS and images
├── resume/                          # Resume PDF and landing page
└── projects/
    ├── index.md                     # Projects listing page
    ├── pburst-pressure-calculation-checker/
    ├── proxy-data-research/         # Research project
    │   ├── index.md                 # Project landing page
    │   ├── updates.md               # Weekly progress updates
    │   ├── research.md              # Research notebooks index
    │   ├── _posts/                  # Weekly blog posts (weeks 2–12)
    │   ├── code/                    # Python scripts (HMDA, Google data)
    │   ├── data/                    # PDFs: proposal, update reports, DPA planning
    │   └── notebooks/               # Jupyter notebooks (.ipynb + rendered .html)
    ├── fenwick-tree-sports-tracker/
    └── one-handy-katie/
```

## Tech Stack

- **Framework**: Jekyll with [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme
- **Hosting**: GitHub Pages (auto-deployed on push to `main`)

## Local Development

```bash
bundle exec jekyll serve
```

Then navigate to `http://localhost:4000`

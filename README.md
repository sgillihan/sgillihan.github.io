# sgillihan.github.io

Personal portfolio website showcasing my software development projects and research.

## Site Structure

```
sgillihan.github.io/
├── index.md                    # Portfolio homepage
├── resume/                     # Resume files
├── projects/                   # Projects directory
│   ├── proxy-data-research/    # Proxy Data Research project
│   │   ├── index.md            # Project landing page
│   │   ├── updates.md          # Weekly updates
│   │   ├── research.md         # Research notebooks
│   │   ├── overview.md         # Project overview & artifacts
│   │   ├── _posts/             # Blog posts
│   │   ├── code/               # Python scripts
│   │   ├── data/               # Project data
│   │   └── notebooks/          # Jupyter notebooks
│   ├── fenwick-tree-sports-tracker/  # Fenwick Tree project
│   └── one-handy-katie/        # One Handy Katie website
└── _config.yml                 # Jekyll configuration
```

## Local Development

To run the site locally:

```bash
bundle exec jekyll serve
```

Then navigate to `http://localhost:4000`

## Deployment

This site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

Visit the live site at: https://sgillihan.github.io

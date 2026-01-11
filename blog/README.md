---


This repository contains the source code for the engineering blog, built with **Hugo (Extended)** and the **PaperMod** theme.

## 🛠 Prerequisites

* **Hugo Extended** v0.146.0+ (Required for PaperMod SCSS processing)
* **Git**

## 🚀 Quick Start (Local Dev)

To preview the site locally with live reload:

```bash
# Ensure you are in this directory
hugo server -D

```

* **`-D`**: Renders posts marked as `draft: true`.
* **Access:** Open `http://localhost:1313`.

---

## 📝 Creating New Content

### 1. Standard Post

Creates a single markdown file. Best for text-only posts.

```bash
hugo new content posts/my-post-name.md

```

### 2. Page Bundle (Recommended for Images)

Creates a directory containing an `index.md`. This keeps images and content together.

```bash
# Manually creating a bundle structure
mkdir content/posts/my-project-name
hugo new content posts/my-project-name/index.md

```

### 3. Publishing

By default, new posts are **drafts**. To publish:

1. Open the file.
2. Change the front matter:
```yaml
draft: false

```



---

## 🖼 Handling Images

### Method: Page Bundles (Preferred)

If you used the **Page Bundle** method above (folder + `index.md`), place images directly in that folder.

**File Structure:**

```text
content/posts/my-project-name/
├── index.md
├── schematic.png
└── pcb-layout.jpg

```

**Markdown Reference:**

```markdown
![Schematic View](schematic.png)

```

### Method: Global Assets

For generic site assets (logos, favicons).

1. Place file in `static/images/`.
2. Reference as `![Logo](/images/logo.png)`.

---

## ⚙️ Configuration & Theme

* **Config:** `hugo.toml` (Site params, menu, social links).
* **Theme:** `themes/PaperMod`.
* *Note:* Do not edit files inside `themes/` directly. Override them by copying the file to `layouts/` in the root of this directory.



**Updating the Theme:**

```bash
git submodule update --remote --merge

```

---

## 🚢 Deployment (CI/CD)

Deployment is handled automatically by **GitHub Actions**.

1. **Trigger:** The workflow listens for pushes to the `main` branch **only** when files inside the `blog/` directory are modified.
2. **Process:**
* GitHub Actions spins up a runner.
* Installs Hugo Extended.
* Builds the site (`hugo --minify`).
* Deploys to the `gh-pages` branch.



**To Deploy:**
Simply commit and push your changes:

```bash
git add .
git commit -m "New post: Project Stargate update"
git push origin main

```

```

```

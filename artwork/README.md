# Silicon Artwork & Easter Eggs

*Turning empty silicon real estate into a canvas.*

Historically, chip designers have left their mark on the microscopic landscape of integrated circuits—from [cartoons and initials](https://micro.magnet.fsu.edu/creatures/index.html) to complex geometric patterns. This project honors that tradition by etching our story into the metal layers of the 4004 recreation.

## 🎨 The Gallery (Planned Inclusions)

We are utilizing unused whitespace on the die (typically filler cells or decoupling cap areas) to embed the following artwork:

### 1. Tributes
* **Federico Faggin's Signature**: A high-fidelity reproduction of the signature of the 4004's architect. Placed prominently near the main core.
* **Persian Script**: A selection of calligraphy  representing the project's cultural appreciation. *(Rumi, Saadi, Hafez and tell me your favorite verses! [I do have to say, please no Barks. Ideally we have the persian script and the english translation below!]).*

### 2. The Team
* **Designer Signature**: Jeremy King.
* **The Lab Assistants**: Stylized, high-contrast vector portraits of the Pebbles, and Goose!.
    * *Note: Fur textures must be simplified to comply with Minimum Spacing rules.*
    * ![Pebbles]()
    * ![Goose]()

### 3. Community Wall
* **Supporter Doodles**: Small, 10x10 micron "tiles" featuring doodles submitted by the open-source silicon community.

---

## 📐 Technical Constraints (Read Before Submitting)

Unlike printing on paper, etching on silicon requires strict adherence to **Design Rule Checks (DRC)**.

* **Layer**: We are targeting **Metal 5** (Top Metal) or the **Passivation Opening** layer for maximum visibility under an optical microscope.
* **Format**: SVG or DXF (Polygons only, no curves/splines).
* **Grid**: All vertices must snap to the manufacturing grid (0.005µm).
* **Color**: Monochrome (1-bit). There is no "gray"—metal is either present or absent.
* **Density**: We must maintain a metal density between 30% and 70% to prevent "dishing" during Chemical Mechanical Polishing (CMP). Large solid blocks of metal will be rejected.

---

## 📥 How to Suggest or Submit Artwork

We want this chip to represent the community! You can contribute in two ways:

### 1. The Suggestion Box (GitHub Issues)
Have an idea for a doodle or a hidden message?
1.  Go to the **[Issues Tab](../../issues)**.
2.  Create a new issue using the **"Artwork Proposal"** template.
3.  Describe your idea or attach a rough sketch.

### 2. Direct Submission (Pull Request)
If you are familiar with GDSII or vector art:
1.  Fork the repo.
2.  Place your DXF/GDS file in `artwork/submissions/`.
3.  Ensure your design passes the DRC rules listed above.
4.  Open a Pull Request with the tag `[ARTWORK]`.

### 3. "Adopt a Tile"
For major supporters, we are allocating specific 20µm x 20µm regions. Contact Jeremy directly for details.

---

## 🖼️ Preview
*(Screenshots of the GDSII layout showing the artwork will be added here as the design progresses)*

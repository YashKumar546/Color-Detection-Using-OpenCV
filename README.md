# 🎨 Color Detection Using OpenCV

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-orange?style=for-the-badge&logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An interactive **Color Detection** application built with **Python**, **OpenCV**, **NumPy**, and **Pandas**. The project allows users to identify colors by double-clicking on an image while also experimenting with HSV thresholding using interactive trackbars.

---

## ✨ Features

- 🎯 Detects the nearest color name from a color database.
- 🖱️ Double-click anywhere on the image to identify a color.
- 🌈 Displays:
  - Color Name
  - RGB Values
  - HSV Values
- 🎚️ Interactive HSV Trackbars
- 🎭 Live HSV Mask Preview
- 🖼️ Live Color Detection Result
- 📂 Supports multiple images using command-line arguments.
- ⚠️ Error handling for missing image and CSV files.

---

## 📂 Project Structure

```
Color-Detection-Using-OpenCV/
│
├── color_detect.py
├── colors.csv
├── pic1.jpg
├── pic2.jpg
├── pic3.jpg
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
    ├── demo1.png
    ├── demo2.png
    └── demo3.png
```

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Pandas

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/YashKumar546/Color-Detection-Using-OpenCV.git
```

Move into the project folder

```bash
cd Color-Detection-Using-OpenCV
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run with the default image:

```bash
python color_detect.py
```

Run with a specific image:

```bash
python color_detect.py pic2.jpg
```

or

```bash
python color_detect.py myimage.jpg
```

Use a custom color database:

```bash
python color_detect.py pic2.jpg --csv colors.csv
```

---

## 🎮 Controls

| Key / Action | Function |
|--------------|----------|
| 🖱️ Double Left Click | Detect Color |
| **R** | Reset detected color |
| **ESC** | Exit application |

---

## 🧠 How It Works

1. Loads an image.
2. Converts the image from **BGR** to **HSV**.
3. Uses HSV trackbars to create a color mask.
4. Double-clicking a pixel retrieves its RGB values.
5. Finds the nearest matching color from `colors.csv`.
6. Displays:
   - Color Name
   - RGB Values
   - HSV Values
7. Shows:
   - Original Image
   - HSV Mask
   - Detected Color Result

---

## 📸 Screenshots

### Original Image

> Add screenshot here

### HSV Mask

> Add screenshot here

### Detected Color

> Add screenshot here

---

## 📈 Future Improvements

- Detect multiple colors simultaneously.
- Draw contours around detected objects.
- Real-time webcam color detection.
- Save detected color information.
- Export HSV values.
- GUI using Tkinter or PyQt.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yash Kumar**

GitHub: https://github.com/YashKumar546

If you found this project helpful, consider giving it a ⭐ on GitHub!

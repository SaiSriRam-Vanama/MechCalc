# MechCalc

> A professional PyQt6 desktop application for core mechanical engineering calculations with an industrial steel-themed interface.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Modules](#modules)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Educational Purpose](#educational-purpose)
- [Author](#author)
- [License](#license)

---

## Overview

MechCalc is a comprehensive GUI toolkit that provides **8 essential mechanical engineering calculation modules** in a single, cohesive desktop application. Built with **PyQt6**, it features a CNC-machine-inspired dark steel interface for a professional engineering feel.

---

## Features

- **Industrial Steel Theme** — Dark CNC-machine-inspired UI with custom QSS styling
- **8 Interactive Modules** — Tabbed interface for quick switching between calculations
- **Real-time Status Bar** — Visual feedback on all operations
- **Error Handling** — Input validation with descriptive error messages
- **Responsive Layout** — Grid-based input/output fields with clear separation
- **Menu Bar** — File and Help menus with About dialog
- **Cross-Platform** — Runs on Windows, macOS, and Linux

---

## Modules

| # | Module | Inputs | Outputs |
|---|--------|--------|---------|
| 1 | Stress-Strain Analysis | Force (N), Area (mm^2), Original Length (mm), Change in Length (mm) | Stress, Strain, Young's Modulus |
| 2 | Beam Bending | Span (m), Central Load (kN), Allowable Stress (MPa), E (GPa), I (cm^4) | Max Bending Moment, Shear Force, Section Modulus, Deflection |
| 3 | Shaft Design | Power (kW), Speed (rpm), Allowable Shear Stress (MPa) | Torque, Required Diameter |
| 4 | Gear Train | Driver Teeth, Driven Teeth, Input Speed (rpm), Input Torque (N-m) | Speed Ratio, Output Speed, Output Torque |
| 5 | Spring Design | Axial Load (N), Deflection (mm), Wire Diameter (mm), Mean Coil Diameter (mm) | Spring Stiffness, Shear Stress |
| 6 | Thermal Expansion | Coefficient (1/C), Original Length (mm), Temperature Change (C), Young's Modulus (MPa) | Change in Length, Final Length, Thermal Stress |
| 7 | Fluid Mechanics | Density (kg/m^3), Viscosity (Pa-s), Pipe Diameter (m), Velocity (m/s), Length (m), Friction Factor | Reynolds Number, Flow Regime, Friction Factor, Head Loss |
| 8 | Heat Transfer | k (W/m-K), Area (m^2), dT (K), Thickness (m), h (W/m^2-K) | Conduction Rate, Convection Rate |

### Formulas Used

| Module | Key Formula |
|--------|------------|
| Stress-Strain | sigma = F / A, epsilon = dL / L0, E = sigma / epsilon |
| Beam Bending | M_max = W * L / 4, V_max = W / 2, Z_req = M / sigma_allow |
| Shaft Design | T = (P * 60) / (2 * pi * N), d = (16T / (pi * tau))^(1/3) |
| Gear Train | VR = T2 / T1, N2 = N1 / VR, T2 = T1 * VR |
| Spring Design | k = F / delta, tau = (8 * F * D) / (pi * d^3) |
| Thermal Expansion | dL = alpha * L0 * dT, sigma = E * alpha * dT |
| Fluid Mechanics | Re = rho * V * D / mu, hf = f * (L/D) * (V^2 / 2g) |
| Heat Transfer | q_cond = k * A * dT / L, q_conv = h * A * dT |

---

## Screenshots

<!-- Add screenshots here -->

---

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Steps

```bash
# Clone the repository
git clone https://github.com/SaiSriRam-Vanama/MechCalc.git

# Navigate to project directory
cd MechCalc

# Install dependencies
pip install -r requirements.txt

# Run the application
python mechanical_toolkit_pyqt.py
```

---

## Usage

1. Launch the application using `python mechanical_toolkit_pyqt.py`
2. Select a calculation module from the tab bar at the top
3. Enter input parameters in the designated fields
4. Click **Calculate** to compute results
5. Use **Clear** to reset all fields in the current tab
6. Check the status bar at the bottom for operation feedback

---

## Project Structure

```
MechCalc/
├── mechanical_toolkit_pyqt.py   # Main application source code
├── requirements.txt              # Python package dependencies
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

---

## Requirements

- **Python** — 3.11+
- **PyQt6** — 6.4+

---

## Educational Purpose

> **Disclaimer:** The formulas and calculations implemented in this software are for **educational purposes only**. They should not be used for critical industrial design, safety-critical applications, or professional engineering decisions. Always verify critical results with certified engineering software and consult a qualified professional engineer.

---

## Author

**Sai Sri Ram Vanama**

- LinkedIn: [saisriramv](https://linkedin.com/in/saisriramv)
- GitHub: [SaiSriRam-Vanama](https://github.com/SaiSriRam-Vanama)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

"""
Mechanical Engineering All-In-One Calculator - PyQt6 Version
==============================================================
A professional desktop GUI application for core mechanical engineering calculations.

Features:
- Industrial Steel Theme (CNC machine interface aesthetic)
- Professional PyQt6 interface with QSS styling
- Mechanical engineering symbols for each module
- 8 comprehensive calculation modules

Modules/Tabs:
1. ⚡ Stress-Strain Analysis
2. 📏 Beam Bending (Simply Supported, Central Load)
3. ⚙ Shaft Design for Power Transmission
4. 🔧 Gear Train Calculations
5. 🔩 Spring Design (Helical Compression)
6. 🌡 Thermal Expansion
7. 💧 Fluid Mechanics (Reynolds Number & Head Loss)
8. 🔥 Heat Transfer (Conduction & Convection)

Requirements:
    pip install PyQt6

How to run:
    python mechanical_toolkit_pyqt.py

Note: Formulas are for educational purposes. Not for critical industrial design.
"""

import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QLineEdit, QPushButton, QGroupBox,
    QGridLayout, QMessageBox, QStatusBar, QMenuBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MechanicalToolkitApp(QMainWindow):
    """Main application class for Mechanical Engineering Calculator."""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("⚙ MechCalc")
        self.setGeometry(100, 100, 1300, 750)
        
        # Apply Industrial Steel Theme
        self.apply_industrial_theme()
        
        # Build UI components
        self.build_menu()
        self.build_main_ui()
        self.build_status_bar()
        
    def apply_industrial_theme(self):
        """Apply Industrial Steel Theme using QSS (Qt StyleSheets)."""
        qss = """
        /* Industrial Steel Color Palette */
        QMainWindow {
            background-color: #1F1F1F;
        }
        
        QWidget {
            background-color: #1F1F1F;
            color: #FFFFFF;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 10pt;
        }
        
        /* Header styling */
        QLabel#header {
            background-color: #2C2C2C;
            color: #C0C0C0;
            font-size: 20pt;
            font-weight: bold;
            padding: 15px;
            border: 2px solid #4A4A4A;
            border-radius: 5px;
        }
        
        QLabel#subtitle {
            background-color: #2C2C2C;
            color: #FFFFFF;
            font-size: 11pt;
            padding: 8px;
        }
        
        /* Tab Widget */
        QTabWidget::pane {
            border: 2px solid #4A4A4A;
            background-color: #2C2C2C;
            border-radius: 5px;
        }
        
        QTabBar::tab {
            background-color: #3D3D3D;
            color: #FFFFFF;
            padding: 12px 20px;
            margin: 2px;
            border: 2px solid #4A4A4A;
            border-bottom: none;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            font-weight: bold;
            font-size: 10pt;
        }
        
        QTabBar::tab:selected {
            background-color: #2C2C2C;
            color: #C0C0C0;
            border: 2px solid #C0C0C0;
            border-bottom: none;
        }
        
        QTabBar::tab:hover {
            background-color: #E6E6E6;
            color: #1F1F1F;
        }
        
        /* Group Boxes (Frames) */
        QGroupBox {
            background-color: #2C2C2C;
            border: 2px solid #4A4A4A;
            border-radius: 5px;
            margin-top: 10px;
            padding: 15px;
            font-weight: bold;
            color: #C0C0C0;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 5px 10px;
            color: #C0C0C0;
            font-size: 11pt;
        }
        
        /* Labels */
        QLabel {
            color: #FFFFFF;
            background-color: transparent;
            font-size: 10pt;
        }
        
        /* Line Edits (Input fields) */
        QLineEdit {
            background-color: #3D3D3D;
            color: #FFFFFF;
            border: 2px solid #4A4A4A;
            border-radius: 3px;
            padding: 6px;
            font-size: 10pt;
        }
        
        QLineEdit:focus {
            border: 2px solid #C0C0C0;
        }
        
        QLineEdit:read-only {
            background-color: #2C2C2C;
            color: #C0C0C0;
        }
        
        /* Buttons */
        QPushButton {
            background-color: #3D3D3D;
            color: #FFFFFF;
            border: 2px solid #4A4A4A;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 10pt;
        }
        
        QPushButton:hover {
            background-color: #E6E6E6;
            color: #1F1F1F;
            border: 2px solid #C0C0C0;
        }
        
        QPushButton:pressed {
            background-color: #C0C0C0;
            color: #1F1F1F;
        }
        
        /* Status Bar */
        QStatusBar {
            background-color: #2C2C2C;
            color: #FFFFFF;
            border-top: 2px solid #4A4A4A;
            font-size: 10pt;
        }
        
        /* Menu Bar */
        QMenuBar {
            background-color: #2C2C2C;
            color: #FFFFFF;
            border-bottom: 2px solid #4A4A4A;
        }
        
        QMenuBar::item {
            background-color: transparent;
            padding: 5px 10px;
        }
        
        QMenuBar::item:selected {
            background-color: #3D3D3D;
        }
        
        QMenu {
            background-color: #2C2C2C;
            color: #FFFFFF;
            border: 2px solid #4A4A4A;
        }
        
        QMenu::item:selected {
            background-color: #3D3D3D;
        }
        """
        self.setStyleSheet(qss)
        
    def build_menu(self):
        """Create menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def show_about(self):
        """Show about dialog."""
        QMessageBox.information(
            self,
            "About",
            "⚙ MechCalc — Mechanical Engineering Calculator\n\n"
            "A comprehensive toolkit for core mechanical engineering calculations.\n\n"
            "Professional PyQt6 Interface\n"
            "Industrial Steel Theme\n\n"
            "Educational purposes only.\n"
            "Version 2.0 (PyQt6)"
        )
        
    def build_main_ui(self):
        """Build main user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Header
        header = QLabel("⚙ MECHCALC")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)
        
        subtitle = QLabel("Professional Toolkit for Core Mechanical Engineering Calculations")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)
        
        # Tab Widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create all tabs
        self.build_stress_tab()
        self.build_beam_tab()
        self.build_shaft_tab()
        self.build_gear_tab()
        self.build_spring_tab()
        self.build_thermal_tab()
        self.build_fluid_tab()
        self.build_heat_transfer_tab()
        
    def build_status_bar(self):
        """Create status bar."""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
    def update_status(self, message):
        """Update status bar message."""
        self.status_bar.showMessage(message)
        
    # ========== TAB 1: STRESS-STRAIN ==========
    def build_stress_tab(self):
        """Build Stress-Strain calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "⚡ Stress-Strain")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input Parameters")
        input_layout = QGridLayout()
        
        self.stress_force = QLineEdit()
        self.stress_area = QLineEdit()
        self.stress_L0 = QLineEdit()
        self.stress_dL = QLineEdit()
        
        input_layout.addWidget(QLabel("Force F (N):"), 0, 0)
        input_layout.addWidget(self.stress_force, 0, 1)
        input_layout.addWidget(QLabel("Area A (mm²):"), 1, 0)
        input_layout.addWidget(self.stress_area, 1, 1)
        input_layout.addWidget(QLabel("Original Length L₀ (mm):"), 2, 0)
        input_layout.addWidget(self.stress_L0, 2, 1)
        input_layout.addWidget(QLabel("Change in Length ΔL (mm):"), 3, 0)
        input_layout.addWidget(self.stress_dL, 3, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.stress_sigma = QLineEdit("—")
        self.stress_sigma.setReadOnly(True)
        self.stress_epsilon = QLineEdit("—")
        self.stress_epsilon.setReadOnly(True)
        self.stress_E = QLineEdit("—")
        self.stress_E.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Stress σ (MPa):"), 0, 0)
        output_layout.addWidget(self.stress_sigma, 0, 1)
        output_layout.addWidget(QLabel("Strain ε:"), 1, 0)
        output_layout.addWidget(self.stress_epsilon, 1, 1)
        output_layout.addWidget(QLabel("Young's Modulus E (MPa):"), 2, 0)
        output_layout.addWidget(self.stress_E, 2, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_stress_strain)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_stress_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 3, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_stress_strain(self):
        """Calculate stress, strain, and Young's modulus."""
        try:
            F = float(self.stress_force.text())
            A = float(self.stress_area.text())
            L0 = float(self.stress_L0.text())
            dL = float(self.stress_dL.text())
            
            if A <= 0:
                raise ValueError("Area must be positive")
            if L0 <= 0:
                raise ValueError("Original length must be positive")
                
            # Stress: σ = F/A (N/mm² = MPa)
            sigma = F / A
            self.stress_sigma.setText(f"{sigma:.4f}")
            
            # Strain: ε = ΔL/L₀
            epsilon = dL / L0
            self.stress_epsilon.setText(f"{epsilon:.6f}")
            
            # Young's Modulus: E = σ/ε
            if abs(epsilon) > 1e-10:
                E = sigma / epsilon
                self.stress_E.setText(f"{E:.2f}")
            else:
                self.stress_E.setText("N/A (strain ≈ 0)")
                
            self.update_status("Stress-Strain calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_stress_tab(self):
        """Clear all fields in stress-strain tab."""
        self.stress_force.clear()
        self.stress_area.clear()
        self.stress_L0.clear()
        self.stress_dL.clear()
        self.stress_sigma.setText("—")
        self.stress_epsilon.setText("—")
        self.stress_E.setText("—")
        self.update_status("Stress-Strain tab cleared")
        
    # ========== TAB 2: BEAM BENDING ==========
    def build_beam_tab(self):
        """Build Beam Bending calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "📏 Beam Bending")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input (Simply Supported, Central Load)")
        input_layout = QGridLayout()
        
        self.beam_L = QLineEdit()
        self.beam_W = QLineEdit()
        self.beam_sigma_allow = QLineEdit()
        self.beam_E = QLineEdit()
        self.beam_I = QLineEdit()
        
        input_layout.addWidget(QLabel("Span L (m):"), 0, 0)
        input_layout.addWidget(self.beam_L, 0, 1)
        input_layout.addWidget(QLabel("Central Load W (kN):"), 1, 0)
        input_layout.addWidget(self.beam_W, 1, 1)
        input_layout.addWidget(QLabel("Allowable Stress σ_allow (MPa):"), 2, 0)
        input_layout.addWidget(self.beam_sigma_allow, 2, 1)
        input_layout.addWidget(QLabel("Modulus E (GPa, optional):"), 3, 0)
        input_layout.addWidget(self.beam_E, 3, 1)
        input_layout.addWidget(QLabel("Moment of Inertia I (cm⁴, optional):"), 4, 0)
        input_layout.addWidget(self.beam_I, 4, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.beam_M_max = QLineEdit("—")
        self.beam_M_max.setReadOnly(True)
        self.beam_V_max = QLineEdit("—")
        self.beam_V_max.setReadOnly(True)
        self.beam_Z_req = QLineEdit("—")
        self.beam_Z_req.setReadOnly(True)
        self.beam_delta = QLineEdit("—")
        self.beam_delta.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Max Bending Moment M_max (kN·m):"), 0, 0)
        output_layout.addWidget(self.beam_M_max, 0, 1)
        output_layout.addWidget(QLabel("Max Shear Force V_max (kN):"), 1, 0)
        output_layout.addWidget(self.beam_V_max, 1, 1)
        output_layout.addWidget(QLabel("Required Section Modulus Z (mm³):"), 2, 0)
        output_layout.addWidget(self.beam_Z_req, 2, 1)
        output_layout.addWidget(QLabel("Mid-span Deflection δ (mm):"), 3, 0)
        output_layout.addWidget(self.beam_delta, 3, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_beam)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_beam_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 4, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_beam(self):
        """Calculate beam bending parameters."""
        try:
            L = float(self.beam_L.text())
            W = float(self.beam_W.text())
            sigma_allow = float(self.beam_sigma_allow.text())
            
            if L <= 0 or W <= 0 or sigma_allow <= 0:
                raise ValueError("All values must be positive")
                
            # Max bending moment: M = WL/4
            M_max_kNm = W * L / 4
            self.beam_M_max.setText(f"{M_max_kNm:.4f}")
            
            # Max shear force: V = W/2
            V_max = W / 2
            self.beam_V_max.setText(f"{V_max:.4f}")
            
            # Required section modulus: Z = M/σ
            M_Nmm = M_max_kNm * 1e6
            Z_req = M_Nmm / sigma_allow
            self.beam_Z_req.setText(f"{Z_req:.2f}")
            
            # Deflection (if E and I provided)
            if self.beam_E.text() and self.beam_I.text():
                E_GPa = float(self.beam_E.text())
                I_cm4 = float(self.beam_I.text())
                
                E_Nmm2 = E_GPa * 1000
                I_mm4 = I_cm4 * 1e4
                
                W_N = W * 1000
                L_mm = L * 1000
                delta_mm = (W_N * L_mm**3) / (48 * E_Nmm2 * I_mm4)
                self.beam_delta.setText(f"{delta_mm:.4f}")
            else:
                self.beam_delta.setText("N/A (E or I not provided)")
                
            self.update_status("Beam bending calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_beam_tab(self):
        """Clear beam bending tab."""
        self.beam_L.clear()
        self.beam_W.clear()
        self.beam_sigma_allow.clear()
        self.beam_E.clear()
        self.beam_I.clear()
        self.beam_M_max.setText("—")
        self.beam_V_max.setText("—")
        self.beam_Z_req.setText("—")
        self.beam_delta.setText("—")
        self.update_status("Beam tab cleared")
        
    # ========== TAB 3: SHAFT DESIGN ==========
    def build_shaft_tab(self):
        """Build Shaft Design calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "⚙ Shaft Design")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input (Solid Circular Shaft)")
        input_layout = QGridLayout()
        
        self.shaft_P = QLineEdit()
        self.shaft_N = QLineEdit()
        self.shaft_tau_allow = QLineEdit()
        
        input_layout.addWidget(QLabel("Power P (kW):"), 0, 0)
        input_layout.addWidget(self.shaft_P, 0, 1)
        input_layout.addWidget(QLabel("Speed N (rpm):"), 1, 0)
        input_layout.addWidget(self.shaft_N, 1, 1)
        input_layout.addWidget(QLabel("Allowable Shear Stress τ_allow (MPa):"), 2, 0)
        input_layout.addWidget(self.shaft_tau_allow, 2, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.shaft_T = QLineEdit("—")
        self.shaft_T.setReadOnly(True)
        self.shaft_d = QLineEdit("—")
        self.shaft_d.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Torque T (N·m):"), 0, 0)
        output_layout.addWidget(self.shaft_T, 0, 1)
        output_layout.addWidget(QLabel("Required Diameter d (mm):"), 1, 0)
        output_layout.addWidget(self.shaft_d, 1, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_shaft)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_shaft_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 2, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_shaft(self):
        """Calculate shaft torque and diameter."""
        try:
            P_kW = float(self.shaft_P.text())
            N_rpm = float(self.shaft_N.text())
            tau_allow = float(self.shaft_tau_allow.text())
            
            if P_kW <= 0 or N_rpm <= 0 or tau_allow <= 0:
                raise ValueError("All values must be positive")
                
            # Torque: T = (P * 60) / (2π * N)
            P_W = P_kW * 1000
            T_Nm = (P_W * 60) / (2 * math.pi * N_rpm)
            self.shaft_T.setText(f"{T_Nm:.4f}")
            
            # Diameter: τ = 16T/(πd³) → d = (16T/(πτ))^(1/3)
            T_Nmm = T_Nm * 1000
            d_mm = ((16 * T_Nmm) / (math.pi * tau_allow)) ** (1/3)
            self.shaft_d.setText(f"{d_mm:.4f}")
            
            self.update_status("Shaft design calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_shaft_tab(self):
        """Clear shaft design tab."""
        self.shaft_P.clear()
        self.shaft_N.clear()
        self.shaft_tau_allow.clear()
        self.shaft_T.setText("—")
        self.shaft_d.setText("—")
        self.update_status("Shaft tab cleared")
        
    # ========== TAB 4: GEAR TRAIN ==========
    def build_gear_tab(self):
        """Build Gear Train calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "🔧 Gear Train")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input (Simple Gear Train)")
        input_layout = QGridLayout()
        
        self.gear_T1 = QLineEdit()
        self.gear_T2 = QLineEdit()
        self.gear_N1 = QLineEdit()
        self.gear_Torque1 = QLineEdit()
        
        input_layout.addWidget(QLabel("Driver Teeth T₁:"), 0, 0)
        input_layout.addWidget(self.gear_T1, 0, 1)
        input_layout.addWidget(QLabel("Driven Teeth T₂:"), 1, 0)
        input_layout.addWidget(self.gear_T2, 1, 1)
        input_layout.addWidget(QLabel("Input Speed N₁ (rpm):"), 2, 0)
        input_layout.addWidget(self.gear_N1, 2, 1)
        input_layout.addWidget(QLabel("Input Torque T₁ (N·m, optional):"), 3, 0)
        input_layout.addWidget(self.gear_Torque1, 3, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.gear_VR = QLineEdit("—")
        self.gear_VR.setReadOnly(True)
        self.gear_N2 = QLineEdit("—")
        self.gear_N2.setReadOnly(True)
        self.gear_Torque2 = QLineEdit("—")
        self.gear_Torque2.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Speed Ratio (VR):"), 0, 0)
        output_layout.addWidget(self.gear_VR, 0, 1)
        output_layout.addWidget(QLabel("Output Speed N₂ (rpm):"), 1, 0)
        output_layout.addWidget(self.gear_N2, 1, 1)
        output_layout.addWidget(QLabel("Output Torque T₂ (N·m):"), 2, 0)
        output_layout.addWidget(self.gear_Torque2, 2, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_gear)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_gear_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 3, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_gear(self):
        """Calculate gear train parameters."""
        try:
            T1 = int(self.gear_T1.text())
            T2 = int(self.gear_T2.text())
            N1 = float(self.gear_N1.text())
            
            if T1 <= 0 or T2 <= 0 or N1 <= 0:
                raise ValueError("All values must be positive")
                
            # Speed ratio: VR = T2/T1
            VR = T2 / T1
            self.gear_VR.setText(f"{VR:.4f}")
            
            # Output speed: N2 = N1/VR
            N2 = N1 / VR
            self.gear_N2.setText(f"{N2:.4f}")
            
            # Output torque (if input torque provided)
            if self.gear_Torque1.text():
                Torque1 = float(self.gear_Torque1.text())
                Torque2 = Torque1 * VR
                self.gear_Torque2.setText(f"{Torque2:.4f}")
            else:
                self.gear_Torque2.setText("N/A (input torque not provided)")
                
            self.update_status("Gear train calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_gear_tab(self):
        """Clear gear train tab."""
        self.gear_T1.clear()
        self.gear_T2.clear()
        self.gear_N1.clear()
        self.gear_Torque1.clear()
        self.gear_VR.setText("—")
        self.gear_N2.setText("—")
        self.gear_Torque2.setText("—")
        self.update_status("Gear tab cleared")
        
    # ========== TAB 5: SPRING DESIGN ==========
    def build_spring_tab(self):
        """Build Spring Design calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "🔩 Spring Design")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input (Helical Compression Spring)")
        input_layout = QGridLayout()
        
        self.spring_F = QLineEdit()
        self.spring_delta = QLineEdit()
        self.spring_d = QLineEdit()
        self.spring_D = QLineEdit()
        
        input_layout.addWidget(QLabel("Axial Load F (N):"), 0, 0)
        input_layout.addWidget(self.spring_F, 0, 1)
        input_layout.addWidget(QLabel("Deflection δ (mm):"), 1, 0)
        input_layout.addWidget(self.spring_delta, 1, 1)
        input_layout.addWidget(QLabel("Wire Diameter d (mm):"), 2, 0)
        input_layout.addWidget(self.spring_d, 2, 1)
        input_layout.addWidget(QLabel("Mean Coil Diameter D (mm):"), 3, 0)
        input_layout.addWidget(self.spring_D, 3, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.spring_k = QLineEdit("—")
        self.spring_k.setReadOnly(True)
        self.spring_tau = QLineEdit("—")
        self.spring_tau.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Spring Stiffness k (N/mm):"), 0, 0)
        output_layout.addWidget(self.spring_k, 0, 1)
        output_layout.addWidget(QLabel("Shear Stress τ (MPa):"), 1, 0)
        output_layout.addWidget(self.spring_tau, 1, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_spring)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_spring_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 2, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_spring(self):
        """Calculate spring parameters."""
        try:
            F = float(self.spring_F.text())
            delta = float(self.spring_delta.text())
            d = float(self.spring_d.text())
            D = float(self.spring_D.text())
            
            if F <= 0 or delta <= 0 or d <= 0 or D <= 0:
                raise ValueError("All values must be positive")
                
            # Spring stiffness: k = F/δ
            k = F / delta
            self.spring_k.setText(f"{k:.4f}")
            
            # Shear stress: τ = 8FD/(πd³)
            tau = (8 * F * D) / (math.pi * d**3)
            self.spring_tau.setText(f"{tau:.4f}")
            
            self.update_status("Spring design calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_spring_tab(self):
        """Clear spring design tab."""
        self.spring_F.clear()
        self.spring_delta.clear()
        self.spring_d.clear()
        self.spring_D.clear()
        self.spring_k.setText("—")
        self.spring_tau.setText("—")
        self.update_status("Spring tab cleared")
        
    # ========== TAB 6: THERMAL EXPANSION ==========
    def build_thermal_tab(self):
        """Build Thermal Expansion calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "🌡 Thermal Expansion")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input")
        input_layout = QGridLayout()
        
        self.thermal_alpha = QLineEdit()
        self.thermal_L0 = QLineEdit()
        self.thermal_dT = QLineEdit()
        self.thermal_E = QLineEdit()
        
        input_layout.addWidget(QLabel("Coefficient α (1/°C):"), 0, 0)
        input_layout.addWidget(self.thermal_alpha, 0, 1)
        input_layout.addWidget(QLabel("Original Length L₀ (mm):"), 1, 0)
        input_layout.addWidget(self.thermal_L0, 1, 1)
        input_layout.addWidget(QLabel("Temperature Change ΔT (°C):"), 2, 0)
        input_layout.addWidget(self.thermal_dT, 2, 1)
        input_layout.addWidget(QLabel("Young's Modulus E (MPa, optional):"), 3, 0)
        input_layout.addWidget(self.thermal_E, 3, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.thermal_dL = QLineEdit("—")
        self.thermal_dL.setReadOnly(True)
        self.thermal_Lf = QLineEdit("—")
        self.thermal_Lf.setReadOnly(True)
        self.thermal_sigma = QLineEdit("—")
        self.thermal_sigma.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Change in Length ΔL (mm):"), 0, 0)
        output_layout.addWidget(self.thermal_dL, 0, 1)
        output_layout.addWidget(QLabel("Final Length L (mm):"), 1, 0)
        output_layout.addWidget(self.thermal_Lf, 1, 1)
        output_layout.addWidget(QLabel("Thermal Stress σ (MPa):"), 2, 0)
        output_layout.addWidget(self.thermal_sigma, 2, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_thermal)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_thermal_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 3, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_thermal(self):
        """Calculate thermal expansion."""
        try:
            alpha = float(self.thermal_alpha.text())
            L0 = float(self.thermal_L0.text())
            dT = float(self.thermal_dT.text())
            
            if L0 <= 0:
                raise ValueError("Original length must be positive")
                
            # Change in length: ΔL = α * L₀ * ΔT
            dL = alpha * L0 * dT
            self.thermal_dL.setText(f"{dL:.6f}")
            
            # Final length
            Lf = L0 + dL
            self.thermal_Lf.setText(f"{Lf:.6f}")
            
            # Thermal stress (if E provided and restrained)
            if self.thermal_E.text():
                E = float(self.thermal_E.text())
                sigma_thermal = E * alpha * dT
                self.thermal_sigma.setText(f"{sigma_thermal:.4f}")
            else:
                self.thermal_sigma.setText("N/A (E not provided)")
                
            self.update_status("Thermal expansion calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_thermal_tab(self):
        """Clear thermal expansion tab."""
        self.thermal_alpha.clear()
        self.thermal_L0.clear()
        self.thermal_dT.clear()
        self.thermal_E.clear()
        self.thermal_dL.setText("—")
        self.thermal_Lf.setText("—")
        self.thermal_sigma.setText("—")
        self.update_status("Thermal tab cleared")
        
    # ========== TAB 7: FLUID MECHANICS ==========
    def build_fluid_tab(self):
        """Build Fluid Mechanics calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "💧 Fluid Mechanics")
        
        layout = QHBoxLayout(tab)
        
        # Input group
        input_group = QGroupBox("Input (Pipe Flow)")
        input_layout = QGridLayout()
        
        self.fluid_rho = QLineEdit()
        self.fluid_mu = QLineEdit()
        self.fluid_D = QLineEdit()
        self.fluid_V = QLineEdit()
        self.fluid_L = QLineEdit()
        self.fluid_f = QLineEdit()
        
        input_layout.addWidget(QLabel("Density ρ (kg/m³):"), 0, 0)
        input_layout.addWidget(self.fluid_rho, 0, 1)
        input_layout.addWidget(QLabel("Dynamic Viscosity μ (Pa·s):"), 1, 0)
        input_layout.addWidget(self.fluid_mu, 1, 1)
        input_layout.addWidget(QLabel("Pipe Diameter D (m):"), 2, 0)
        input_layout.addWidget(self.fluid_D, 2, 1)
        input_layout.addWidget(QLabel("Velocity V (m/s):"), 3, 0)
        input_layout.addWidget(self.fluid_V, 3, 1)
        input_layout.addWidget(QLabel("Pipe Length L (m):"), 4, 0)
        input_layout.addWidget(self.fluid_L, 4, 1)
        input_layout.addWidget(QLabel("Friction Factor f (optional):"), 5, 0)
        input_layout.addWidget(self.fluid_f, 5, 1)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Output group
        output_group = QGroupBox("Results")
        output_layout = QGridLayout()
        
        self.fluid_Re = QLineEdit("—")
        self.fluid_Re.setReadOnly(True)
        self.fluid_regime = QLineEdit("—")
        self.fluid_regime.setReadOnly(True)
        self.fluid_f_calc = QLineEdit("—")
        self.fluid_f_calc.setReadOnly(True)
        self.fluid_hf = QLineEdit("—")
        self.fluid_hf.setReadOnly(True)
        
        output_layout.addWidget(QLabel("Reynolds Number Re:"), 0, 0)
        output_layout.addWidget(self.fluid_Re, 0, 1)
        output_layout.addWidget(QLabel("Flow Regime:"), 1, 0)
        output_layout.addWidget(self.fluid_regime, 1, 1)
        output_layout.addWidget(QLabel("Friction Factor f:"), 2, 0)
        output_layout.addWidget(self.fluid_f_calc, 2, 1)
        output_layout.addWidget(QLabel("Head Loss h_f (m):"), 3, 0)
        output_layout.addWidget(self.fluid_hf, 3, 1)
        
        # Buttons
        btn_layout = QHBoxLayout()
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_fluid)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_fluid_tab)
        btn_layout.addWidget(calc_btn)
        btn_layout.addWidget(clear_btn)
        output_layout.addLayout(btn_layout, 4, 0, 1, 2)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
    def calculate_fluid(self):
        """Calculate fluid mechanics parameters."""
        try:
            rho = float(self.fluid_rho.text())
            mu = float(self.fluid_mu.text())
            D = float(self.fluid_D.text())
            V = float(self.fluid_V.text())
            L = float(self.fluid_L.text())
            
            if rho <= 0 or mu <= 0 or D <= 0 or V < 0 or L <= 0:
                raise ValueError("Values must be positive (velocity ≥ 0)")
                
            # Reynolds number: Re = ρVD/μ
            Re = (rho * V * D) / mu
            self.fluid_Re.setText(f"{Re:.2f}")
            
            # Flow regime
            if Re < 2000:
                regime = "Laminar"
            elif Re < 4000:
                regime = "Transitional"
            else:
                regime = "Turbulent"
            self.fluid_regime.setText(regime)
            
            # Friction factor
            if self.fluid_f.text():
                f = float(self.fluid_f.text())
            else:
                if Re < 2000:
                    f = 64 / Re if Re > 0 else 0
                else:
                    f = 0.316 / (Re ** 0.25) if Re > 0 else 0
            self.fluid_f_calc.setText(f"{f:.6f}")
            
            # Head loss: h_f = f * (L/D) * (V²/2g)
            g = 9.81
            hf = f * (L / D) * (V**2 / (2 * g))
            self.fluid_hf.setText(f"{hf:.6f}")
            
            self.update_status("Fluid mechanics calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_fluid_tab(self):
        """Clear fluid mechanics tab."""
        self.fluid_rho.clear()
        self.fluid_mu.clear()
        self.fluid_D.clear()
        self.fluid_V.clear()
        self.fluid_L.clear()
        self.fluid_f.clear()
        self.fluid_Re.setText("—")
        self.fluid_regime.setText("—")
        self.fluid_f_calc.setText("—")
        self.fluid_hf.setText("—")
        self.update_status("Fluid tab cleared")
        
    # ========== TAB 8: HEAT TRANSFER ==========
    def build_heat_transfer_tab(self):
        """Build Heat Transfer calculator tab."""
        tab = QWidget()
        self.tabs.addTab(tab, "🔥 Heat Transfer")
        
        main_layout = QVBoxLayout(tab)
        top_layout = QHBoxLayout()
        
        # Conduction section
        cond_group = QGroupBox("Conduction (1D Steady-State)")
        cond_layout = QGridLayout()
        
        self.cond_k = QLineEdit()
        self.cond_A = QLineEdit()
        self.cond_dT = QLineEdit()
        self.cond_L = QLineEdit()
        self.cond_q = QLineEdit("—")
        self.cond_q.setReadOnly(True)
        
        cond_layout.addWidget(QLabel("Thermal Conductivity k (W/m·K):"), 0, 0)
        cond_layout.addWidget(self.cond_k, 0, 1)
        cond_layout.addWidget(QLabel("Area A (m²):"), 1, 0)
        cond_layout.addWidget(self.cond_A, 1, 1)
        cond_layout.addWidget(QLabel("Temperature Difference ΔT (K):"), 2, 0)
        cond_layout.addWidget(self.cond_dT, 2, 1)
        cond_layout.addWidget(QLabel("Thickness L (m):"), 3, 0)
        cond_layout.addWidget(self.cond_L, 3, 1)
        cond_layout.addWidget(QLabel("Heat Transfer Rate q (W):"), 4, 0)
        cond_layout.addWidget(self.cond_q, 4, 1)
        
        calc_cond_btn = QPushButton("Calculate Conduction")
        calc_cond_btn.clicked.connect(self.calculate_conduction)
        cond_layout.addWidget(calc_cond_btn, 5, 0, 1, 2)
        
        cond_group.setLayout(cond_layout)
        top_layout.addWidget(cond_group)
        
        # Convection section
        conv_group = QGroupBox("Convection")
        conv_layout = QGridLayout()
        
        self.conv_h = QLineEdit()
        self.conv_A = QLineEdit()
        self.conv_dT = QLineEdit()
        self.conv_q = QLineEdit("—")
        self.conv_q.setReadOnly(True)
        
        conv_layout.addWidget(QLabel("Heat Transfer Coefficient h (W/m²·K):"), 0, 0)
        conv_layout.addWidget(self.conv_h, 0, 1)
        conv_layout.addWidget(QLabel("Area A (m²):"), 1, 0)
        conv_layout.addWidget(self.conv_A, 1, 1)
        conv_layout.addWidget(QLabel("Temperature Difference ΔT (K):"), 2, 0)
        conv_layout.addWidget(self.conv_dT, 2, 1)
        conv_layout.addWidget(QLabel("Heat Transfer Rate q (W):"), 3, 0)
        conv_layout.addWidget(self.conv_q, 3, 1)
        
        calc_conv_btn = QPushButton("Calculate Convection")
        calc_conv_btn.clicked.connect(self.calculate_convection)
        conv_layout.addWidget(calc_conv_btn, 4, 0, 1, 2)
        
        conv_group.setLayout(conv_layout)
        top_layout.addWidget(conv_group)
        
        main_layout.addLayout(top_layout)
        
        # Clear button
        clear_btn = QPushButton("Clear All")
        clear_btn.clicked.connect(self.clear_heat_tab)
        main_layout.addWidget(clear_btn)
        
    def calculate_conduction(self):
        """Calculate conduction heat transfer."""
        try:
            k = float(self.cond_k.text())
            A = float(self.cond_A.text())
            dT = float(self.cond_dT.text())
            L = float(self.cond_L.text())
            
            if k <= 0 or A <= 0 or L <= 0:
                raise ValueError("k, A, and L must be positive")
                
            # q = k * A * ΔT / L
            q = k * A * dT / L
            self.cond_q.setText(f"{q:.4f}")
            
            self.update_status("Conduction heat transfer calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def calculate_convection(self):
        """Calculate convection heat transfer."""
        try:
            h = float(self.conv_h.text())
            A = float(self.conv_A.text())
            dT = float(self.conv_dT.text())
            
            if h <= 0 or A <= 0:
                raise ValueError("h and A must be positive")
                
            # q = h * A * ΔT
            q = h * A * dT
            self.conv_q.setText(f"{q:.4f}")
            
            self.update_status("Convection heat transfer calculated successfully")
            
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {e}")
            self.update_status("Calculation failed")
            
    def clear_heat_tab(self):
        """Clear heat transfer tab."""
        self.cond_k.clear()
        self.cond_A.clear()
        self.cond_dT.clear()
        self.cond_L.clear()
        self.cond_q.setText("—")
        self.conv_h.clear()
        self.conv_A.clear()
        self.conv_dT.clear()
        self.conv_q.setText("—")
        self.update_status("Heat transfer tab cleared")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MechanicalToolkitApp()
    window.show()
    sys.exit(app.exec())

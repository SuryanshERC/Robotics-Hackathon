# Autonomous Warehouse Robot Electronics System

## 🚀 Objective
Design and simulate the complete **electronics system** for an **autonomous warehouse robot** using **TinkerCAD**. The system must be:
- Efficient
- Reliable
- Capable of controlling robot movements and core warehouse functions

---

## 🛠️ System Overview

### 🔌 Simulation Platform
- **Tool**: [TinkerCAD Circuits](https://www.tinkercad.com/)
- **Assumptions**:
  - All simulated components meet required torque and power specs
  - Real-world discrepancies are documented

### 🧠 Microcontrollers
- **2 x Arduino UNO**
  - **Master Arduino**: Decision-making & communication
  - **Slave Arduino**: Motor control & sensor interface

---

## 🔧 System Functions

### 1. Differential Drive Movement
- Control **4 DC motors**
- Provide forward, reverse, and turning capability

### 2. Forklift Mechanism
- Control **2 DC motors with encoders**
- Enable precise **vertical movement**

### 3. Conveyor Belt System
- Control **2 DC motors with encoders**
- Operate the **prong conveyor system**

---

## 📡 Sensing Systems

| Sensor Type         | Function                                          |
|---------------------|---------------------------------------------------|
| Ultrasonic Sensor   | Object position detection on conveyor belt       |
| Limit Switches      | Forklift boundary detection (upper & lower)      |
| Encoders            | Feedback for motor position & control accuracy   |

---

## 🔋 Power System

- **Total Power Calculations**:
  - Estimate power consumption of all motors & sensors
  - Factor in operating voltage, current, and safety margins

- **Component List**:
  - Realistic part selection based on:
    - Motor torque/power specs
    - Sensor and control circuitry requirements

---

## 🧩 PCB Design (KiCad)

- **Slave Arduino UNO Shield**
  - Includes:
    - Motor drivers (e.g., L298N, TB6612FNG)
    - Encoder interfaces
    - Screw terminals for external connections

- **Design Considerations**:
  - Track thickness calculations for power paths
  - Proper footprint placement
  - Minimized wiring complexity
  - Compliance with actual part datasheets

---

## 💻 Software Requirements

### Communication
- **I²C Serial Communication** between Master and Slave Arduinos

### Control Logic
- Implement subsystem-specific algorithms for:
  - Navigation
  - Lifting
  - Conveyor timing

### Safety Features
- Emergency stop logic
- Limit switch-based motion halts

### Code Documentation
- Clear, modular code
- Commented thoroughly for:
  - Sensor inputs
  - Motor control logic
  - Communication protocols

---

## 📓 General Notes

- ✅ All assumptions are documented
- ✅ PCB footprints and specifications match real-world components
- ✅ Key differences between TinkerCAD simulation and actual hardware are addressed

---

## 🌟 Bonus Creativity

- You are **encouraged** to explore other microcontrollers beyond Arduino UNO (e.g., ESP32, STM32, Teensy)
- Optional features may include:
  - Bluetooth/Wi-Fi diagnostics
  - OLED display for debugging
  - Battery management systems

---

## 📁 Project Structure


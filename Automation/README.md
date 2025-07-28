# 🤖 Autonomous Warehouse Management Robot – Automation System

## 🎯 Objective
Design and implement the complete **automation system** for an **autonomous warehouse robot** using **ROS 2 Humble** and **Gazebo Fortress Ignition**.  
The robot should:
- Navigate the warehouse environment
- Detect and organise misplaced packages
- Avoid static and dynamic obstacles

---

## 🏗️ Simulation Setup

- **Middleware**: ROS 2 Humble
- **Simulator**: Gazebo Fortress Ignition
- **World**: Provided `.sdf`/`.world` warehouse environment (see *Setup Instructions* below)
- **Start Position**: Robot begins at a predefined home location
- **Environment**:
  - **Shelves**: RGBY-color-coded shelves for different companies
  - **Obstacles**: Static human models, trolleys, pallets, and bins

---

## 🧠 Primary Tasks

### 📦 Inventory Management
- **Box Detection** on shelves
- **Colour-Based Identification**:
  - Red (R), Green (G), Blue (B), Yellow (Y)
- **AruCo Marker Detection**:
  - 5x5 AruCo markers (IDs 0–19)
  - Marker encodes the **Shelf and Rack Number**
- **Reorganisation**:
  - Move misplaced boxes to correct positions based on **Appendix 1**
  - Compute **optimal paths** to complete the reorganisation

### 🧹 Floor Priority System
- Detect **misplaced boxes on the floor**
- Smart decision-making:
  - Decide whether to **complete current task** or **interrupt it** to address floor boxes
  - Resume previous task after floor cleanup

---

## 🧩 Technical Requirements

### 🔄 Path Planning
- Implement **RRT/RRT\*** or **A\*** for navigating:
  - Maze-like warehouse
  - Multi-objective path optimisation: task completion & safety

### 🚶 Dynamic Obstacle Avoidance
- Handle **moving people**
- Re-plan paths in real time to avoid dynamic collisions

### 🎮 Control System
- **Collision Avoidance** with shelves, boxes, humans
- **Emergency Stop** for safety on critical trigger

### 👁️ Computer Vision
- **OpenCV** for all vision tasks
- Real-time processing of camera feed
- **Color Recognition** (RGBY)
- **AruCo Marker** reading for location tagging and rack ID extraction

---

## 📋 General Instructions

- Document all **assumptions**, **design choices**, and **edge cases**
- Implement robust **error handling** and **recovery mechanisms**
- Include **comprehensive comments** and clean ROS 2 node documentation
- Test thoroughly inside Gazebo before deployment

---

## 🌟 Bonus Points

| Feature                       | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 📨 Custom ROS 2 Messages     | Define custom message types for warehouse tasks                             |
| 🤖 Multi-Robot Coordination  | Implement basic multi-robot collaboration logic                             |
| 🧠 Machine Learning          | Improve box detection/classification using lightweight ML models (e.g., CNN)|

---

## 🔧 Setup Instructions

> **NOTE**: World file and robot URDF will be added soon.

### ✅ ROS 2 Humble Installation
Follow official instructions: [ROS 2 Humble Install Guide](https://docs.ros.org/en/humble/Installation.html)

### ✅ Gazebo Fortress Installation
Install instructions: [Gazebo Fortress](https://gazebosim.org/docs/fortress/install)

**Why Fortress?**
- Better compatibility with ROS 2 Humble
- Stable physics engine for warehouse-scale simulation

---

## 📁 Recommended Project Structure


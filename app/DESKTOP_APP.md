"""CAUGU Desktop App - Electron Setup"""

This guide helps you create a desktop app for CAUGU.

## Setup Instructions

### Prerequisites
- Node.js 16+
- npm

### Create Project

```bash
npm install -g electron-forge
electron-forge import
```

### Install Dependencies

```bash
npm install axios react react-dom
```

### Project Structure

```
.
├── src/
│   ├── index.js
│   ├── preload.js
│   ├── renderer.js
│   └── components/
├── public/
│   └── index.html
└── package.json
```

### Main Process (src/index.js)

- Window management
- IPC communication
- System tray integration

### Run Development

```bash
npm start
```

### Build for Distribution

```bash
npm run make
```
